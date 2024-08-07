from flask import Flask, request, render_template, jsonify
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline
import os
import logging

# Setup basic configuration for logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Flask application
application = Flask(__name__)
app = application

# Route for the home page
@app.route('/')
def home_page():
    return render_template('index.html')

# Route to display the prediction form and handle predictions
@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        # Render the prediction form
        return render_template('form.html')
    else:
        # Validate and extract data from form submission
        try:
            if not all([request.form.get(field) for field in ['carat', 'depth', 'table', 'x', 'y', 'z', 'cut', 'color', 'clarity']]):
                return render_template('form.html', error="All fields are required.")

            data = CustomData(
                carat=float(request.form.get('carat')),
                depth=float(request.form.get('depth')),
                table=float(request.form.get('table')),
                x=float(request.form.get('x')),
                y=float(request.form.get('y')),
                z=float(request.form.get('z')),
                cut=request.form.get('cut'),
                color=request.form.get('color'),
                clarity=request.form.get('clarity')
            )
            # Convert data to DataFrame suitable for prediction
            final_new_data = data.get_data_as_dataframe()
            # Initialize the prediction pipeline
            predict_pipeline = PredictPipeline()
            # Make prediction
            pred = predict_pipeline.predict(final_new_data)
            results = f"Predicted Price: ${round(pred[0], 2)}"
        except Exception as e:
            # Log the error and return a generic error message
            logging.error(f"Error during prediction: {str(e)}")
            results = "An error occurred during the prediction process. Please try again."
        
        # Render the form again with the results
        return render_template('form.html', final_result=results)

# Main block to run the application
if __name__ == '__main__':
    DEBUG_MODE = os.environ.get('DEBUG_MODE', 'False').lower() == 'true'
    PORT = int(os.environ.get('PORT', 5002))
    app.run(debug=DEBUG_MODE, host='0.0.0.0', port=PORT)

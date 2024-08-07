from flask import Flask, request, render_template, jsonify
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

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
        # Extract data from form submission
        try:
            data = CustomData(
                carat=float(request.form.get('carat', 0)),
                depth=float(request.form.get('depth', 0)),
                table=float(request.form.get('table', 0)),
                x=float(request.form.get('x', 0)),
                y=float(request.form.get('y', 0)),
                z=float(request.form.get('z', 0)),
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
            results = round(pred[0], 2)
        except Exception as e:
            # Handle errors during form processing or prediction
            results = f"Error: {str(e)}"
        
        # Render the form again with the results
        return render_template('form.html', final_result=results)

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)  # Change to port 5002


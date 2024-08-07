# Diamond Price Predictor

This project develops a machine learning model to predict diamond prices based on various features such as carat, depth, table, and physical dimensions (x, y, z). The model and its preprocessing pipeline are deployed as a web application using Flask.

## Project Structure

```
Diamond-Price-Prediction/
├── artifacts/
│   ├── model.pkl            # Trained model
│   ├── preprocessor.pkl     # Preprocessing pipeline
├── data/
│   ├── raw.csv              # Raw data
│   ├── test.csv             # Test dataset
│   ├── train.csv            # Training dataset
│   ├── gemstone.csv         # Additional data
├── notebooks/
│   ├── EDA.ipynb            # Exploratory Data Analysis
│   ├── Model Training.ipynb # Notebook for training models
├── src/
│   ├── components/          # Modular components of the application
│   ├── pipelines/           # Data processing and ML pipelines
│   ├── exception.py         # Exception handling module
│   ├── logger.py            # Logging module
│   ├── utils.py             # Utility functions
├── templates/
│   ├── form.html            # HTML form for input data
│   ├── index.html           # Main page of the web application
├── .gitignore               # Specifies intentionally untracked files to ignore
├── README.md                # README file for project documentation
├── application.py           # Flask application entry point
├── requirements.txt         # List of dependencies
├── setup.py                 # Setup script for the application
```

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/imaadiiii/Diamond-Price-Prediction.git
   ```
2. Navigate to the project directory:
   ```
   cd Diamond-Price-Prediction
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Flask application:
```
python application.py
```
Visit `http://127.0.0.1:5002` to access the application.

## Features

- **Predictive Modeling:** Utilizes Scikit-Learn for building a regression model to estimate diamond prices.
- **Data Visualization:** Notebooks include EDA with libraries like Seaborn and Pandas.
- **Web Interface:** Flask application for easy interaction with the predictive model.

## Screenshots

Screenshots of the application can be found in the `ScreenShot` directory:
- SS1.png
- SS2.png
- SS3.png

## Contributing

Contributions are welcome. Please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
```

### Notes on the README
- **Installation and Usage:** Clear instructions help users set up and start the application.
- **Project Structure:** Detailed breakdown of directories and files helps users navigate the project.
- **Features and Screenshots:** Highlights the main features and visual representation of the application.
- **Contributing and License:** Encourages contributions and notes the license.


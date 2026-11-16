
# Algerian Forest Fires — FWI Prediction

An end-to-end Machine Learning project that estimates
the Fire Weather Index (FWI) using historical data
from the Algerian Forest Fires dataset.

The project demonstrates data preprocessing, exploratory
data analysis, feature engineering, regression model
training, evaluation, and Flask web integration.

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Flask
- HTML and CSS
- Jupyter Notebook

## Machine Learning Workflow

1. Load the Algerian Forest Fires dataset.
2. Clean and preprocess the data.
3. Perform Exploratory Data Analysis (EDA).
4. Explore correlations and select features.
5. Split the data into training and testing sets.
6. Apply StandardScaler preprocessing.
7. Train and evaluate regression models.
8. Save the selected Ridge Regression model.
9. Integrate the trained model into Flask.

## Models Explored

- Linear Regression
- Ridge Regression
- Lasso Regression
- Elastic Net Regression

### Deployed Model

Ridge Regression with StandardScaler preprocessing.

### Reported Ridge Regression Results

- R-Squared (R²): 0.9843
- Mean Absolute Error (MAE): 0.5642

These results are from the project's notebook
evaluation on a held-out test split.

## Project Structure

```text
TestForestFires/
|-- application.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- dataset/
|   |-- Algerian_forest_fires_dataset.csv
|   |-- Algerian_forest_fires_cleaned_dataset.csv
|-- models/
|   |-- ridge.pkl
|   |-- standard_scaler.pkl
|-- notebooks/
|   |-- EDANFeatureEngineering.ipynb
|   |-- Model_Training.ipynb
|-- templates/
    |-- index.html
    |-- home.html
```

## Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd TestForestFires
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the Flask application

```bash
python application.py
```

Open your browser:

http://127.0.0.1:5000/

## Prediction Inputs

The application accepts nine inputs:

- Temperature
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rainfall
- Fine Fuel Moisture Code (FFMC)
- Duff Moisture Code (DMC)
- Initial Spread Index (ISI)
- Fire Class (Classes)
- Region

The model uses these inputs to estimate FWI.

## Limitations

This is an educational Machine Learning project,
not a real-time wildfire forecasting or warning system.

The current model uses the historical fire class as
an input, which may introduce target-related leakage.
Further evaluation without that feature is recommended.

Reported performance is based on a small historical
dataset and does not establish real-world reliability.

## Future Improvements

- Investigate and remove potential target leakage.
- Add stronger cross-validation and baseline comparisons.
- Add user input validation.
- Introduce automated testing.
- Improve deployment readiness.
- Add an online hosted demo.

## Dataset

Algerian Forest Fires Dataset,
available through the UCI Machine Learning Repository.
```
from flask import Flask,render_template,request,jsonify
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# Create Flask application
application = Flask(__name__)
app = application

#import regressor and and standard scaler
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/standard_scaler.pkl','rb'))


# Home page
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_point():
    if request.method=='POST':

        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = float(request.form.get("Classes"))
        Region = float(request.form.get("Region"))

        if Region == 0:
            region_name = "Bejaia"
        elif Region == 1:
            region_name = "Sidi Bel-Abbes"
        else:
            raise ValueError("Invalid region selected")

        # Step 2: Prepare input values
        input_data = [[
            Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region
        ]]

        # Step 3: Standardize input
        new_data_scaled = standard_scaler.transform(input_data)

        # Step 4: Predict FWI
        result = ridge_model.predict(new_data_scaled)

        # Step 5: Get predicted value
        # prediction = result[0]
        prediction = round(float(result[0]), 2)

        # print("Model:", type(ridge_model).__name__)
        # print("Features:", standard_scaler.n_features_in_)
        # print("Scaled inputs:", new_data_scaled)
        # print("Prediction:", result[0])

        # Step 6: Display prediction in HTML
        return render_template(
            "home.html",
            prediction=prediction
        )
        
    else:
        return render_template('home.html')

# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)
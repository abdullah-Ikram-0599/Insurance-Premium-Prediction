from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask("__name__")



## Route for a home page

@application.route('/')
def index():

    return render_template('index.html')

@application.route('/predictdata', methods = ['GET', 'POST'])
def predict_datapoint():

    if request.method == 'GET':

        return render_template('home.html')

    else:

        data = CustomData(

            age = int(request.form.get('age')),
            gender = request.form.get('gender'),
            bmi= float(request.form.get('bmi')),
            children=int(request.form.get('children')),
            smoke = request.form.get('smoke'),
            region = request.form.get('region')
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results = results[0])
    
if __name__ == "__main__":

    application.run(debug=True)

    





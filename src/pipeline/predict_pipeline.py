import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os
class PredictPipeline:

    def __init__(self):

        pass
    # def predict(self, features):

    #     try: 

    #         model_path = "artifacts\model.pkl"
    #         preprocessor_path = "artifacts\preprocessor.pkl"

    #         model = load_object(file_path = model_path)
    #         preprocessor = load_object(file_path=preprocessor_path)
    #         data_scaled = preprocessor.transform(features)
    #         preds = model.predict(data_scaled)
    #         return preds
        
    #     except Exception as e:

    #         raise CustomException(e, sys)

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:

    def __init__(self, 
                 
                 age: int,
                 gender: str,
                 bmi: float,
                 children: int,
                 smoke: str,
                 region: str
                 ):
        self.age = age

        self.gender = gender

        self.bmi = bmi

        self.children = children

        self.smoke = smoke

        self.region = region

    def get_data_as_data_frame(self):

        try:

            custom_data_input_dict = {

                "age": [self.age],

                "sex": [self.gender],

                "bmi": [self.bmi],

                "children": [self.children],

                "smoker": [self.smoke],

                "region": [self.region]
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:

            raise CustomException(e, sys)


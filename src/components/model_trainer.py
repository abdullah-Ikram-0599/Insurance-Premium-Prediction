import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from xgboost import XGBRegressor
from sklearn.metrics import r2_score


from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:

    trained_model_file_path = os.path.join("C:/Users/91999/Desktop/VSCode/Insurance-Premium-Prediction/artifacts", "model.pkl")

class ModelTrainer:

    def __init__(self):

        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):

        try:
            logging.info("Split train and test input data")

            X_train, y_train, X_test, y_test = (

                train_array[:,:-1], 
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {

                "XGBRegressor": XGBRegressor()
            }

            params={
          
                "XGBRegressor":{'max_depth': [5,10, 15, 20, 25, 30],'learning_rate':[0.001, 0.01, 0.1, 0.5], 
                                'n_estimators': [100,150,200, 250, 300], 'subsample': [0.6, 0.7, 0.8] },
            
                }

            model_report: dict = evaluate_models(X_train = X_train, y_train =y_train,X_test=X_test, y_test=y_test, models = models, param = params)

            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict
            best_model_name = list(model_report.keys())[ 

                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score < 0.6:

                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            
            r2_square = r2_score(y_test, predicted)

            return r2_square

        except Exception as e:
            raise CustomException(e, sys)


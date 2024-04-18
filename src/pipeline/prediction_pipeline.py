import sys 
import os 
from src.exception import CustomException 
from src.logger import logging 
from src.utils import load_obj
import pandas as pd

class PredictPipeline: 
    def __init__(self) -> None:
        pass

    def predict(self, features): 
        try: 
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_obj(preprocessor_path)
            model = load_obj(model_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e: 
            logging.info("Error occured in predict function in prediction_pipeline location")
            raise CustomException(e,sys)
        
class CustomData: 
        def __init__(self, dsa:int, 
                     cgpa:float, 
                     Kml:str,
                     Kdsa:str,
                     Kpython:str,
                     KJavascript:str,
                     club:str,
                     backlogs:int
                     ): 
             self.dsa = dsa
             self.cgpa = cgpa
             self.Kml = Kml
             self.Kdsa = Kdsa
             self.Kpython = Kpython
             self.KJavascript = KJavascript
             self.club = club 
             self.backlogs = backlogs 
             
        
        def get_data_as_dataframe(self): 
             try: 
                  custom_data_input_dict = {
                       'No. of DSA questions': [self.dsa], 
                       'CGPA': [self.cgpa], 
                       'Knows ML': [self.Kml], 
                       'Knows DSA': [self.Kdsa],
                       'Knows Python':[self.Kpython],
                       'Knows JavaScript':[self.KJavascript], 
                       'Was in Coding Club': [self.club], 
                       'No. of backlogs': [self.backlogs] 
                       

                  }
                  df = pd.DataFrame(custom_data_input_dict)
                  logging.info("Dataframe created")
                  return df
             except Exception as e:
                  logging.info("Error occured in get_data_as_dataframe function in prediction_pipeline")
                  raise CustomException(e,sys) 
             
             
        
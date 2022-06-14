import joblib
import json
import logging
import os
import numpy

def init():
    global model
    
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model/regressor.pkl')
    model = joblib.load(model_path)
    
    logging.info('Init complete')

def run(data):
    logging.info('model 1: request received')
    
    try:
        MAE_SCORE = 2.284865e6
        
        data = json.loads(data)
        X = [list(data['data'].values())[3:]]
        
        pred_value = model.predict(X).tolist()[0]
        result = {
            'pred_value': pred_value
            , 'min_value': 0
            , 'max_value': pred_value + MAE_SCORE
        }
        
        logging.info('Prediction successed')
        
        return {
            'Result': result
            , 'Status': 'Successed'
        }
    
    except Exception as e:
        error = str(e)
        logging.info('[!!]', e)
        
        return {
            'Result': error
            , 'Status': 'Failed'
        }

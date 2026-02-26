import requests
from config import PREDICT_ENDPOINT

def get_prediction(data:dict):
    try:
        response = requests.post(PREDICT_ENDPOINT, json=data)
        if response.status_code==200:
            return response.json(), None
        else:
            return None, response.json()
    except Exception as e:
        return None, str(e)
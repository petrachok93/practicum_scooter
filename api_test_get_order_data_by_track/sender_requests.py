import configuration as c
import requests

def create_order(data):
    response = requests.post(c.URL_SERVICE + c.CREATE_ORDER_PATH, json=data)
    return response

def get_order(track):
    response = requests.get(c.URL_SERVICE + c.GET_ORDER_PATH, params={"t": track})
    return response

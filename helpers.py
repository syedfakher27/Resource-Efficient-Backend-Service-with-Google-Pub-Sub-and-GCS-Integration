import requests

def invoke_servce(url,body):
    response = requests.post(url,json=body)
    return response
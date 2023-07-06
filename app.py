import requests
import json

API_SERVER = "http://127.0.0.1:8080"
SET_CONFIG = "/v1.0/config/info"

def config(location='Taipei'):
    try:
        location='Taipei22'
        data = {
            'location': location
        }
        headers = {'Content-Type': 'application/json'}
        postConfigResponse = requests.post(url=API_SERVER + SET_CONFIG,
                                          headers=headers, data=json.dumps(data), verify=False)
        if postConfigResponse.status_code == 200:
            return "success"
        else:
            return "fail"
    except Exception as err:
        print('Other error occurred %s' % {err})


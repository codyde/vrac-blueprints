import requests
import json

def handler(context, inputs):
    
    ip = inputs['addresses'][0][0]
    
    url = "https://18.144.49.195/api/v2/inventories/1/hosts/"
    job = "https://18.144.49.195/api/v2/job_templates/5/launch/"
    
    enabled = True
    
    
    payload = {
    'name': ip,
    'enabled': enabled
    }
    
    pl = json.dumps(payload)
    
    headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic YWRtaW46cGFzc3dvcmQ="
    }
    
    limit = {
        'limit': ip
    }
    
    limit_json = json.dumps(limit)

    host_add = requests.post(url, data=pl, headers=headers, verify=False)
    
    job_exec = requests.post(job, data=limit_json, headers=headers, verify=False)
    
    status = {"status": "ok"}

    return status

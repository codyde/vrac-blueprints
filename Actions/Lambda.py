from requests
import json

def handler(context, inputs):
    name = inputs['resourceNames'][0]
    os = inputs['customProperties']['image']
    reqid = inputs['requestId']
    print(name)
    data = {"text":"Your VM named "+name+" has completed\n The Operating System is "+os+"\n For future API calls your request ID is "+reqid}
    url = "https://hooks.slack.com/services/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"
    r = requests.post(url, data = json.dumps(data), verify=False)
    if r.status_code == 200:
        print("success")
        outputs = {"statusCode":r.status_code}
        return outputs
    else:
        print("Failure")
        outputs = {"statusCode":r.status_code}
        return outputs

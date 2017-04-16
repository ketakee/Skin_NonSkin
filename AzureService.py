import urllib
import json 

data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["B", "G", "R", "Skin"],
                    "Values": [ [ "0", "0", "0", "0" ], [ "0", "0", "0", "0" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/89defe37884340ee931a2acffd739102/services/fa07dea439e74bbfaf6771a684ea933a/execute?api-version=2.0&details=true'
api_key = 'insert the key here'
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers) 
response = urllib.request.urlopen(req)
result = response.read()
print(result) 

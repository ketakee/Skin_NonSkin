import urllib
# If you are using Python 3+, import urllib instead of urllib

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
api_key = 'Yh7QvhdBt38zFMljVkSNGpAwAsUVbHq1yxGF+BoQ9MHoheE6UnauqfZSP0Gywupuix4rPbU7P1GYHu8Yd19H1g=='# Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers) 
response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

result = response.read()
print(result) 

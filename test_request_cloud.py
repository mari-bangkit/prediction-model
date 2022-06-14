#!/usr/bin/env python

import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data
data = {
    "data": {
        "Customer Name": "Foo Bar",
        "Customer e-mail": "foobar@baz.com",
        "Country": "Indonesia",
        "Gender": 1,
        "Age": 24,
        "Annual Salary": 120000000,
        "Credit Card Debt": 12000000,
        "Net Worth": 300000000
    }
}

body = str.encode(json.dumps(data))

url = os.environ['AZURE_ML_URL']
api_key = os.environ['AZURE_ML_API_KEY']

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {"Content-Type":"application/json", "Authorization":("Bearer "+ api_key), "azureml-model-deployment": "initial" }

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(json.loads(result))
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))

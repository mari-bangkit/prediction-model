#!/usr/bin/env python

import requests
import json
import os


url = os.environ['AZURE_ML_URL_LOCAL']

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

r = requests.post(url, str.encode(json.dumps(data)))

print(r.json())
# Program to print a JSON file from a URL
# Author: Sharon Curley

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(data)

# review done
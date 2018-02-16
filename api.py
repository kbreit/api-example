#!/usr/bin/python3

from requests.auth import HTTPBasicAuth
import requests

dnaC = "https://sandboxdnac.cisco.com"
username = "devnetuser"
password = "Cisco123!"

authURL = dnaC + "/api/system/v1/auth/login"
r = requests.get(authURL, auth=HTTPBasicAuth(username, password), verify=False)
# print(r.headers)
cookie = r.headers['Set-Cookie']
# print(cookie)

requestHeader = {'Cookie': cookie}
inventoryURL = dnaC + "/api/v1/network-device"
inventoryResponse = requests.get(inventoryURL, auth=HTTPBasicAuth(username, password), verify=False, headers=requestHeader)
# print(inventory.text)
inventory = inventoryResponse.json()
print(inventory['response'][0]['type'])
deviceName = inventory['response'][0]['type']
deviceLocation = inventory['response'][0]['location']
print(deviceLocation)
if deviceLocation is None:
	print(deviceName + " has no location")
else:
	print(deviceName + " is located at " + deviceLocation)
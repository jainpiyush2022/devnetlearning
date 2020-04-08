# This program is connecting to IOS XE device using restconf and pulling the operation status of GigabitEthernet1
import requests
import json
from pprint import pprint

router = {
    "host" : "ios-xe-mgmt-latest.cisco.com",
    "port" : "9443",
    "username" : "developer",
    "password" : "C1sco12345"
}


url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

print(url)

payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("GET", url, headers=headers, data = payload,verify=False)

api_data = response.json()
pprint('/' * 50)
pprint(f"Interface Description :{ api_data['Cisco-IOS-XE-interfaces-oper:interface']['description']} \n Interface Status: { api_data['Cisco-IOS-XE-interfaces-oper:interface']['admin-status']}")
pprint('/' * 50)

# This program connects to NX-OS API CLI and run the show command.
import requests
import json
from pprint import pprint

"""
This is NX-OS device
"""
url='https://sbx-nxos-mgmt.cisco.com/ins'
switchuser='admin'
switchpassword='Admin_1234!'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show ip int brief",
      "version": 1
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),verify=False).json()

interfaces = response['result']['body']['TABLE_intf']['ROW_intf']

print("Interface Name \t IP address \t Admin-State \t Protocol-State ")
for interface in interfaces:
    print(interface['intf-name'],"\t", interface['prefix'], "\t",interface['admin-state'], "\t\t",interface['proto-state'])
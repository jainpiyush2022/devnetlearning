import requests
import json
from pprint import pprint

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload = "{\n\"aaaUser\": {\n\"attributes\": {\n\"name\": \"admin\",\n\"pwd\": \"Admin_1234!\"\n}\n}\n}"
headers = {
  'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data = payload,verify=False).json()

token = response['imdata'][0]['aaaLogin']['attributes']['token']

#print(token)

cookies = {}
cookies['APIC-cookie'] = token

url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/phys-[eth1/97].json"

payload = "{\n    \"l1PhysIf\": {\n          \t\"attributes\": {\n          \t\t\"descr\": \" \"\n          \t}\n    }\n}"
headers = {
  'Content-Type': 'application/json',
}

response_put = requests.put(url, headers=headers, data = payload,cookies=cookies,verify=False)

if (response_put.status_code == 200):
    print("Successfully updated the configuration!")




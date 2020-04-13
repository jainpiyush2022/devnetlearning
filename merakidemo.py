import requests
import json
from pprint import pprint

url = "https://dashboard.meraki.com/api/v0/organizations"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '025a21071ae517fca144cfe2e16a2f0d371648ef'
}

response = requests.get(url, headers=headers, data = payload).json()

OrganizationId = response[0]['id']

print("OrganizationID : " , OrganizationId)

url = f"https://dashboard.meraki.com/api/v0/organizations/{OrganizationId}/networks"


response = requests.get(url, headers=headers, data = payload).json()

for net in response:
    if net['name'] == 'DNSMB5':
        networkId = net['id']

print("NetworkID : ", networkId)

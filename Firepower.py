import json
import requests
from pprint import pprint

### Login to Firepower and get the token from Headers #######

url = 'https://fmcrestapisandbox.cisco.com/api/fmc_platform/v1/auth/generatetoken'

headers = {
  'Content-Type': 'application/json'
}

username = 'piyujain'
password = 'ABpTW2z8'

response = requests.post(url, headers=headers, auth=(username,password), verify=False)
token = response.headers['X-auth-access-token']
print(token)

#### Now you can use this token to run other APIs. In this example we will configure Access policies ####

url = 'https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies'

# Add the token to the headers
headers['X-auth-access-token'] = token

payload = {
"type": "AccessPolicy",
"name": "CBT Nuggets AC Policy ",
"description": "CBT Nuggets Policy to Block and Detect Threats",
"defaultAction": {
 "intrusionPolicy": {
   "name": "Security Over Connectivity",
   "id": "abba9b63-bb10-4729-b901-2e2aa0f4491c",
   "type": "IntrusionPolicy"
 },
 "variableSet": {
   "name": "Default Set",
   "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
   "type": "VariableSet"
 },
 "type": "AccessPolicyDefaultAction",
 "logBegin": False,
 "logEnd": True,
 "sendEventsToFMC": True
}
}

### Commented the post after created the policy ###
response_pol = requests.post(url,headers=headers,data=json.dumps(payload),verify=False).json()

url = 'https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies?limit=200'

response_pol = requests.get(url,headers=headers,verify=False).json()

policies = response_pol['items']

for policy in policies:
    if policy['name'] == "CBT Nuggets AC Policy":
        policyId = policy['id']

print('CBT Nuggets AC Policy: ',policyId)


#### You can print the policy using the policy id ####

url = f'https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/{policyId}'

response_pol = requests.get(url,headers=headers,verify=False).json()

pprint(response_pol)

### You can add the rules to this policy #####

url = f'https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/{policyId}/accessrules'

payload ={
  "sendEventsToFMC": True,
  "action": "ALLOW",
  "enabled": True,
  "type": "AccessRule",
  "name": "CBT Nugget Malware Inspect",
  "logFiles": True,
  "logBegin": False,
  "logEnd": False,
  "variableSet": {
    "name": "Default Set",
    "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
    "type": "VariableSet"
  },
  "sourceNetworks": {
    "objects": [{
      "type": "NetworkGroup",
      "name": "IPv4-Private-All-RFC1918",
      "id": "15b12b14-dace-4117-b9d9-a9a7dcfa356f"
    }]
  },
  "filePolicy": {
    "name": "New Malware",
    "id": "59433a1e-f492-11e6-98fd-84ec1dfeed47",
    "type": "FilePolicy"
  }
}

response_rules = requests.post(url,headers=headers,data=json.dumps(payload),verify=False)
print('Access rules created with ',response_rules.status_code)

### Now delete the policy 

url = f'https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/{policyId}'

response_pol = requests.delete(url,headers=headers,verify=False)
print('Policy Deleted with ', response_pol.status_code)



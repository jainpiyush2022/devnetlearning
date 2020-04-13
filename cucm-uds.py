import requests
import xmltodict
 

url = "https://10.10.20.1/cucm-uds/users"

payload = {}
headers = {
  'Content-Type': 'application/xml',
  'Accept': 'application/xml',
  'Authorization': 'Basic YWRtaW5pc3RyYXRvcjpjaXNjb3BzZHQ='
}

response = requests.get(url, headers=headers, data = payload,verify=False)

tree = xmltodict.parse(response.text.encode('utf8'))

users = tree['users']['user']

for user in users:
    print(user['id'], user['userName'],user['firstName'], user['lastName'])
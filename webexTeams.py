import json
import requests

token = 'NzdlY2I0ZDQtZDAyMi00MzdiLWI4MGMtYTRkNGExNjY0NmE5MzliZTU1MmItN2Q0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'

url = 'https://api.ciscospark.com/v1/teams'

body = {
    'name' : 'CBT Team'
    }

headers = {'Authorization': f'Bearer {token}','Content-Type' : 'application/json'}
# Create a new team
# r = requests.post(url, data=json.dumps(body), headers= headers).json()

# print(r)
# You can now pull the names of all the Teams and look for CBT Team

teams = requests.get(url, headers= headers).json()

#print(teams)

for team in teams['items']:
    if team['name'] == 'CBT Team':
        teamid = team['id']

print(teamid)

### CREATE A ROOM ###
room_url = 'https://api.ciscospark.com/v1/rooms'

room_body = {
    'title' : 'CBT Room',
    'teamId' : teamid
    }

# r = requests.post(room_url, data=json.dumps(room_body), headers= headers).json()


# You can now pull the names of all the Teams and look for CBT Team

rooms = requests.get(room_url, headers= headers).json()

# print(rooms)

for room in rooms['items']:
    if room['title'] == 'CBT Room':
        roomid = room['id']

print(roomid)


### POST A MESSAGE IN THE ROOM ###
message_url = 'https://api.ciscospark.com/v1/messages'

message_body = {
    'text' : 'Hello Guys! how are you? Corona Virus has ended.',
    'roomId' : roomid
    }

r = requests.post(message_url, data=json.dumps(message_body), headers= headers).json()


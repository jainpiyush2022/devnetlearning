from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

token = '025a21071ae517fca144cfe2e16a2f0d371648ef'

meraki = MerakiSdkClient(token)

orgs = meraki.organizations.get_organizations()

pprint(orgs)

collect = {}
organization_id = orgs[0]['id']
collect['organization_id'] = organization_id

networks = meraki.networks.get_organization_networks(collect)

#pprint(networks)
pprint('---' * 20)
for network in networks:
    pprint(network)
    if network['name'] == 'DNSMB1':
        netid = network['id']
        pprint(f"Network ID : {netid} ")

print('-' * 50)

collect = {}
collect['network_id'] = netid
clients = meraki.clients.get_network_clients(collect)

pprint(clients)
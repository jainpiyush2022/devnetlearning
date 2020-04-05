# This program is reading the CWM sync status json file
import json

with open('json-file-sample.json') as stream:
    jsonobject = json.loads(stream.read())
    #jsonobject = json.load(stream)  >>> This can also work

    status_list = jsonobject['CUCMs_Sync']

    print('Cluster', 'Last Sync Status' , 'last_Sync_StartTimestamp_UTC')
    
    for cluster in status_list:
        print(cluster + '\t' + status_list[cluster]['last_Sync_Status'] + '\t\t' + status_list[cluster]['last_Sync_StartTimestamp_UTC'] )
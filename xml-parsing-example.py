# This example parses the xml file got from CIMC to check the HDD status and errors.
import xmltodict

with open('xml-file-sample.xml') as stream:
    xml = xmltodict.parse(stream.read())
    
    hdds = xml['configResolveClass']['outConfigs']['storageLocalDiskProps']
    
    print('physicalDrive pdStatus health bootDrive mediaErrorCount otherErrorCount predictiveFailureCount ')
    
    for hdd in hdds:
        print(hdd['@physicalDrive'] + '\t\t' + hdd['@pdStatus'] + '\t' + hdd['@health'] + '\t' + hdd['@bootDrive'] + '\t' +
        hdd['@mediaErrorCount'] + '\t\t' + hdd['@otherErrorCount'] + '\t\t' + hdd['@predictiveFailureCount']  )


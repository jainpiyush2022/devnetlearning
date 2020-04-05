import yaml
from yaml import load,load_all

with open('yaml-file-sample.yml') as stream:
    documents = load_all(stream,Loader=yaml.FullLoader)
    print(type(documents))
    for doc in documents:
        print(type(doc))
        for key in doc:
            print(key, doc[key])

import json
from pprint import pprint

with open('example.json') as j:
    data = json.load(j)

for doc in data['data']:
    for ind in doc['actions']:
        pprint(ind)        
#pprint(data['data'][0]['actions'])
#pprint(data['data'][1]['actions'])

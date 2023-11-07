import json

with open('fcc.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    #print(fcc_data)
    
    print(json.dumps(fcc_data, indent=4, sort_keys=True))


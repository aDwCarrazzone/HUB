import json

try:
    config = json.load(open('configDB.json'))
    print('ConnectionString = {}'.format(config['connectionString']))
except:
    print('Configuration file not found or nonexistent!')

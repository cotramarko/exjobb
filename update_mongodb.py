from pymongo import MongoClient
import json
from copy import deepcopy
client = MongoClient()

db = client.exjobb
coll = db.dataset

current_data = list(coll.find())
new_data = deepcopy(current_data)
#fake insert some outdated
for x in range(5):
    coll.insert(dict({'title':'Outdated job' + str(x)}))
    current_data.append(dict({'title':'Outdated job' + str(x)}))


#fake insert some outdated
for x in range(5):
    new_data.append(dict({'title':'Hot new job' + str(x)}))



current_data_titles = set([x['title'] for x in current_data])
new_data_titles = set([x['title'] for x in new_data])


outdated = current_data_titles - new_data_titles
print('Outdated jobs = {}'.format(current_data_titles - new_data_titles))
print('Continued jobs = {}'.format(current_data_titles.intersection(new_data_titles)))
print('New jobs = {}'.format(new_data_titles - current_data_titles))



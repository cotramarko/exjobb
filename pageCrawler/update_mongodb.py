from pymongo import MongoClient
import json
from copy import deepcopy

def database_object():
    client = MongoClient()
    db = client.exjobb
    coll = db.dataset
    return coll

def remove_test_data():
    coll.remove({'company' : 'TestOrg'})

def update_database(crawlresult):
    coll = database_object()
    current_data = list(coll.find({},{ "_id" : 0}))

    current_data_titles = set([(x['title'], x['company']) for x in current_data])
    crawl_data_titles = set([(x['title'], x['company']) for x in crawlresult])

    outdated = current_data_titles - crawl_data_titles
    news = crawl_data_titles - current_data_titles


    print('Outdated',*outdated, sep='\n')
    print('New', *news, sep='\n')

    

def test_db():    
    coll = database_object()
    remove_test_data()

    current_data = list(coll.find({},{ "_id" : 0}))
    with open('mongo.json', 'w') as f:
            json.dump(current_data, f, ensure_ascii=False,indent=4, sort_keys=True)

    new_data = deepcopy(current_data)
    #fake insert some outdated
    for x in range(5):
        coll.insert(dict({'title':'Outdated job' + str(x), 'company' : "TestOrg"}))
        current_data.append(dict({'title':'Outdated job' + str(x), 'company':"TestOrg"}))

    #fake insert some new
    for x in range(5):
        new_data.append(dict({'title':'Hot new job' + str(x), 'company' : "TestOrg"}))

    current_data_titles = set([(x['title'], x['company']) for x in current_data])
    new_data_titles = set([(x['title'], x['company']) for x in new_data])


    outdated = current_data_titles - new_data_titles
    news = new_data_titles - current_data_titles

    #print('Outdated jobs = {}'.format(current_data_titles - new_data_titles))
    #print('Continued jobs = {}'.format(current_data_titles.intersection(new_data_titles)))
    #print('New jobs = {}'.format(new_data_titles - current_data_titles))

    for old_job in outdated:
        coll.update({'title' : old_job[0], 'company' : old_job[1]}, { "$set" : { 'inactive' : True} })

    new_content = []
    for thesis in new_data:
        if (thesis['title'], thesis['company']) in news:
            new_content.append(thesis)

    coll.insert_many(new_content)
    remove_test_data()




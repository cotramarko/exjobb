import json

def update_json(new_data):
    '''updates file, expects list of dictionaries'''

    with open('exjobb.json', encoding= 'utf-8') as f:
        #print(f.read())
        data = json.load(f)

    for entry in new_data:
        data.append(dict(entry))

    with open('exjobb.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False,indent=4, sort_keys=True)


if __name__ == '__main__':
    
    update_json([{"title":"okidoki"}])

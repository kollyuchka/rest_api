import json


def isEmpty(name, id): # If local repository is empty, fill it with initial data.

    with open('storage.json', 'w+') as f:
        data = {'data': [{'id':id, 'full_name':name}]}
        json.dump(data, f)

def add_or_edit(name,id): # Adds a new user or edits an old user.
    data = json.load(open('storage.json'))
    for  i in data["data"]:
        if i['id']==id:
            i['full_name'] = name
        else:
            data["data"].append({"id":id,"full_name":name })
    with open('storage.json', 'w') as f:
        json.dump(data, f)

def delete(id): #delete user
    data = json.load(open('storage.json'))
    for  i in data["data"]:
        if i['id']==id:
            data["data"].remove(i)
    with open('storage.json', 'w') as f:
        json.dump(data, f)

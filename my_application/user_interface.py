from my_application import db
from my_application.models import User
import json
import os
from abc import ABC,  abstractmethod
from flask import make_response, request

def is_non_zero_file(fpath):  # Сheck if file exists and is empty
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

def write_to_json(users):
    with open('storage.json', 'w+') as f:
        json.dump(users, f)

def users():
    return json.load(open('storage.json'))


class User_Interface(ABC):
    @abstractmethod
    def save(self, user):
        pass
    @abstractmethod
    def get(self, id):
        pass
    @abstractmethod
    def delete(self, id):
        pass
    @abstractmethod
    def edite(self, id, user):
        pass


class App_User_Interface(User_Interface):

    def save(self, name):
        if is_non_zero_file('storage.json'): # If file is not empty write user
            id  =len(users())+1
            users()[id] = name
            write_to_json(users())
        else:
            id = 1
            write_to_json({id: name})
        return User(name)


    def get(self, id):
        name =  users()[id]
        return User(name)


    def delete(self, id):
        look_user_name =  users()[id]
        users().pop(id)
        write_to_json(users())
        return User(look_user_name)

    def edite(self, id, name):
        look_user_name =  users()[id]
        users()[id] = name
        write_to_json(users())
        return User(look_user_name)


class Db_User_interface(User_Interface):

    def save(self, name):
        if bool(User.query.filter_by(full_name=name).first()):
            return make_response("User exists")
        else:
            user = User(full_name=name)
            db.session.add(user)
            db.session.commit()
        return user


    def get(self, id):
        user = User.query.get(id)
        return user


    def delete(self, id):
        delete_user = User.query.get(id)
        user = delete_user
        db.session.delete(user)
        return delete_user


    def edite(self, id):
        new_user = User(full_name=json.loads(request.data)["full_name"])
        old_user = User.query.get(id)
        editing_user = old_user
        old_user.full_name = new_user.full_name
        db.session.add(editing_user)
        db.session.commit()
        return old_user

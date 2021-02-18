from my_application import db
from my_application.models import User
import json
import os


def is_non_zero_file(fpath):  # Сheck if file exists and is empty
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0


def write_to_json(users):
    with open('storage.json', 'w+') as f:
        json.dump(users, f)


def users():
    return json.load(open('storage.json'))


class Repository():

    def save(self, user):
        pass

    def all(self):
        pass

    def get(self, id):
        pass

    def delete(self, id):
        pass

    def edite(self, id, user):
        pass


class App_Rep(Repository):

    def save(self, id, name):
        if is_non_zero_file('storage.json'):  # If file is not empty write user
            users()[id] = name
            write_to_json(users())
        else:
            write_to_json({id: name})

    def get(self, id):
        return users()[id]

    def delete(self, id):
        users().pop(id)
        write_to_json(users())

    def edite(self, id, user):
        users()[id] = user.name
        write_to_json(users())


class Db_Rep(Repository):

    def save(self, new_user):
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get(self, id):
        user = User.query.get(id)
        return user

    def delete(self, id):
        delete_user = User.query.get(id)
        user = delete_user
        db.session.delete(user)
        return user

    def edite(self, id, old_user, new_user):
        old_user.full_name = new_user.full_name
        db.session.add(old_user)
        db.session.commit()
        return new_user

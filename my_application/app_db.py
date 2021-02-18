from flask import make_response, request
from my_application import create_app, db
from my_application.repository import  Db_Rep
from my_application.models import User
import json


db_rep = Db_Rep()
app = create_app()
db.create_all(app=app)


class MyInterface():
    def create_user(self):
        pass

    def edite_user(self, id):
        pass

    def get_user(self, id):
        pass

    def delete_user(self, id):
        pass


class Interface_Db(MyInterface):

    @app.route("/user", methods=["POST"])  # Creating a new user in db.
    def create_user():
        full_name = json.loads(request.data)["full_name"]
        if bool(User.query.filter_by(full_name=full_name).first()):
            return make_response("User exists")
        else:
            user = User(full_name=full_name)
            db_rep.save(user)
            return make_response(f"{user} successfully created!")


    @app.route("/user/<id>", methods=["PUT"])  # Edit old user in db.
    def edite_user(id):
        new_user = User(full_name=json.loads(request.data)["full_name"])
        db_rep.edite(id, new_user)
        return make_response(f"user replaced {new_user}")


    @app.route("/user/<id>", methods=["GET"])  # Get user by id.
    def get_user(id):
        user = db_rep.get(id)
        return make_response(f"{user}")

    @app.route("/user/<id>", methods=["DELETE"])  # Delete user by id.
    def delete_user(id):
        user = db_rep.delete(id)
        return make_response(f"{user} deleted")


if __name__ == '__main__':
    app.run(debug=True)

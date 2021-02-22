from flask import make_response, request
from my_application import create_app, db
from my_application.user_interface import  Db_User_interface
import json


db_rep = Db_User_interface
app = create_app()
db.create_all(app=app)



class Interface_Db():

    @app.route("/user", methods=["POST"])  # Creating a new user in db.
    def create_user():
        full_name = json.loads(request.data)["full_name"]
        user = db_rep.save(full_name)
        return make_response(f"{user} successfully created!")


    @app.route("/user/<id>", methods=["PUT"])  # Edit old user in db.
    def edite_user(id):
        full_name = json.loads(request.data)["full_name"]
        user = db_rep.edite(id, full_name)
        return make_response(f"user  {user} replaced {full_name}")


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

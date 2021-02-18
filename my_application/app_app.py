from flask import make_response, request
from my_application import create_app, db
from my_application.repository import App_Rep
from my_application.models import User
from my_application.app_db import MyInterface
import json

app_rep = App_Rep()
app = create_app()
db.create_all(app=app)


class Interface_App(MyInterface):
    @app.route("/user", methods=["POST"])  # Creating a new user in app repository.
    def create_user():
        full_name = json.loads(request.data)["full_name"]
        user = User.query.get(full_name)
        app_rep.save(user.id, user.full_name)
        return make_response(f"{user} successfully created!")

    @app.route("/user", methods=["POST"])  # Edite user in app repository.
    def edite_user(id):
        new_user = User(full_name=json.loads(request.data)["full_name"])
        app_rep.edite(id, new_user)
        return make_response(f"user replaced {new_user}")

    @app.route("/user/<id>", methods=["GET"])  # Get user by id.
    def get_user(id):
        user = app_rep.get(id)
        return make_response(f"{user}")

    @app.route("/user/<id>", methods=["DELETE"])  # Delete user by id.
    def delete_user(id):
        app_rep.delete(id)
        user = app_rep.delete(id)
        return make_response(f"{user} deleted")


if __name__ == '__main__':
    app.run(debug=True)

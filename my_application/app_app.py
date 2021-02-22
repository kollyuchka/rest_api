from flask import make_response, request
from my_application import create_app, db
from my_application.user_interface import App_User_Interface
import json

app_rep = App_User_Interface()
app = create_app()
db.create_all(app=app)


class Interface_App():
    @app.route("/user", methods=["POST"])  # Creating a new user in app repository.
    def create_user():
        full_name = json.loads(request.data)["full_name"]
        user =  app_rep.save(full_name)
        return make_response(f" User {user} successfully created!")


    @app.route("/user", methods=["POST"])  # Edite user in app repository.
    def edite_user(id):
        full_name=json.loads(request.data)["full_name"]
        user = app_rep.edite(id, full_name)
        return make_response(f"user{user} replaced {full_name}")


    @app.route("/user/<id>", methods=["GET"])  # Get user by id.
    def get_user(id):
        user = app_rep.get(id)
        return make_response(f" User {user}")


    @app.route("/user/<id>", methods=["DELETE"])  # Delete user by id.
    def delete_user(id):
        user = app_rep.delete(id)
        make_response(f"{user} deleted")


if __name__ == '__main__':
    app.run(debug=True)

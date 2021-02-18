from flask import request, make_response
from my_application.models import User
import json
from my_application import create_app, db
from my_application.repository import App_Rep, Db_Rep

app_rep = App_Rep()
db_rep = Db_Rep()
app = create_app()
db.create_all(app=app)


class Actions():

    @app.route("/user", methods=["POST"])  # Creating a new user.
    def create_user():
        full_name = json.loads(request.data)["full_name"]
        if bool(User.query.filter_by(full_name=full_name).first()):
            return make_response("User exists")
        else:
            user = User(full_name=full_name)

            db_rep.save(user)  # Add a new user to db.
            user = User.query.get(full_name)
            app_rep.save(user.id, user.full_name)  # Add a new user to app repository.
            return make_response(f"{user} successfully created!")

    @app.route("/user/<id>", methods=["PUT"])  # Edit old user.
    def edite_user(id):
        new_user = User(full_name=json.loads(request.data)["full_name"])
        old_user = User.query.get(id)
        app_rep.edite(id, new_user)  # Editing user in app repository.
        db_rep.edite(id, old_user, new_user)  # Editing user in db.
        return make_response(f"user replaced {new_user}")

    @app.route("/user/<id>", methods=["GET"])  # Get user by id.
    def get_user(id):
        user = db_rep.get(id)
        return make_response(f"{user}")

    @app.route("/user/<id>", methods=["DELETE"])  # Delete user by id.
    def delete_user(id):
        app_rep.delete(id)  # Delete user from app repository.
        user = db_rep.delete(id)  # Delete user from db.
        return make_response(f"{user} deleted")

    @app.route("/user/all", methods=["GET"])  # Get user by id.
    def get_users():
        user = app_rep.all()
        return make_response(f"{user}")


if __name__ == '__main__':
    app.run(debug=True)

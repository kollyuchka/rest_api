from flask import request, make_response
from my_application.models import User
from my_application.additional_func import isEmpty, add_or_edit, delete
import json
import os
from my_application import app,db


class Actions():
    @app.route("/user", methods=["POST"])  # Creating a new user.
    def create_user():
        full_name = json.loads(request.data)["full_name"]
        if bool(User.query.filter_by(full_name=full_name).first()):
            return make_response("User exists")
        else:
            new_user = User(full_name=full_name)
            db.session.add(new_user)  # Add a new user to db.
            db.session.commit()
            if os.stat('storage.json').st_size == 0:
                isEmpty(new_user.full_name, new_user.id)
            add_or_edit(new_user.full_name, new_user.id)  # Add a new user to local repository.
        return make_response(f"user {new_user.full_name} successfully created!")


    @app.route("/user/<id>", methods=["PUT"])  # Edit old user.
    def edite_user(id):
        full_name = json.loads(request.data)["full_name"]
        existing_user = User.query.get(id)
        old_name = existing_user.full_name
        existing_user.full_name = full_name
        db.session.add(existing_user)  # Save the edited user to db.
        db.session.commit()
        add_or_edit(existing_user.full_name, existing_user.id) # Editing user in local storage.
        return make_response(f"user {old_name}"
                             f" replaced {existing_user.full_name}{f}")


    @app.route("/user/<id>", methods=["GET"])  # Get user by id.
    def get_user(id):
        existing_user = User.query.get(id)
        user_name = existing_user.full_name
        return make_response(f"user {user_name}")


    @app.route("/user/<id>", methods=["DELETE"]) # Delete user by id.
    def delete_user(id):
        delete_user = User.query.get(id)
        old_name = delete_user.full_name
        db.session.delete(delete_user)
        db.session.commit()
        delete(id) # Editing user in local storage.
        return make_response(f"user {old_name} deleted")


if __name__ == '__main__':
    app.run(debug=True)

from my_application import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, full_name):
        self.full_name = full_name

    def __repr__(self):
        return '<User %r>' % (self.full_name)

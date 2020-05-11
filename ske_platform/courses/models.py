from ske_platform.database import db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    id_ord = db.Column(db.Integer)
    path = db.Column(db.String(128), unique=True)

    # father_id of -1 represents
    # top-most course
    father_id = db.Column(db.Integer, nullable=True, default=-1)

    body_md = db.Column(db.String)
    body_html = db.Column(db.String)

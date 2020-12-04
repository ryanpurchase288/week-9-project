from application import db



class dateTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dateGenerate = db.Column(db.String(20), nullable=False)
    share = db.Column(db.String(250), nullable=False)
    
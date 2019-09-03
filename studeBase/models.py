from studeBase import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    full_names=db.Column(db.String(255),nullable=False)
    username=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(255),nullable=False)
    password=db.Column(db.Text(),nullable=False)
    
    def __repr__(self):
        return '{}'.format(self.username)
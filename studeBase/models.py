from studeBase import db,app
from flask_login import LoginManager,UserMixin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime

admin=Admin(app)


login_manager=LoginManager(app)

login_manager.login_view= 'Login'

#user loader callback

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    full_names=db.Column(db.String(255),nullable=False,unique=True)
    username=db.Column(db.String(255),nullable=False,unique=True)
    email=db.Column(db.String(255),nullable=False,unique=True)
    password=db.Column(db.Text(),nullable=False)
    
    def __repr__(self):
        return '{}'.format(self.username)

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),unique=True,nullable=False)
    age=db.Column(db.Integer(),nullable=False)
    gender=db.Column(db.String(255),nullable=False)
    course=db.Column(db.String(255),nullable=False)
    school=db.Column(db.String(255),nullable=False)
    payments=db.relationship('Payments',backref='payer',lazy=True)

    def __repr__(self):
        return '{}'.format(self.name)

class Payments(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(255),nullable=False)
    amount=db.Column(db.Integer(),nullable=False,default=0)
    date_paid=db.Column(db.DateTime(),default=datetime.utcnow)
    student_id=db.Column(db.Integer(),db.ForeignKey('student.id'))


admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Student,db.session))

admin.add_view(ModelView(Payments,db.session))

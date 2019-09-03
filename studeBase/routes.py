from studeBase import app,db
from flask import render_template,url_for,request,flash,redirect
from studeBase.models import User
from flask_bcrypt import Bcrypt

bcrypt=Bcrypt(app)



#the home page
@app.route('/')
def index():
    return render_template('index.html')

#the sign up page
@app.route('/signup',methods=['GET', 'POST'])
def SignUp():
    if request.method=='POST':
        full_names=request.form.get('full_names')
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        p=bcrypt.generate_password_hash(password)
        new_user=User(full_names=full_names,
        username=username,email= email,password=p)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully for %s, Please Log In! ' %username)
            return redirect('/signup')
        except:
            flash('Failed to create the account, There is a problem!')
            return redirect('/signup')

        
    return render_template('sign.html')
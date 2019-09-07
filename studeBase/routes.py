from studeBase import app,db
from flask import render_template,url_for,request,flash,redirect
from studeBase.models import User,Student
from flask_bcrypt import Bcrypt
from studeBase.forms import LoginForm
from flask_login import login_user,logout_user,login_required

bcrypt=Bcrypt(app)



#the home page
@app.route('/')
def index():
    return render_template('index.html',title='Home ')

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

        
    return render_template('sign.html',title='Create An Account')



@app.route('/login', methods=['GET','POST'])
def Login():
    form=LoginForm()
    email=request.form.get('email')
    password=request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password,password):
        login_user(user)
        return redirect('/')  
    
    return render_template('login.html',form=form,title='Login') 

@app.route('/logout')
def LogOutUser():
   logout_user()
   return redirect('/login')

@app.route('/users')
@login_required
def UserDetails():
    students=Student.query.all()
    return render_template('users.html',title='Users',students=students)
    

@app.route('/users/addstudent', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name=request.form.get('name')
        age=request.form.get('age')
        gender=request.form.get('gender')
        course=request.form.get('course')
        school=request.form.get('school')

        new_student=Student(name=name,age=age,gender=gender,course=course,school=school)
        db.session.add(new_student)
        db.session.commit()
        flash('Record Added Successfully')
        return redirect('/users')

    return render_template('users.html')
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def UpdateUser(id):
    student=Student.query.get_or_404(id)
    if request.method == 'POST':    
        student.name=request.form.get('name')
        student.age=request.form.get('age')
        student.gender=request.form.get('gender')
        student.course=request.form.get('course')
        student.school=request.form.get('school')
        db.session.commit()
        flash('Info Updated Successfully!!')
        return redirect('/users')
    

    return render_template('update.html',student=student)
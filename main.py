from flask import Flask, request, redirect, render_template
import html
import os




app = Flask(__name__)
app.config['DEBUG'] = True




@app.route("/signin",methods=['POST'])
def verify_signin():
    
    
    username   = request.form['username']
    password_1 = request.form['password_1']
    password_2 = request.form['password_2']
    email      = request.form['email']
    error_username   = ""
    error_password_1 = ""
    error_password_2 = ""
    error_email      = ""
    if username.strip() =='' or username.count(' ')>0 or len(username)>20 or len(username)<3:
        error_username ='That is not a valid username.'
        username = ''
    if password_1!=password_2:
        error_password_2 = 'Passwords do not match'
        password_2=''
    if password_1.strip() =='' or password_1.count(' ')>0 or len(password_1)>20 or len(password_1)<3:
        error_password_1 ='That is not a valid password.'
        password_1 = ''
        password_2 = ''
    if email!='':
        if email.isspace() == True:       
            
            error_email = 'Invalid Email'
            email=''
        if email.count('@')!=1 or email.count('.')!=1:

            error_email = 'Invalid Email'
            email=''
    
    if error_username=='' and error_password_1=='' and error_password_2=='' and error_email=='':
        
        return redirect('/welcome?username='+username)
    
    return render_template('signup_form.html',username=username,
    password_1=password_1,password_2=password_2,
    email=email, error_username=error_username,
    error_password_1=error_password_1,error_password_2=error_password_2,
    error_email=error_email)
    
@app.route("/welcome")
def welcome():
    username= request.args.get('username')
    return render_template('welcome.html',username=username)
@app.route("/")
def index():
    
    error = request.args.get("error")
    if error:
        error_esc = html.escape(error, quote=True)
        error_element = '<div class="error">' + error_esc + '</div>'
    else:
        error_element = ''

    return render_template('signup_form.html')
app.run()
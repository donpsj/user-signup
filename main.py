from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/validate-signup", methods=['GET','POST'])
def validate_signup():
    username = str(request.form['username'])
    password = str(request.form['password'])
    verify = str(request.form['verify'])
    email = request.form['email']
    username_error=''
    password_error=''
    verify_error=''
    email_error=''

    if len(username)<3:
        username_error = "The username must have at least 3 characters!" 
    elif len(username)>20:
        username_error = "The username cannot have more than 20 characters!" 
    elif " " in username:
         username_error = "The username contains a 'space' character!" 
         
    if len(password)<3:
        password_error = "The password must have at least 3 characters!"    
    elif len(password)>20:
        password_error = "The password cannot have more than 20 characters!" 
    elif " " in password:
        password_error = "The password contains a 'space' character!" 

    if verify not in password or verify=='':
        verify_error = "The passwords don't match!" 
        password_error = "The password must have at least 3 characters!"  
    if len(email)!=0 and len(email)<3:
        email_error="The email need to have at least 3 characters!"
    elif len(email)>=3:
        n1=0
        n2=0
        for char in email:
            if char == '@':
                n1 += 1
            if char == '.':
                n2 += 1
        if n1!=1 or n2!=1:
            email_error="This is an invalid email."
     
            
    if (not username_error and not password_error and not verify_error and not email_error):
        return render_template('welcome.html', username=username)
     
    return render_template('index.html', username=username, email=email, password=password, verify=verify, username_error=username_error, password_error=password_error, verify_error=verify_error,email_error=email_error)
     
@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html',  error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
        
 
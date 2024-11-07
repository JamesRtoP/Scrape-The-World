from .app import app

from markupsafe import escape
#see escape import in app.py
#calling {escape(something)} in https stops scripts from being entered as things

from flask import url_for 
#supposedly better

from flask import render_template
#templates in flask via jinja2


#Old index page
#@app.route("/")#this creates a new page on the website
#if you go to the url/ it will bring you to this page
#def index():
#    return "<p>IDK what an index page is</p>"


@app.route("/kyan")#this creates a new page on the website
#if you go to the url/ it will bring you to this page
def kyan():
    return "<h1> Kyan Is cool </h1>"

@app.route('/home')
def home():
    return '<h2> Welcome to Scrape The World </h2>'

#Flask templates through jinja2 #thus the templates folder in backend
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

from flask import request

@app.route("/user")
def userBasePage():
    login = "Login<br>"
    newAccount = "Create New Account<br>"
    return login + newAccount



def sh_name(name):
    oldName = name
    name = 'Sh'
    for x in range(len(oldName)):
        if x != 0:
            name += oldName[x]
    return name

#try not to end routes with a /, redirects to no slash, but adds complications
@app.route("/user/<username>")
def display_profile(username):
    Wassup = ("Wassup {}<br>")
    user = f"User {escape(username)}<br>"
    shuser = sh_name(str(username))+'<br>'
    

    return user + shuser + Wassup.format(username)


@app.route("/")#this creates a new page on the website
#if you go to the url/ it will bring you to this page
def indexPage():
    header = "<h1>Welcome To Scrape The World</h1>"
    learningGoals = "<p1>The learning goals for this project are to learn how Flask works, then the parellel website thing, then eventually to learn webscraping </p1>"
    link = '<p>Link to <a href="user">User</a> page</p>'#we got links now?
    
    
    
    return render_template("page-topper.html") +render_template('home.html')

@app.route('/gallery')
def gallery():
    return render_template("page-topper.html") + render_template('gallery.html') 


@app.route("/late")
def late():
    me = '<h1 style = "font-family: times new roman; color: cyan"> Asa is lame<br><hr></h1>'
    return render_template("page-topper.html") + me + render_template('late.html')
    #return '<h1>Hello World!<br></h1>' + '<h2>Hello World!<br></h2>' + '<h3>Hello World!<br></h3>' + '<h4>Hello World!<br></h4>' + '<h5>Hello World!<br></h5>' + '<h6>Hello World!<br></h6>'

@app.route("/default")
def default():
    return render_template("page-topper.html") + render_template('default_explained.html')


#"<img src = \"./static/South_Spirits.png\" alt = \"South Spirits Logo\" >"
#image

#everything below here is a little hellish

#You will notice that code which depends on a request object will suddenly break because there is no request object. 
#Whatever that means^
#does whatever that means below
with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


#print(url_for('home'))
#should work but doesn't

#HTTP Methods
#Get, retrieves data
#post, creates new data
#put, update/change data
#delete, remove data
#IE CRUD
#Create -post
#Read -get
#Update -put
#delete -delete

#route is ususally a post command

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        return do_the_login()
#    else:
#        return show_the_login_form()
    
#alternatively

#@app.get('/login')#trying to go the url calls this one
#def login_get():
#    return show_the_login_form()
#@app.post('/login')
#def login_post():
#    return do_the_login()

#static files through python
#url_for('static', filename = 'style.css')

#<em> </em> italisize
#<br> new line
from .app import app

from markupsafe import escape
#see escape import in app.py
#calling {escape(something)} in https stops scripts from being entered as things

from flask import url_for 
#supposedly better

from flask import render_template
#templates in flask via jinja2

@app.route("/")#this creates a new page on the website
#if you go to the url/ it will bring you to this page
def index():
    return "<p>IDK what an index page is</p>"


@app.route("/kyan")#this creates a new page on the website
#if you go to the url/ it will bring you to this page
def kyan():
    return "<h1> Kyan Is cool </h1>"

@app.route('/home')
def home():
    return '<h2> Welcome to Scrape The World </h2>'

#try not to end routes with a /, redirects to no slash, but adds complications
@app.route("/user/<username>")
def display_profile(username):
    return f"User {escape(username)}"


#Flask templates through jinja2 #thus the templates folder in backend
@app.route('/template/<t>')
def tem(t):
    return render_template('hello.html', person=t)

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


from flask import Flask #import flask class
#from markupsafe import escape: for safety purposes

app = Flask(__name__)#insantiate a flask class called app 
#the first argument is the name of the applications module or package, 
# #__name__ is a shortcut for the name of the file ie app
# Check if this script is being run directly

#since our application is named app, we can run
#by using flask run
#otherwise we'd have to use flask --app __appName__ run

#run using --debug for debugger
#debugger updates web when code changes
#and pops errors when errors arrise on webpage

if __name__ == '__main__':
    app.run(debug=True)



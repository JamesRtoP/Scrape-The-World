from flask import Flask
app = Flask(__name__)
# Check if this script is being run directly
if __name__ == '__main__':
    app.run(debug=True)



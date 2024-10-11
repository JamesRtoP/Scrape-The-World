from .app import app


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/kyan")
def kyan():
    return "<h1> Kyan Is cool </h1>"
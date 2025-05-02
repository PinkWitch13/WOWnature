from flask import Flask

app = Flask(__name__)

@app.route("/")
def wow_nature():
    return "<p>WOWnature!</p>"
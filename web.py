from flask import Flask
app = Flask(__name__)

@app.route('/')


def index():
    print("The application should work now.")
    
    return "Hello Wiktor"


index()

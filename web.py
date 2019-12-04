from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    print("Hello World!")
    print("The application should work now.")

index()

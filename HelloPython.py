import datetime
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    print("Hello World!")
    print("Hello Wiktor!")
    now = datetime.datetime.now()
    print("Current date and time is ")
    print(now.strftime("%A, %d-%m-%Y : %H:%M"))
    return "Hello!"
  
index()

from flask import Flask,request,json
from JiraBoard import *
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Flask Python Application'

@app.route('/webhook')
def webhookJira():
    JiraBoard()
    return "Retrieving issues is completed"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, escape

app = Flask(__name__)

def say_world():
    return "World"


@app.route('/')
def hello():
    name = say_world()
    return f'Hello, {escape(name)}!'

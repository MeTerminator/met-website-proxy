from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('https://www.met6.top:444/', code=301)

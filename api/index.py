from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return redirect('https://www.met6.top:444/')


@app.route('/tools/')
def tools():
    return redirect('https://tools.met6.top:444/')


@app.route('/shop/')
def shop():
    return redirect('https://shop.met6.top:444/')


@app.route('/necl/')
def necl():
    return redirect('https://www.brmc.top:444/necl/')


@app.route('/music/')
def music():
    return redirect('https://music.met6.top:444/')


@app.route('/music/v1/')
def music_v1():
    return redirect('https://music.met6.top:444/v1.php')


@app.route('/files/')
def files():
    return redirect('https://files.met6.top:444/')


@app.route('/card/')
def card():
    return redirect('https://card.met6.top:444/')


@app.route('/blog/')
def blog():
    return redirect('https://blog.met6.top:444/')


@app.route('/blcloud/')
def blcloud():
    return redirect('https://blcloud.met6.top:444/')

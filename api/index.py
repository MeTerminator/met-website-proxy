from flask import Flask, redirect, send_from_directory
import os

app = Flask(__name__)

"""
Links
"""


@app.route('/')
def home():
    return redirect('https://www.met6.top:444/')


@app.route('/tools/')
def tools():
    return redirect('https://tools.met6.top:444/')


@app.route('/shop/')
def shop():
    return redirect('https://shop.met6.top:444/')


@app.route('/mcsdf/')
def mcsdf():
    return redirect('https://mcsdf.met6.top:444/')


@app.route('/music/')
def music():
    return redirect('https://music.met6.top:444/')


@app.route('/music/v1/')
def music_v1():
    return redirect('https://music.met6.top:444/v1.php')


@app.route('/likemusic/')
def likemusic():
    return redirect('https://music.met6.top:444/likemusic/')


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


"""
Resources
"""
RES_DIR = os.path.join(os.path.dirname(__file__), "../res")


@app.route('/res/logo.png')
def res_logo():
    return send_from_directory(RES_DIR, 'logo.png')

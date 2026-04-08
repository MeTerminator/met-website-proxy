from flask import Flask, redirect, send_from_directory
import os

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return redirect("https://www.met6.top:444/")


@app.route("/")
def home():
    return redirect("https://www.met6.top:444/")


@app.route("/mcsdf/")
def mcsdf():
    return redirect("https://mcsdf.met6.top:444/")


@app.route("/blcloud/")
def blcloud():
    return redirect("https://blcloud.met6.top:444/")


@app.route("/blog/")
def blog():
    return redirect("https://blog.met6.top:444/")


@app.route("/music/")
def music():
    return redirect("https://music.met6.top:444/")


@app.route("/tools/")
def tools():
    return redirect("https://tools.met6.top:444/")


@app.route("/files/")
def files():
    return redirect("https://files.met6.top:444/")


@app.route("/shop/")
def shop():
    return redirect("https://shop.met6.top:444/")


@app.route("/card/")
def card():
    return redirect("https://card.met6.top:444/")


RES_DIR = os.path.join(os.path.dirname(__file__), "../res")
PAGES_DIR = os.path.join(os.path.dirname(__file__), "../pages")


@app.route("/p/bio")
def bio():
    return send_from_directory(PAGES_DIR, "bio.html")


@app.route("/res/<path:filename>")
def resources(filename):
    return send_from_directory(RES_DIR, filename)

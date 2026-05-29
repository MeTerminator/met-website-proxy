from flask import Flask, redirect, send_from_directory, request
import os
from urllib.parse import urlparse, urlunparse, urlencode

app = Flask(__name__)


def redirect_with_tracking(target_url):
    query = request.args.to_dict(flat=False)

    if request.referrer and "ref" not in query:
        query["ref"] = [request.referrer]

    url_parts = list(urlparse(target_url))

    if query:
        url_parts[4] = urlencode(query, doseq=True)

    final_url = urlunparse(url_parts)
    if isinstance(final_url, bytes):
        final_url = final_url.decode('utf-8')
    return redirect(final_url)


def should_redirect_to_target():
    host = request.host.lower()
    host_name = host.split(':')[0]
    return host_name in ['met6.top', 'www.met6.top']


@app.errorhandler(404)
def page_not_found(e):
    if should_redirect_to_target():
        return redirect_with_tracking("https://www.met6.top:444/")
    else:
        return send_from_directory(PAGES_DIR, "bio.html")


@app.route("/")
def home():
    if should_redirect_to_target():
        return redirect_with_tracking("https://www.met6.top:444/")
    else:
        return send_from_directory(PAGES_DIR, "bio.html")


@app.route("/mcsdf/")
def mcsdf():
    return redirect_with_tracking("https://mcsdf.met6.top:444/")


@app.route("/blcloud/")
def blcloud():
    return redirect_with_tracking("https://blcloud.met6.top:444/")


@app.route("/blog/")
def blog():
    return redirect_with_tracking("https://blog.met6.top:444/")


@app.route("/music/")
def music():
    return redirect_with_tracking("https://music.met6.top:444/")


@app.route("/tools/")
def tools():
    return redirect_with_tracking("https://tools.met6.top:444/")


@app.route("/files/")
def files():
    return redirect_with_tracking("https://files.met6.top:444/")


@app.route("/shop/")
def shop():
    return redirect_with_tracking("https://shop.met6.top:444/")


@app.route("/card/")
def card():
    return redirect_with_tracking("https://card.met6.top:444/")


RES_DIR = os.path.join(os.path.dirname(__file__), "../res")
PAGES_DIR = os.path.join(os.path.dirname(__file__), "../pages")


@app.route("/p/bio")
def bio():
    return send_from_directory(PAGES_DIR, "bio.html")


@app.route("/res/<path:filename>")
def resources(filename):
    return send_from_directory(RES_DIR, filename)

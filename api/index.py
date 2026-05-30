from flask import Flask, redirect, send_from_directory, request, g
import os
from urllib.parse import urlparse, urlunparse, urlencode

app = Flask(__name__)


@app.before_request
def capture_referrer():
    # Capture Referer header to track origin referrers externally
    referrer = request.headers.get("Referer")
    if referrer:
        host = request.host.lower()
        parsed_ref = urlparse(referrer)
        ref_host = parsed_ref.netloc.lower()

        # Exclude self-referrals within our domain and subdomains
        if ref_host and ref_host != host and not ref_host.endswith(".met6.top") and ref_host != "met6.top":
            g.new_referrer = referrer


@app.after_request
def set_referrer_cookie(response):
    if hasattr(g, 'new_referrer'):
        # Keep the cookie active for 30 days
        response.set_cookie(
            'from_referer', g.new_referrer, max_age=86400 * 30, path='/')
    return response


def redirect_with_tracking(target_url):
    query = request.args.to_dict(flat=False)

    if request.referrer and "ref" not in query:
        query["ref"] = [request.referrer]

    parsed = urlparse(target_url)

    if query:
        query_str = urlencode(query, doseq=True)
    else:
        query_str = parsed.query

    final_url = urlunparse((
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        parsed.params,
        query_str,
        parsed.fragment
    ))

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
def root():
    if should_redirect_to_target():
        return redirect_with_tracking("https://www.met6.top:444/")
    else:
        return send_from_directory(PAGES_DIR, "bio.html")


@app.route("/home/")
def home():
    target_url = "https://www.met6.top:444/"
    from_ref = request.cookies.get('from_referer')

    query = request.args.to_dict(flat=False)
    if from_ref and "from" not in query:
        query["from"] = [from_ref]

    parsed = urlparse(target_url)
    if query:
        query_str = urlencode(query, doseq=True)
    else:
        query_str = parsed.query

    final_url = urlunparse((
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        parsed.params,
        query_str,
        parsed.fragment
    ))

    return redirect(final_url)


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


@app.route("/p/contact")
def contact():
    return send_from_directory(PAGES_DIR, "contact.html")


@app.route("/p/sponsor")
def sponsor():
    return send_from_directory(PAGES_DIR, "sponsor.html")


@app.route("/res/<path:filename>")
def resources(filename):
    return send_from_directory(RES_DIR, filename)

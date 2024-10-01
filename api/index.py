from flask import Flask, redirect

app = Flask(__name__)

MET_WEBSITE_URL = 'https://www.met6.top:444/'

@app.route('/')
def home():
    return redirect(MET_WEBSITE_URL, code=301)

@app.errorhandler(404)
def not_found(e):
    return redirect(MET_WEBSITE_URL, code=301)

if __name__ == '__main__':
    app.run()

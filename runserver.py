import requests
from flask import Flask, render_template
app = Flask(__name__)

try:
    app.config.from_pyfile('watchlist.py')
    watchlist = app.config.get('WATCHLIST')
except (RuntimeError, IOError):
    watchlist = []


@app.route("/")
def watch():
    for element in watchlist:
        urls = element.get('urls')
        if urls:
            for url in urls:
                try:
                    r = requests.get(url.get('url', ''),
                                     headers=element.get('headers', ''))
                    url['status'] = r.status_code

                except AttributeError:
                    # looks like they passed a string instead of a dict
                    # Let's make this a dict
                    r = requests.get(url, headers=element.get('headers', ''))
                    index = urls.index(url)
                    urls[index] = {'url': url}
                    urls[index]['status'] = r.status_code
                    print urls[index]

    context = {
        'watchlist': watchlist,
    }
    return render_template('watch.html', **context)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host='0.0.0.0')

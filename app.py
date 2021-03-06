""" Main application entry point
"""

from flask import Flask, render_template, request

import api

app = Flask(__name__)


@app.route('/')
def index():
    """ Home page endpoint """
    return render_template('index.html')

@app.route('/searchHome', methods=['GET', 'POST'])
def search_home():
    """ Endpoint for search home form, calls api service """
    address = request.form['address']
    citystatezip = request.form['citystatezip']
    results = api.search_by_address(address, citystatezip)
    return render_template('results.html', results=results, count=len(results))


if __name__ == '__main__':
    app.run(debug=True)

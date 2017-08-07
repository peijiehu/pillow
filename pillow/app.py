from flask import Flask, render_template, request

import api

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/searchHome', methods=['GET', 'POST'])
def search_home():
    address = request.form['address'] # 2114 Bigelow Ave
    citystatezip = request.form['citystatezip'] # Seattle, WA
    json_data = api.search_by_address(address, citystatezip)
    return render_template('home.html', result=json_data)


if __name__ == '__main__':
    app.run(debug=True)

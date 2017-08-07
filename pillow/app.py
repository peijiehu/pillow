from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/searchHome', methods=['GET', 'POST'])
def search_home():
    print request.form['address'] # 2114 Bigelow Ave
    print request.form['citystatezip'] # Seattle, WA
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

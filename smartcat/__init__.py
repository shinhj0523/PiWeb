from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pages/<page>')
def pages(page):
    return render_template('/pages/'+page)
    
@app.route('/contents/<page>')
def contents(page):
    return render_template('/contents/'+page)

@app.route('/bbs/<page>')
def bbs(page):
    return render_template('/bbs/'+page)

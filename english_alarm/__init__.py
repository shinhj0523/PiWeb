# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "shinheejoon"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///english.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class WordBook(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    word = db.Column(db.String(100), nullable = False)
    memo = db.Column(db.String(200))

    def __init__(self, word, memo):
        self.word = word
        self.memo = memo

@app.route( '/find', methods=['POST'] )
def find():
    element = request.form['word']
    find_data = WordBook.query.filter(WordBook.word.contains(element))
    return render_template("list.html", words = find_data, aaaa = element)

@app.route('/')
def root():
    alldata = WordBook.query.all() # select * from wordbook;
    return render_template("list.html", words = alldata)
    
@app.route('/createdb')
def createdb():
    db.create_all()
    return "데이터베이스가 만들어졌습니다. 폴더에서 확인하세요."



@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        word = request.form['word']
        memo = request.form['memo']

        new_word = WordBook(word,memo)
        db.session.add(new_word)
        db.session.commit()

        return redirect(url_for('root'))

@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    del_word = WordBook.query.get(id)
    db.session.delete(del_word)
    db.session.commit()
    return redirect(url_for('root'))
    

@app.route('/update', methods = ['POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        wb = WordBook.query.get(id)
        wb.word = request.form['word']
        wb.memo = request.form['memo']
        db.session.commit()
        return redirect(url_for('root'))
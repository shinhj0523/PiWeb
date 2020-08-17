# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "shinheejune"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///english.db'
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class WordBook(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    word = db.Column(db.String(100), nullable=False)
    memo = db.Column(db.String(200))

    def __init__(self, word, memo):
        self.word = word
        self.memo = memo

@app.route('/')
def root():
    return "ddddd"

@app.route('/createdb')
def createdb():
    db.create_all()
    return "데이타베이스가 만들어졌습니다. 폴더에서 확인하세요."

@app.route('/list')
def list():
    alldata = WordBook.query.all() # select * from WordBook;
    return render_template("list.html", wordbook=alldata)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        word = request.form['word']
        memo = request.form['memo']
        
        new_word = WordBook(word,memo)
        db.session.add(new_word)
        db.session.commit()

        return redirect(url_for('list'))

@app.route('/delete/<id>', methods=['GET','POST'])        
def delete(id):
    del_word = WordBook.query.get(id)
    db.session.delete(del_word)
    db.session.commit()
    return redirect(url_for('list'))

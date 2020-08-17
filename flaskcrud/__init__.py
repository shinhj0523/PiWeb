# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db' #'mysql://root:''@localhost/crud'
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, username, email, phone):
        self.username = username
        self.email = email
        self.phone = phone

@app.route('/')
def index():
    # all_data = User.query.all()
    all_data = User.query.order_by(User.id.desc()).all()
    return render_template("index.html", employees = all_data)

@app.route('/insert', methods=['POST'])
def insertUser():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']

        inputUser = User(username,email,phone)
        db.session.add(inputUser)
        db.session.commit()

        flash(u"직원이 성공적으로 등록되었습니다.","success") # 한글은 앞에 u넣기

        return redirect(url_for('index'))

@app.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        inputUser = User.query.get(request.form.get('id'))
        inputUser.username = request.form['username']
        inputUser.email = request.form['email']
        inputUser.phone = request.form['phone']

        db.session.commit()

        flash(u"직원이 성공적으로 수정되었습니다.","success")
        flash(u"수고하셨습니다.","success")

        return redirect(url_for('index'))

@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    deleteUser = User.query.get(id)
    db.session.delete(deleteUser)
    db.session.commit()
    flash(u"직원이 성공적으로 삭제되었습니다.","success")
    return redirect(url_for('index'))
    
@app.route('/test')
def test():
    return "한글테스트"

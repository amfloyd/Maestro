from flask import Flask, abort, jsonify, request, render_template,send_from_directory,url_for, redirect
from sklearn.externals import joblib
#import json
import db as dbio
import logging
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['pwd']
        check=dbio.insertUser(username, password)
        return render_template('index.html',check=check)

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        passwd = request.form['password']
        user,pwd = dbio.retrieveUsers(user,passwd)
        if user == user and passwd == pwd:
            return redirect('home')
        else:
            return render_template('index.html', wrong=True)

@app.route('/home')
def home():
    mostpop = joblib.load('mostpop.pkl')
    return render_template('recs.html',correct=True,songlist=mostpop)
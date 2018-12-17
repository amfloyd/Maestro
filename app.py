#!/usr/bin/python3.7

from flask import Flask, abort, jsonify, request, render_template,send_from_directory,url_for, redirect
from sklearn.externals import joblib
#import json
import db as dbio
import youtube as yt
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
app = Flask(__name__)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#heroku = Heroku(app)
#db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST' or request.method == 'GET':
        username = request.form['uname']
        password = request.form['pwd']
        #check=dbio.insertUser(username, password)
        return render_template('index.html',check=True)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST' or request.method == 'GET':
        user = request.form['username']
        passwd = request.form['password']
        # user,pwd = dbio.retrieveUsers(user,passwd)
        # if user == user and passwd == pwd:
        #     return redirect('home')
        # else:
        #     return render_template('index.html', wrong=True)
        return redirect('home')

@app.route('/song', methods=['GET','POST'])
def getinfo():
    if request.method == 'POST' or request.method == 'GET':
        song = request.form['song']
        title, release, artist_name, year = dbio.getsonginfo(song)
        infotup=(title, release, artist_name, year)
        if not infotup[0]==" ":
            # print (infotup)
            return render_template('song.html',title=title,release=release,artist=artist_name,year=year,empty=False)
        else:
            # print ("got nothing")
            return render_template('song.html',empty=True)

@app.route('/youtube',methods=['GET','POST'])
def showvideos():
    if request.method=='POST' or request.method=='GET':
        # artist=request.form['artist']
        # dic=yt.youtube_search(artist)
        return render_template('ytsearch.html')

@app.route('/display',methods=['POST','GET'])
def display():
    if request.method=='POST' or request.method=='GET':
        # artist=request.form['artist']
        # dic=yt.youtube_search(artist)
        return '<div class="item"> <h2>{{title}}</h2> <iframe class="video w100" width="640" height="360" src="//www.youtube.com/embed/{{videoid}}" frameborder="0" allowfullscreen></iframe> </div>'

@app.route('/home')
def home():
    mostpop = joblib.load('mostpop.pkl')
    return render_template('recs.html',correct=True,songlist=mostpop)

@app.route('/musix')
def musix():
    return render_template('musix.html')

if __name__ == '__main__':
    #app.run(ssl_context=('cert.pem', 'key.pem'))
    app.run()
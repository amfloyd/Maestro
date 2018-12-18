#!/usr/bin/python3.7

from flask import Flask, abort, jsonify, request, render_template,send_from_directory,url_for, redirect, make_response
from sklearn.externals import joblib
#import json
#import db as dbio



import os

import tweepy


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

import usersdb


consumer_key="REf4WjS1J9xKEMcjPKGdo1MJT"
consumer_secret="LmbacJYnMnaDHfGCjSf6AlaLZnOv8cUKUYBhngbRMSSsxKc0ec"
access_token="175046594-rlc2LODoFs9ZBV4XQvY0iDo8syP5pRGKBgI7cqrS"
access_secret="n5QPwUhny5BNWBEtwgnaHHo1YHFrxyiVfLKUT6AMywAg7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# search=api.search(q="music",rpp=10)
# print (search)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST' or request.method == 'GET':
        firstname = request.form['fname']
        lastname = request.form['lname']
        uname = request.form['uname']
        emailid = request.form['emailid']
        password = request.form['pwd']
        check="Valid"
        info = usersdb.user(first_name=firstname,last_name=lastname,emailid=emailid,password=password,uname=uname)
        db.session.add(info)
        db.session.commit()

        resp = make_response(redirect(url_for('home',_scheme="https",_external=True)))
        resp.set_cookie('first', firstname)
        resp.set_cookie('last', lastname)
        resp.set_cookie('sig',check)

        return resp

        #return redirect('home',fname=firstname,lname=lastname,db=True)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST' or request.method == 'GET':
        username = request.form['username']
        passwd = request.form['password']
        exists = db.session.query(db.exists().where(usersdb.user.uname == username and usersdb.user.password==passwd)).scalar()
        if exists:
            f=db.session.query(usersdb.user.first_name.label('fn'),usersdb.user.last_name.label('ln')).filter(usersdb.user.uname==username, usersdb.user.password==passwd).first()
            # print (f.user)
            resp = make_response(redirect(url_for('home',_scheme="https",_external=True)))
            check="Valid"
            resp.set_cookie('sig', check)
            resp.set_cookie('first', f.fn)
            resp.set_cookie('last', f.ln)
            return resp
        else:
            return render_template("index.html",exists=exists)

@app.route('/song', methods=['GET','POST'])
def getinfo():
    # if request.method == 'POST' or request.method == 'GET':
    #     song = request.form['song']
    #     #title, release, artist_name, year = dbio.getsonginfo(song)
    #     infotup=(title, release, artist_name, year)
    #     if not infotup[0]==" ":
    #         # print (infotup)
    #         return render_template('song.html',title=title,release=release,artist=artist_name,year=year,empty=False)
    #     else:
    #         # print ("got nothing")
    #         return render_template('song.html',empty=True)
    pass

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
    firstname = request.cookies.get('first')
    lastname = request.cookies.get('last')
    check= request.cookies.get('sig')
    mostpop = joblib.load('mostpop.pkl')
    return render_template('recs.html',correct=True,songlist=mostpop,first=firstname,last=lastname,sig=check)

@app.route('/musix')
def musix():
    return render_template('musix.html')

if __name__ == '__main__':
    app.run()

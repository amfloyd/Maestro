import _sqlite3 as sql
from flask import g

def insertUser(uname,pwd):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (uname,pwd))
    con.commit()
    con.close()
    return True

def retrieveUsers(username,password):
    con = sql.connect("database.db")
    cur = con.cursor()
    if cur.execute("SELECT username, password FROM users WHERE username=? AND password=?",(username,password)).fetchone():
        user,password= cur.execute("SELECT username, password FROM users WHERE username=? AND password=?",(username,password)).fetchone()
    else:
        user,password=" "," "
    con.close()
    return user,password

#create plays relation

def getsonginfo(song):
    con=sql.connect("database.db")
    cur=con.cursor()
    if cur.execute("SELECT title,release,artist_name,year FROM songinfo WHERE title=? ",(song,)).fetchone():
        title,release,artist_name,year= cur.execute("SELECT title,release,artist_name,year FROM songinfo WHERE title=? ",(song,)).fetchone()
    else:
        title, release, artist_name, year=" "," "," "," "

    return title,release,artist_name,year



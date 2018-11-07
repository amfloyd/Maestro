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
    user,password= cur.execute("SELECT username, password FROM users WHERE username=? AND password=?",(username,password)).fetchone()
    con.close()
    return user,password



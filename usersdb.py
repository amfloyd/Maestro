
from app import db


class user(db.Model):
    __tablename__ = 'users'

    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    emailid = db.Column(db.String())
    password = db.Column(db.String())
    uname=db.Column(db.String(), primary_key=True)

    def __init__(self, first_name, last_name, emailid , password,uname):
        self.first_name = first_name
        self.last_name = last_name
        self.emailid = emailid
        self.password = password
        self.uname = uname

    def __repr__(self):
        return "<user(firstname='%s', lastname='%s',emailid='%s',password='%s', uname='%s')>" % (self.first_name, self.last_name, self.emailid,self.password,self.uname)

    def serialize(self):
        return {
            'first_name': self.fname,
            'last_name': self.lname,
            'emailid': self.emailid,
            'password': self.password,
            'uname': self.uname
        }


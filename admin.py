# -*- coding: utf8 -*-

from sys import argv
from app import models
from flask import Flask
cccApp = Flask(__name__)
cccApp.config.from_object('config')

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(cccApp)


def addUser(*args):
    """adding an user in the database: (email, passwd, firstname, timezone)"""
    #timezone = 'fr_FR'
    user = models.User(email=email, password=passwd, firstname=firstname, timezone=timezone)
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    email = argv[1]
    passwd = argv[2]
    try:
        firstname = argv[3]
    except:
        firstname = None
    try:
        timezone = argv[4]
    except:
        timezone = None

    addUser(email, passwd, firstname, timezone)
# -*- coding: utf-8 -*-
"""
    User service example
"""
from pydbwrapper.database import Database
from bottle import get, put

@get("/users/<id>")
def load(id):
    """ Load user from id """
    with Database() as db:
        user = db.execute("select id, name from users where id = %(id)s", {"id":id}).fetchone()
        return {"content": user}


@get("/users")
def query():
    """ Load all users """
    with Database() as db:
        users = db.execute("select id, name from users").fetchall()
        return {"content": users}


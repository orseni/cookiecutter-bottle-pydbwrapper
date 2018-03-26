# -*- coding: utf-8 -*-
"""
    User service example
"""

from bottle import get, post, request, put, delete
from pydbwrapper.database import Database, Page
from schemas import SchemaType, UserSchema


@put('/users', schemas={SchemaType.BODY: UserSchema()})
def insert():
    with Database() as db:
        db.insert("users").setall(request.json).execute()


@post('/users/<id>')
def update(id):
    user = request.json
    with Database() as db:
        db.update("users").setall(user).where("id", id).execute()


@get('/users/<id>')
def load(id):
    with Database() as db:
        user = db.execute('select id, name from users where id = %(id)s', {"id": id}).fetchone()
        return user


@get('/users')
def all():
    with Database() as db:
        pagenumber = request.GET.get("pagenumber")
        pagesize = request.GET.get("pagesize")
        return db.select("users").paging(pagenumber, pagesize)


@delete('/users/<id>')
def delete(id):
    with Database() as db:
        db.delete("users").where("id", id).execute()


import sqlite3
from flask import  g

DATABASE='data/database.db'

def connect_db():
    return sqlite3.connect(DATABASE)
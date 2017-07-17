from flask import render_template, request, current_app, redirect,\
    url_for, flash
from  . import  main

@main.route('/')
def index():
    #BlogView.add_view(db)

    return render_template('index.html')
    #return render_template('index.html')
from  flask import Blueprint
from os import path

main=Blueprint('main',__name__,template_folder='../../templates')
#path.join(path.pardir, 'templates', 'main')
#main=Blueprint('main',__name__,template_folder=path.join(path.pardir, 'templates'))

from  . import  views
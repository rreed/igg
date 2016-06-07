import requests

from flask import render_template, current_app
from bs4 import BeautifulSoup

from ...data.db import db
from ...data.models import Game

def show():
    tumblr_xml = requests.get('http://blog.iggmarathon.com/api/read').text

    soup = BeautifulSoup(tumblr_xml)
    posts = soup.tumblr.posts.find_all('post')

    return render_template('index.tmpl', posts=posts)

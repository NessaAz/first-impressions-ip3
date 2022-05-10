from flask import render_template, redirect, url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment,Upvote,Downvote
from .forms import UpdateProfile,PitchForm,CommentForm
# from .. import db


@main.route('/')
def index():
    allp = Pitch.query.all()
    jobs = Pitch.query.filter_by(category = 'Interviews').all() 
    event = Pitch.query.filter_by(category = 'Networking').all()
    dates = Pitch.query.filter_by(category = 'Dates').all()
    return render_template('index.html', allp = allp,jobs = jobs, event = event,dates= dates)



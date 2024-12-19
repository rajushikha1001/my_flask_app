from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import User

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@bp.route('/add', methods=['POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.index'))

from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import db, User, Post
from datetime import datetime

users_bp = Blueprint('users', __name__, url_prefix='/users')
posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

@users_bp.route('/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('show.html', user=user)

@users_bp.route('/<int:user_id>/posts/new', methods=['GET'])
def show_add_post_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('new_post.html', user=user)

@users_bp.route('/<int:user_id>/posts/new', methods=['POST'])
def add_post(user_id):
    user = User.query.get_or_404(user_id)
    title = request.form['title']
    content = request.form['content']

    if not title or not content:
        flash('Title and content are required.', 'error')
        return redirect(url_for('users.show_add_post_form', user_id=user_id))

    new_post = Post(title=title, content=content, created_at=datetime.utcnow(), user_id=user.id)
    db.session.add(new_post)
    db.session.commit()
    flash('Post added successfully!', 'success')

    return redirect(url_for('users.show_user', user_id=user_id))

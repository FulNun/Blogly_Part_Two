from flask import Flask, redirect, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Post
from users_routes import users_bp
from posts_routes import posts_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///blogly"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ihaveasecret'

db.init_app(app)

# Register blueprints
app.register_blueprint(users_bp)
app.register_blueprint(posts_bp)

@app.route('/')
def index():
    """Homepage showing recent posts."""
    recent_posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return render_template('index.html', recent_posts=recent_posts)

if __name__ == '__main__':
    app.run(debug=True)

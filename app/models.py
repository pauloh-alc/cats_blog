from app import db
from flask_login import UserMixin
from app import login_manager
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from abc import abstractmethod


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), nullable=False, index=True, unique=True)
    password = db.Column(db.String(200), nullable=False)
    cat_name = db.Column(db.String(50), nullable=False)
    cat_sex = db.Column(db.String(1), nullable=False)
    posts = relationship('Post', backref='author', cascade='all, delete-orphan')


    def get_id(self):
        return self.id


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

    @abstractmethod
    def format_content(self):
        pass


class TextPost(Post):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.format_content()

    def format_content(self):
        self.title = self.title.lower()
        max_length = 300
        if len(self.body) > max_length:
            self.body = self.body[:max_length] + "..."


class ImagePost(Post):
    path_image = db.Column(db.String(512))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.format_content()

    def format_content(self):
        max_length = 100
        self.title = self.title.upper()
        if len(self.body) > max_length:
            self.body = self.body[:max_length] + "..."
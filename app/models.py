from . import db
from datetime import datetime

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comments = db.relationship('BlogComments',backref = 'comments',lazy="dynamic")

    def __repr__(self):
        return 'Blog post ' + str(self.id)

class BlogComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog_post.id'))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    

    def __repr__(self):
        return f'User {self.username}'
    


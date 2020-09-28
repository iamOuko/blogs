from flask import render_template,redirect,request,url_for
from . import blog
from .forms import BlogForm, CommentForm, SubscribeForm
from .. import db
from ..models import BlogPost, BlogComments, User
from ..email import mail_message
import urllib
import json

@blog.route('/')
def index():
    search_quotes_url = "http://quotes.stormconsultancy.co.uk/random.json"

    with urllib.request.urlopen(search_quotes_url) as url:
        search_quotes_data = url.read()
        search_quotes_response = json.loads(search_quotes_data)
    
    blogs = BlogPost.query.all()
    return render_template('index.html', blogs=blogs, random_quote=search_quotes_response)

@blog.route('/subscribe', methods=('GET', 'POST'))
def user():
    form = SubscribeForm()

    if form.validate_on_submit():
        user = User(email = form.email.data, name = form.name.data)
        db.session.add(user)
        db.session.commit()

    return render_template('subscribe.html', form=form)



@blog.route('/addblog', methods=('GET', 'POST'))
def blog_admin():

    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        author = form.author.data

        blog=BlogPost(title=title, content=content, author=author)

        db.session.add(blog)
        db.session.commit()

        return redirect('/viewblogs')

    return render_template('addform.html', form=form)

@blog.route('/viewblogs', methods=('GET', 'POST'))
def blog_view():
    blogs = BlogPost.query.all()
    return render_template('viewblogs.html', blogs=blogs)

@blog.route('/deleteblog/<int:id>', methods=('POST',))
def blog_delete(id):
    post = BlogPost.query.filter(BlogPost.id==id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect('/viewblogs')

@blog.route('/editblogs/<int:id>', methods=('GET', 'POST'))
def blog_edit(id):

    form = BlogForm()
    post = BlogPost.query.filter(BlogPost.id==id).first()
    
    if form.validate_on_submit():    
        post.title = form.title.data
        post.content = form.content.data
        post.author = form.author.data

        db.session.commit()

        return redirect('/viewblogs')

    form.title.data = post.title
    form.content.data = post.content
    form.author.data = post.author
    
    return render_template('addform.html', form=form)

@blog.route('/comment/<int:id>', methods=('GET', 'POST'))
def blog_comment(id):

    blog = BlogPost.query.filter(BlogPost.id==id).first()
    comments = BlogComments.query.filter(BlogComments.blog_id==id).all()

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data

        comment=BlogComments(comment=comment, blog_id=id)

        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('blog.blog_comment', id=id))

    return render_template('postcomments.html', form=form, blog=blog, comments=comments)


@blog.route('/manage/<int:id>', methods=('GET', 'POST'))
def manage_comment(id):
    blog = BlogPost.query.filter(BlogPost.id==id).first()
    comments = BlogComments.query.filter(BlogComments.blog_id==id).all()

    return render_template('managecomments.html', blog=blog, comments=comments)


@blog.route('/deletecomment/<int:blog_id>/<int:comment_id>',  methods=('POST',))
def comment_delete(blog_id, comment_id):
    comment = BlogComments.query.filter(BlogComments.id==comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('blog.manage_comment', id=blog_id))

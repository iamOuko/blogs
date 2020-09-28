from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length


class BlogForm(FlaskForm):
    """Blogs form."""

    title = StringField('Blog Title', 
                validators=[DataRequired(message=('Blog title required'))])
    content = TextField('Blog Content', 
                validators=[DataRequired(message=('Blog content Required'))])
    author = StringField('Blog Author', 
                validators=[DataRequired(message=('Blog author required'))])
    submit = SubmitField('Add Blog')

class CommentForm(FlaskForm):
    comment = TextField('Comment', 
                validators=[DataRequired(message=('Comment Required'))])
    submit = SubmitField('Add Comment')

class SubscribeForm(FlaskForm):
    name = StringField('Enter your name',validators = [DataRequired()])
    submit = SubmitField('Subscribe')


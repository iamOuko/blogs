from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired,Email, Length
from ..models import User


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
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    name = StringField('Enter your name',validators = [DataRequired()])
    submit = SubmitField('Subscribe')


    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')


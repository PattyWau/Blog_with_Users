from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField("Login")


class CommentForm(FlaskForm):
    comment = StringField("Comments:", [DataRequired()])
    submit = SubmitField("Submit")


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterFormForUser(FlaskForm):
    file = FileField('choose your logo')
    name = StringField("name you wish others to call you", validators=[DataRequired()])
    email = StringField("enter your email address", validators=[DataRequired()])
    password = PasswordField("create your password here", validators=[DataRequired()])
    password_confirm = PasswordField("re-enter your password here", validators=[DataRequired()])
    submit = SubmitField("Register")


class LoginFormForUser(FlaskForm):
    email = StringField("enter your email address", validators=[DataRequired()])
    password = PasswordField("create your password here", validators=[DataRequired()])
    submit = SubmitField("Log in")


class CommentForm(FlaskForm):
    body = StringField("add a public comment", validators=[DataRequired()])


class ProfileForm(FlaskForm):
    old_password = PasswordField("enter your old password here", validators=[DataRequired()])
    password = PasswordField("enter your new password here", validators=[DataRequired()])
    password_confirm = PasswordField("re-enter your new password", validators=[DataRequired()])

class UploadLogo(FlaskForm):
    file = FileField('choose your logo')

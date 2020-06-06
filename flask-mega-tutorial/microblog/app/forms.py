from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FieldList
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user != None:
            raise ValidationError('Please use a different username')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user != None:
            raise ValidationError('Please use a different email')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, orig_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.orig_username = orig_username

    def validate_username(self, username):
        if username == self.orig_username:
            return
        user = User.query.filter_by(username = username.data).first()
        if user != None:
            raise ValidationError('Please use a different username')

class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')

class CreatePoll(FlaskForm):
    title = TextAreaField('Title', validators=[DataRequired(), Length(min=1, max=100)])
    description = TextAreaField('Description')
    choice1 = StringField('Choice1', validators=[DataRequired()])
    choice2 = StringField('Choice2', validators=[DataRequired()])
    choice3 = StringField('Choice3', validators=[DataRequired()])
    submit = SubmitField('Submit')


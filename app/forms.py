from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    user_name = StringField('Username*', validators=[DataRequired()])
    password = PasswordField('Password*', validators=[DataRequired()], id="pass")
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
    user_name = StringField('Username*', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Password*', validators=[DataRequired(), Length(min=6)], id="pass")
    cat_name = StringField('Cat Name*', validators=[DataRequired()])
    cat_sex = RadioField('Cat Sex*', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Register')


class UpdateUserForm(FlaskForm):
    user_name = StringField('Username*', validators=[DataRequired(), Length(min=4, max=50)])
    cat_name = StringField('Cat Name*', validators=[DataRequired()])
    cat_sex = RadioField('Cat Sex*', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Register')


class PostForm(FlaskForm):
    title = StringField('Title*', validators=[DataRequired()])
    body = TextAreaField('Body*', validators=[DataRequired()])
    path_image = StringField('path')
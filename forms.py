from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
                                     
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Log In')


class SearchForm(FlaskForm):
    city = StringField('City',
                       validators=[DataRequired()])

    submit = SubmitField('Submit')


class HotelForm(FlaskForm):
    check_in_date = StringField('Check In Date (XXXX-XX-XX)',
                              validators=[DataRequired()])
                            
    check_out_date = StringField('Check Out Date (XXXX-XX-XX)',
                               validators=[DataRequired()])
                                
    submit = SubmitField('Submit')
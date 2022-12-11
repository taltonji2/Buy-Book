from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (DataRequired, Email, EqualTo, Length, Optional)

class SignUpForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired()]
    )
    password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )
    passwordconfirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )

    submit = SubmitField('Sign Up')

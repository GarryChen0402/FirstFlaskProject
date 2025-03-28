from wtforms import StringField, PasswordField, IntegerField, widgets, SelectField, SubmitField
from flask_wtf import  FlaskForm
from wtforms.validators import Length, DataRequired, NumberRange, EqualTo, length


class UserInfoForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(message='Username can\'t be null'), Length(6, 30, message='The length of username should be >= 6 and <= 30')]
                           , render_kw={'class':'form-control', 'placeholder':'Please input your Username'})
    password = PasswordField(label='Password', validators=[DataRequired(message='Password can\'t be null'), Length(6, 30, message='The length of password should be >= 6 and <= 30')]
                             , render_kw={'class':'form-control', 'placeholder':'Please input your Password'})
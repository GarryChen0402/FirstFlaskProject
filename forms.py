from cProfile import label

from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, IntegerField, widgets, SelectField, SubmitField
from flask_wtf import  FlaskForm
from wtforms.validators import Length, DataRequired, NumberRange, EqualTo


class UserInfoForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(message='Username can\'t be null'), Length(6, 30, message='The length of username should be >= 6 and <= 30')]
                           , render_kw={'class':'form-control', 'placeholder':'Please input your Username'})
    password = PasswordField(label='Password', validators=[DataRequired(message='Password can\'t be null'), Length(6, 30, message='The length of password should be >= 6 and <= 30')]
                             , render_kw={'class':'form-control', 'placeholder':'Please input your Password'})
    password_repeat = StringField(label='Please repeat your password.', validators=[DataRequired(message='Password can\'t be null'), Length(6, 30, message='The length of password should be >= 6 and <= 30')
                            , EqualTo('password', message='Repeat password must equal to the password above.')], widget=widgets.PasswordInput())
    age = IntegerField(label='Age', default=1, validators=[NumberRange(1, 120, message='The age should be >= 1 and <= 120')],
                            render_kw={'class' : 'form-control'})
    mobile = StringField(label='Mobile phone number', validators=[DataRequired(message='Mobile phone number can\'t be null. '), Length(11, 11, message='The length of phone number must be 11')],
                            render_kw={'class' : 'form-control', 'placeholder' : 'Please input your mobile phone number.'} )
    status = [('-1', 'Please input'), ('0', 'Common'), ('1', 'Error')]
    user_status = SelectField(label='User Status', validators=[DataRequired(message='User Status can\'t be null')], choices=status)
    submit = SubmitField(label='Submit')

class UploadFileForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(message='Username can\'t be null'), Length(6, 30, message='The length of username should be >= 6 and <= 30')]
                           , render_kw={'class':'form-control', 'placeholder':'Please input your Username'})

    file = FileField(label='User icon', validators=[FileRequired(message='User icon can\'t be null'), FileAllowed(['jpg', 'png'])], render_kw={'class':'form-control'})
    submit = SubmitField(label='Submit')



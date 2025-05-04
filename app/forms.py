from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=128)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Save')

class ExpenseForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired(), Length(max=200)])
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Save')

class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')

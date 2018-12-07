from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class MainForm(FlaskForm):
    content = TextAreaField('Kodunuzu buraya yazın', validators=[DataRequired()])
    submit = SubmitField('Renklendir!')

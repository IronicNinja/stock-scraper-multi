from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Length

class InputForm(FlaskForm):
    stocks = StringField('Input Stock Names', validators=[DataRequired(), Length(max=500)])
    date_start = DateField('Date Start', validators=[DataRequired()])
    date_end = DateField('Date End', validators=[DataRequired()])
    submit = SubmitField('Submit')
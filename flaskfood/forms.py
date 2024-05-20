from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange



    
class inputData(FlaskForm):
  food = StringField('Food',validators=[DataRequired(),Length(min=1,max=30)])
  calories = StringField('Calories',validators=[DataRequired(), NumberRange(min=1,max=10000)])
  submit = SubmitField('Submit')










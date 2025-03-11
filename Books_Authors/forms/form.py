from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FloatField, DateField
from wtforms.validators import DataRequired, Length, ValidationError
from datetime import datetime

class AuthorForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(), 
        Length(min=1, max=100, message="Author name must be between 1 and 100 characters.")
    ])
    
    submit = SubmitField('Submit')
class BookForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(), 
        Length(min=1, max=100, message="Title must be between 1 and 100 characters.")
    ])
    
    author = SelectField('Author', coerce=int)
    
    publish_date = DateField('Publish Date', format='%Y-%m-%d', validators=[DataRequired()])
    create_date = DateField('Create Date', format='%Y-%m-%d', validators=[DataRequired()])
    
    price = FloatField('Price', validators=[DataRequired()])
    
    submit = SubmitField('Submit')

    def validate_create_date(self, field):
        if self.publish_date.data and field.data >= self.publish_date.data:
            raise ValidationError("Create Date must be before Publish Date.")


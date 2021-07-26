from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from wtforms import StringField, SubmitField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired, ValidationError



class BasicForm(FlaskForm):
    car_Make = StringField('Car Make', validators=[DataRequired()])
    car_Model = StringField('Car Model', validators=[DataRequired()])
    submit = SubmitField('Add Car')

class RentForm(FlaskForm):
    car_Make = StringField('Car Make', validators=[DataRequired()])
    car_Model = StringField('Car Model', validators=[DataRequired()])
    submit = SubmitField('Add Car')
    car_year = IntegerField('Year of Manufacture')
    car_description = StringField('Car Description')
    order_car = IntegerField ('Order Number')
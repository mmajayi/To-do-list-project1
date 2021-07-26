from flask import Flask, render_template, request
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField
from application import app
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')







# from application import app 

# if __name__ == "__main__": 
#     app.run(debug=True, host='0.0.0.0')

# from flask import Flask


# app = Flask(__name__)

# @app.route('/')
# def Home():
#     return "Mike's Car Rentals"

# if __name__=='__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField
from application import app
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy

# from flask_wtf import SubmitField, StringField



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

# @app.route('/', methods=['GET', 'POST'])
# @app.route('/rent', methods=['GET', 'POST'])
# def register():
#     error = ""
#     form = BasicForm

#     if request.method == 'POST':
#         car_make = form.car_make.data
#         car_model = form.car_model.data

#         if len(car_make) == 0 or len(car_model) == 0:
#             error = "Please select an instock car make and model"
#         else:
#             return "Thank you!"
#     return render_template('home.html', form=form, message=error)






# from application.forms import TaskForm
# from flask import redirect, url_for, render_template
# from flask_wtf import form
# from . import app, db
# from .forms import TaskForm
# from .models import Task


# @app.route("/")
# def home():
#     tasks = Task.query.all()

#     return render_template('home.html', tasks=tasks)

#     # result = ""
#     # for task in tasks:
#     #     result += f"{task.id:0>3} | {task.description} | {task.completed}\<br>"

#     return result

# @app.route("/create", methods=["GET", "POST"])
# def create():
#     form = TaskForm()

#     if request.method =="POST":
#         new_task = Task(description=form.description.data)
#         db.session.add(new_task)
#         db.session.commit()

#         return redirect(url_for("home"))

#     else:
#         return render_template("create.html", form=form)

# @app.route("/update/<int:id>", methods=["GET", "POST"])
# def update(id, description):
#     task = Task.query.get(id)
#     form = TaskForm()

#     if request.method =="POST":
#         task.description = form.description.data
#         db.session.add(task)
#         db.session.commit()

#         return redirect(url_for("home"))

#     else:
#         return render_template("create.html", form=form)

# # @app.route("/update/<int:id><desctiption>")
# # def update(id, description):
# #     task = Task.query.get(id)
# #     task.description = description
# #     db.session.add(task)
# #     db.session.commit()

# #     return redirect(url_for("home"))

# @app.route("/delete/<int:id>")
# def delete(id):
#     task = Task.query.get(id)
#     db.session.delete(task)
#     db.session.commit()

#     return redirect(url_for("home"))

# @app.route("/complete/<int:id>")
# def complete(id):
#     task = Task.query.get(id)
#     task.completed = True
#     db.session.add(task)
#     db.session.commit()

#     return redirect(url_for("home"))

# @app.route("/incomplete/<int:id>")
# def incomplete(id):
#     task = Task.query.get(id)
#     task.completed = False
#     db.session.add(task)
#     db.session.commit()

#     return redirect(url_for("home"))

# @app.route('/home')
# def home():
#     return 'Hello, World!'


from application import app, db 
from application.models import Car
from application.forms import BasicForm, RentForm
from flask import render_template, redirect, url_for, request

# @app.route('/', methods=['GET', 'POST']) 
# def home():
#     form=BasicForm()
#     car = Car.query.all()
#     return render_template('home.html', title='New cars', car=car, form=form)
    
# @app.route('/', methods=['GET', 'POST']) 
# def home():
#     form=RentForm.query.all()
#     car = Car.query.all()
#     car_make = car_make.query.all()
#     car_model = car_model.query.all()
#     car_year = car_year.query.all()
#     car_description = car_description.query.all
#     order_car = order_car.filter_by(desc).all 
    
    # return render_template('home.html', title='New cars', car=car, form=form, car_make=car_make, car_model=car_model, year=year, description=description)

@app.route('/', methods=['GET', 'POST']) 
def home():
    car=Car.query.all()

    return render_template("home.html", car=car)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = RentForm()
    if request.method == "POST":
        new_car = Car(car_Make=form.car_Make.data, car_Model=form.car_Model.data, car_year=form.car_year.data, car_description=form.car_description.data, order_car=form.order_car.data)

        db.session.add(new_car)
        db.session.commit()

        return "Added a new car to database"
    else:
        return render_template("create.html", form=form)

    # result = ""
    # for new_cars in Car:
    #     result += f"{new_cars.car_Make} | {new_cars.car_Model} | {new_cars.car_year} | {new_cars.car_description} {new_cars.order_car}<br>"

    

# @app.route('/read')
# def read():
#     all_cars = Car.query.all()
#     car_string = ""
#     for car in all_cars:
#         car_string += "<br>"+ car.name

#     return car_string

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    car_update = Car.query.get(id)
    form = RentForm()
    if request.method == 'POST':
        # if len(form.car_Make.data):
        car_update.car_Make = form.car_Make.data
        # if len(form.car_Model.data):
        car_update.car_Model = form.car_Model.data
        # if len(form.submit.data):
        #     car_update.submit = form.submit.data
        # if len(form.car_year.data):
        car_update.car_year = form.car_year.data
        # if len(form.car_description.data):
        car_update.car_description = form.car_description.data
        # db.session.add(car_update)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("create.html", form=form)

    

@app.route("/delete/<int:id>")
def delete(id):
    car_delete = Car.query.get(id)
    db.session.delete(car_delete)
    db.session.commit()

    return redirect(url_for("home"))


# car_to_delete = Car.query.first()

# db.session.delete(car_to_delete)
# db.session.commit()

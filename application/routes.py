from application import app, db 
from application.models import Car
from application.forms import BasicForm, RentForm
from flask import render_template, redirect, url_for, request


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


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    car_update = Car.query.get(id)
    form = RentForm()
    if request.method == 'POST':
        car_update.car_Make = form.car_Make.data
        car_update.car_Model = form.car_Model.data
        car_update.car_year = form.car_year.data
        car_update.car_description = form.car_description.data
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

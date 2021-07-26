# from . import db

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(100), nullable=False)
#     completed = db.Column(db.Boolean, nullable=False, default=False)



# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(30), nullable=False)
#     last_name = db.Column(db.String(30), nullable=False)


from application import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(45), nullable=False)
    email_address = db.Column(db.String(40), nullable=True)
    orders = db.relationship('Orders', backref='client')

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity_purchased = db.Column(db.Integer, nullable=True)
    order_date= db.Column(db.DateTime)
    client_order = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    car = db.relationship('Car', backref='orders')

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_Make = db.Column(db.String(45), nullable=False)
    car_Model = db.Column(db.String(35), nullable=False)
    car_year = db.Column(db.Integer, nullable=False)
    car_description = db.Column(db.String(100), nullable=True)
    order_car = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)



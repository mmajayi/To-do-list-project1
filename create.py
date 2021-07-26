from application import db
from application.models import Car, Client, Orders


db.drop_all() 
db.create_all()

first_client = Client(first_name="Paul", last_name="Davies", address="123 John Doe Street", email_address="pdavies@outlook.com")
second_client = Client(first_name="Sam", last_name="Foden", address="3 Chelsea Avenue", email_address="samfoden@outlook.com")
third_client = Client(first_name="Mike", last_name="Kane", address="321 John Street", email_address="mkane@gmail.com")
fourth_client = Client(first_name="John", last_name="Beckham", address="10 Downing Street", email_address="jbecks@yahoo.com")
fifth_client = Client(first_name="Cindy", last_name="Jackson", address="40 London Close", email_address="cindy@hotmail.com")


db.session.add(first_client)
db.session.add(second_client)
db.session.add(third_client)
db.session.add(fourth_client)
db.session.add(fifth_client)
db.session.commit()


first_Orders = Orders(quantity_purchased="1", order_date="2021-07-21 16:46:59.502157", client_order="1")
second_Orders = Orders(quantity_purchased="1", order_date="2021-06-11 13:26:59.205867", client_order="3")
third_Orders = Orders(quantity_purchased="3", order_date="2021-04-21 08:56:20.532337", client_order="2")
fourth_Orders = Orders(quantity_purchased="2", order_date="2020-11-17 14:12:32.522166", client_order="4")
fifth_Orders = Orders(quantity_purchased="5", order_date="2020-12-20 03:28:30.404157", client_order="5")
sixth_Orders = Orders(quantity_purchased="1", order_date="2021-07-03 21:19:11.675659", client_order="1")

db.session.add(first_Orders)
db.session.add(second_Orders)
db.session.add(third_Orders)
db.session.add(fourth_Orders)
db.session.add(fifth_Orders)
db.session.add(sixth_Orders)
db.session.commit()

first_car = Car(car_Make="Ford" , car_Model="Focus" , car_year="2018", car_description="Fast, nippy and economical car", order_car="1")
second_car = Car(car_Make="Vauxhall" , car_Model="Corsa" , car_year="2018", car_description="Flight and environmentally friendly", order_car="2")
third_car = Car(car_Make="Land Rover" , car_Model="Range Rover" , car_year="2021", car_description="Luxury SUX and good off roader", order_car="3")
fourth_car = Car(car_Make="Lamborghini" , car_Model="Urus" , car_year="2020", car_description="Sports car in a sleek SUV style", order_car="4")
fifth_car = Car(car_Make="Kia", car_Model="Sportage" , car_year="2021", car_description="Family sized fun enjoyable car", order_car="5")
sixth_car = Car(car_Make="Mercedes", car_Model="E-Class" , car_year="2020", car_description="Elegant car with long standing history", order_car="6")
seventh_car = Car(car_Make="BMW" , car_Model="3 Series" , car_year="2017", car_description="Fast reliable German car", order_car="2")

db.session.add(first_car)
db.session.add(second_car)
db.session.add(third_car)
db.session.add(fourth_car)
db.session.add(fifth_car)
db.session.add(sixth_car)
db.session.add(seventh_car)
db.session.commit()
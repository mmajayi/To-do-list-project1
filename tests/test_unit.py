from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase 
from application import app, db
from application.models import Car
from flask import url_for


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            WTF_CSRF_ENABLED=False
        )

        return app
    
    def setUp(self):
        db.create_all()
        db.session.add(Car(car_Make="Ford" , car_Model="Focus" , car_year="2018", car_description="Fast, nippy and economical car", order_car="1")
)
       
        db.session.commit()

    def tearDown(self):
        db.drop_all()


class TestView(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assert200(response)


    def test_add(self):
        response = self.client.get(url_for("add"))
        self.assert200(response)


    def test_update(self):
        response = self.client.get(url_for("update", id=1))
        self.assert200(response)

class TestRead(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))

        assert "Ford" in response.data.decode()
        
    
class TestAdd(TestBase):
    def test_add(self):
        response = self.client.post(
            url_for('add'),
            data={"car_Make": "Dodge"},

            follow_redirects=True
        )

        assert "Dodge" in response.data.decode()

class TestEdit(TestBase):
    def test_edit(self):
        response = self.client.post(
            url_for('add', id=3),
            data={"Land Rover": "Mazda"},

            follow_redirects=True
        )

        assert "Mazda" in response.data.decode()
        

class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.get(url_for('delete', id=1))
        follow_redirects=True

        assert "Ford" not in response.data.decode()




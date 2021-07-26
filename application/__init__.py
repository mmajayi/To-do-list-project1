# from flask import Flask
# 
# # C



# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"



# # app.config['SECRET_KEY = str(os.urandom(16))'] = 

# # SECRET_KEY = str(os.urandom(16))

# db = SQLAlchemy(app)

# from application import routes

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

# 

# db.create_all()
# db.drop_all()

import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = str(os.urandom(16))

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:testpass@34.142.88.11/car'

db = SQLAlchemy(app)

from application import routes
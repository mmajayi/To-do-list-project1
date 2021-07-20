from application import db 
from application.models import Task 

db.drop_all() 
db.create_all() 
 
first_task = Task(description="Idk, some task!") 
second_task = Task(description="Idk, some other task!", completed=True)  

db.session.add(first_task) 
db.session.add(second_task) 
db.session.commit() 

 
 
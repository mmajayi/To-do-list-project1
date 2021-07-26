# Mike's Car Rental README.md 

## Content

* [Introduction](#introduction) 
  * [Objective](#objective)
  * [Proposal](#proposal)
* [Architecture](#architecture)
  * [Risk Assessment](#risk-assessment)
  * [Jira](#jira)
  * [Entity Relationship Diagram](#entity-relationship-diagram)
  * [Continuous Integration](#continuous-integration)
* [Development](#development)
  * [Testing](#testing)
* [Footer](#footer)

## Introduction

### Objective

This project provided a solid foundation on key DevOps fundamentals such as. Project Management, Python Fundamentals, Python Testing, Git, Basic Linux, Python Web Development, Continuous Integration, Cloud Fundamentals, Databases.

The project focussed on the createation of a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules covered during training.

### Proposal

In this project I have decided to create a CRUD application for a Car Rental company which allows users to view, select, edit and delete the cars they wish to rent.

An outline of how I have implemented the CRUD application functionalities are as follow:  

Create:  
- Available rental car selections
- Add a rental car selection
- User/client profile and information

Read:
- View client, car and orders
- View car profile and description
- View cars available to rent

Update
- Change the preference of a car you wish as a user
- Update client information/profile

Delete
- Delete cars from the database
- Delete client information from the database



## Architecture

### Risk Assessment

Below is my risk assessment going into detail of the possible cyber attacks that become a potential threat to my web app or to any application. This risk assessment goes into the typical cause of some risks and the solution while it is happening and how to prevent a risk emerging in the future. 

Google Docs Risk Assessment  
[Link to my Risk Assessment](https://docs.google.com/spreadsheets/d/11WV03PXcX_gj0fiztK3AGl0nGf49VlLtsd38Yo333X8/edit#gid=0)

As the course continued more risks became relevant in relation to my web app, as a result there is a date added column on the far right for the times I have added a new risk that was appropriate in line of what I had learnt in the course.

### Jira

The Jira User story was made to understand what the client, developer or any relevant party wanted from the web application.  This created a multi lens perspective to get a clear depth of understanding of what different users want.   

User Story  
[Link to application User Stories](https://team-1624354737559.atlassian.net/jira/software/projects/PROJ/boards/5/roadmap?atlOrigin=eyJpIjoiMDRiOGQ4NTNkYTNhNGNjOTk1ZWYxNGI0YWUyNTAyN2MiLCJwIjoiaiJ9&timeline=MONTHS&shared=)


My Jira board was used to track my progression and ensure I am up to date on all tasks. I was ticking tasks off that were completed as I went along. Jira proved to be a great way for me to fully organise myself and my tasks and tackle each task efficiently. I choose Jira because the user face is clear and the entire website is intuitive and engaging. This would be an ideal app for someone who is starting their career in DevOps.

Jira Board  
[Link to Jira Board](https://team-1624354737559.atlassian.net/jira/software/projects/PROJ/boards/5)

### Entity Relationship Diagram 

This is the first Version of my ERD. This was completed very early on in the project. This ERD consisted of two tables; cars and orders in a one to many relationship.

![First Version of my ERD](https://lucid.app/publicSegments/view/7d71300d-c821-4f59-928b-f0b80da6a3d0/image.png)



This revisited second version of my ERD allowed me to get a better grasp of what each table should consist of depending on user needs. Additionally, this second ERD follows how my database is structured. The change and addition in tables was due to lack of checkout authenticator and authorisation. Therefore, I created a client table with unique attributes to distinguish between the different client orders. 

![Revisited Second ERD](https://lucid.app/publicSegments/view/fc221f3e-a88b-4b51-a64f-241441730653/image.png)

I have used the one=to=many relationship because after using my first ERD as a guide for my second ERD. A car can have only one client at a single time but one single client can have man orders. 


## Continuous Integration

[Link to my CI Pipeline](https://docs.google.com/document/d/1gjioqiHzDXwMo6dzBvPu3lT5CjaPNko0gjVctzbqXRw/edit?usp=sharing)

Here is a deailed pipeline demonstrating the various stages in a continuous integration. 


## Development 

### Testing

This project solely focuses on unit testing and integration testing. However, there are many other tests that would normally come to play before a web application can go live. For example, speed and process testing will go through rigorous testing to ensure user experience is kept to a high standard. 
#### Breaches 
As highlighted in my risk assessment earlier, data breaches are very common. Web applications willgo through non stop security runs and patches to prevent major security breaches. Of course bugs can still sneak in however, security measures are put in place to minimise this.  
#### Data Storage
With data storage on a rise web apps must be compatible to the change from physial storage to data centre cloud storages. Back up and reliability would have been testing before an official application can go live.  
#### UX and UI
Lastly, general UX and UI will be improved throughout the entire process of the web application. This is done to improve any small or large features in the users interest such as tranistional slides from page to page or animated effects.  



### Unit Testing

Unit testing is a great tool for DevOps as it increases automation by seperating the route functions and testing each function with numerous well thought out tasks. The main responsibility of this is to assert each function returns an expected response under each given input task. Unit tests are run fully autonomously after every Git push using Jenkins. Jenkins prints out whether or not the tests were successsful and also gives a coverage report noting the percentage of the application that was tested as listed below. 


```
====================================================== short test summary info =======================================================
FAILED tests/test_unit.py::TestAdd::test_add - AssertionError: assert 'Dodge' in '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final...
FAILED tests/test_unit.py::TestEdit::test_edit - AssertionError: assert 'Mazda' in '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Fin...
==================================================== 2 failed, 5 passed in 1.23s =====================================================
```

In this project I encountered many different obstacles such as testing, when a unit fails Jenkins build is marked as a fail. This is illustrative in my example above.If any of the unit testing fails, the entire Jenkins build is marked as a fail, as you can see in the example below. 


#### Coverage

````
----------- coverage: platform linux, python 3.6.9-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
application/__init__.py       9      0   100%
application/forms.py         16      0   100%
application/models.py        21      0   100%
application/routes.py        31      7    77%
---------------------------------------------
TOTAL                        77      7    91%

====================================================== short test summary info =======================================================
FAILED tests/test_unit.py::TestAdd::test_add - AssertionError: assert 'Dodge' in '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final...
FAILED tests/test_unit.py::TestEdit::test_edit - AssertionError: assert 'Mazda' in '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Fin...
==================================================== 2 failed, 5 passed in 1.70s =====================================================
````


## Front End

Web Application

When navigating to the home page (/) or to the URL with no specified path, the user is shown a list of all the rental cars available including the car manufactures make, model, year and description. Each entry is shown in a row style with the buttons edit and delete on the far right of the text.  
The edit button allows users to change the vehicle so it suits their preference so long we have the vehicle in stock.  
The delete button allows users to quickly delete rental cars they are no longer interested with ease.  
The (/add) funtionality provides users with the option to add a new car they wish to rent for complete UX control.


## Footer

### Future Improvements  
Future improvements include a jam packed new innovative design to improve UI and excite users when they come to the web app. This will also go into further detail and analysis of CRUD functionalities exploring all the possibilities this brings. 


### Author
Mike Ajayi
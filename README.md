# Student Project
Flask Microservices

## Installation

#### Install required Python Packages
```
pip install -r requirements.txt
```

#### Connect Flask Models to Mysql Database
- Create Database in mysql using following command:
```
create database student_db;
use student_db;
```
- Go into the Interpreter and run the following commands to create tables in student_db:
```
from app import db
db.create_all()
```

#### Credentials
- We need following credentials:
```
1. Mysql Credentials in app.py file
```

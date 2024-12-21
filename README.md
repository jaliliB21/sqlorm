# SQLiteORM  
**A lightweight, easy-to-use Object Relational Mapping (ORM) framework for SQLite databases in Python.**  

## Overview  
SQLiteORM simplifies database interactions by allowing developers to define models using Python classes.  
It abstracts complex SQL queries into simple Python methods, making database management more intuitive and less error-prone.  

## Features  
- Simple and intuitive model definition  
- Automatic table creation and synchronization  
- Basic CRUD operations (Create, Read, Update, Delete)  
- Bulk insert support for performance optimization  
- Customizable fields (e.g., unique, nullable, default)  
- Foreign key support  

## Installation  
```bash
pip install sqliteorm_py
```

## Getting Started
### 1. Create a New Project

```bash
sqliteorm-admin createproject myproject
cd myproject
```
### 2. Define Models

```python
from sqliteorm.basemodel import BaseModel, CharField, IntegerField  

class User(BaseModel):  
    table_name = "users"  
    id = IntegerField(primary_key=True, autoincrement=True)  
    name = CharField(max_length=100, unique=True)  
    age = IntegerField()  
```

### 3. Apply Migrations

```bash
py manage.py migrations
```

### 4. Insert Data
```python
from models import User  

User.insert(name="Alice", age=30)  
User.insert(name="Bob", age=25)  
```
### 5. Query Data
```python
users = User.all()  
for user in users:  
    print(user.name, user.age)    
```
### 6. Update Records
```python
User.update({"name": "Alice"}, age=35)   
```

### 7. Delete Records
```python
User.delete(name="Bob")  
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss the proposed changes

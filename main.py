from models import User
import sqlite3


def get_table_info():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(users);")

    columns = cursor.fetchall()

    for column in columns:
        print(column)

    conn.close()


# get_table_info()

"""
First, set the name of the database in the file settings
Second, create the models (tables) in the models file
Third, type this command: py manage.py migrations
And finally:
"""


# User.insert(age=22, name="behzad")
# User.insert(name="behzad jalili", age=18)
# User.insert(name='n', age='18')

# User.update({"name": "beh"}, id=2)
# User.update({"id": 4}, name="babak")
# User.update(filters={"id": 4}, name="babak", age=9)
# User.update(filters={"id": 1}, name="behzad")


# User.delete(id=4)

# user = User.filter(name="behzad jalili", id=5)
# print(user)

users = User.all()

for user in users:
    print(f"id: {user.id}\tname: {user.name}\t\tage {user.age}")

# User.all().update(age=10, name="B")
# User.all().update(age=10, name=1)

# User.all().delete()

# User.insert(name="behzad", age=22)
# User.insert(name="bahar", age=19)
# User.insert(name="azadeh2", age=25)

# User.insert(name="Behzad", age=18)
#
# User.insert(name="Behzad", age=18)



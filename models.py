from sqliteorm.basemodel import BaseModel
from sqliteorm.fields import CharField, IntegerField, ForeignKey, TextField


class User(BaseModel):
    table_name = "users"
    id = IntegerField(primary_key=True, autoincrement=True)
    name = CharField(max_length=100, unique=True)
    age = IntegerField()


# class Author(BaseModel):
#     table_name = "authors"
#     id = IntegerField(primary_key=True, autoincrement=True)
#     name = CharField(max_length=100)
#     # age = IntegerField()
#
#
# class Book(BaseModel):
#     table_name = "books"
#     id = IntegerField(primary_key=True, autoincrement=True)
#     title = CharField(max_length=200)
#     desc = TextField()
#     author_id = ForeignKey(Author, on_delete="CASCADE")


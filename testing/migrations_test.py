import unittest
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from sqliteorm.basemodel import BaseModel, IntegerField, CharField, TextField
from sqliteorm import get_existing_tables, drop_table


class TestMigrations(unittest.TestCase):
    """
    This class contains tests for migration operations such as creating tables,
    adding fields, removing fields, and synchronizing models with the database.
    """

    def test_create_table(self):
        """
        Test that a new table is created for a model.
        """
        class NewModel(BaseModel):
            table_name = "new_model"
            id = IntegerField(primary_key=True, autoincrement=True)
            name = CharField(max_length=50)

        NewModel.create_table()
        # drop_table(NewModel.table_name)
        tables = get_existing_tables()
        # assert "NewNodel" in get_existing_tables()
        self.assertIn("new_model", tables)

    # def test_add_field(self):
    #     """
    #     Test that a new column is added to an existing table.
    #     """
    #     class User(BaseModel):
    #         table_name = "users"
    #         id = IntegerField(primary_key=True, autoincrement=True)
    #         name = CharField(max_length=50)
    #
    #     # Create table initially
    #     User.create_table()
    #
    #     # Add a new field
    #     User.age = IntegerField(default=20)
    #     User.sync_fields()
    #
    #     # Verify that the new column exists
    #     columns = User.get_existing_columns()
    #     self.assertIn("age", columns)

    def test_remove_missing_columns(self):
        """
        Test that columns not defined in the model are removed from the table.
        """
        class User(BaseModel):
            table_name = "users"
            id = IntegerField(primary_key=True, autoincrement=True)
            name = CharField(max_length=50)

        # Create table
        User.create_table()

        # Remove a field from the model
        del User.name
        User.remove_missing_columns()

        # Verify that the column has been removed
        columns = User.get_existing_columns()
        self.assertNotIn("name", columns)

    def test_sync_fields(self):
        """
        Test that sync_fields adds new columns without removing existing ones.
        """
        class User(BaseModel):
            table_name = "users"
            id = IntegerField(primary_key=True, autoincrement=True)
            name = CharField(max_length=50)

        User.create_table()

        # Add a new field
        User.age = IntegerField(default=25)
        User.sync_fields()

        columns = User.get_existing_columns()
        self.assertIn("name", columns)
        self.assertIn("age", columns)

    def test_add_non_nullable_field_to_existing_table_with_data(self):
        """
        Test that adding a non-nullable field to a table with data raises an error.
        """
        class User(BaseModel):
            table_name = "users"
            id = IntegerField(primary_key=True, autoincrement=True)
            name = CharField(max_length=50)

        User.create_table()
        User.insert(name="Alice")

        # Add a new non-nullable field
        User.age = IntegerField()
        with self.assertRaises(ValueError):
            User.sync_fields()

    def test_add_nullable_field_to_existing_table_with_data(self):
        """
        Test that adding a nullable field to a table with data works without error.
        """
        class User(BaseModel):
            table_name = "users"
            id = IntegerField(primary_key=True, autoincrement=True)
            name = CharField(max_length=50)

        User.create_table()
        User.insert(name="Alice")

        # Add a new nullable field
        User.age = IntegerField(null=True)
        User.sync_fields()

        columns = User.get_existing_columns()
        self.assertIn("age", columns)

    def test_drop_table(self):
        """
        Test that a table is deleted from the database.
        """
        class TempModel(BaseModel):
            table_name = "temp_model"
            id = IntegerField(primary_key=True, autoincrement=True)
            data = TextField()

        TempModel.create_table()
        drop_table(TempModel.table_name)

        tables = get_existing_tables()   # مشکلمذ اینجاست من اینو تو بیس مدل ندارم و تو مایگریشن دارم
        self.assertNotIn("temp_model", tables)

    def test_full_migration_process(self):
        """
        Test the full migration process including creating, updating, and removing fields.
        """
        class User(BaseModel):
            table_name = "users"
            id = IntegerField(primary_key=True, autoincrement=True)
            name = CharField(max_length=50)

        User.create_table()

        # Add a new field
        User.age = IntegerField(default=30)
        User.sync_fields()
        columns = User.get_existing_columns()
        self.assertIn("age", columns)

        # Remove a field
        del User.age
        User.remove_missing_columns()
        columns = User.get_existing_columns()
        self.assertNotIn("age", columns)


if __name__ == "__main__":
    unittest.main()

import unittest
import sqlite3
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from models import User


class TestUserModel(unittest.TestCase):
    def setUp(self):
        """
        This method runs before every test to create a clean table.
        """
        User.create_table()

    def tearDown(self):
        """
        This method runs after every test to clear the table.
        """
        User.all().delete()

    # -----------------------------
    # Tests for insert()
    # -----------------------------
    def test_insert_missing_required_field(self):
        """
        Test that inserting a record without required fields raises ValueError.
        """
        with self.assertRaises(ValueError) as context:
            User.insert(age=25)  # 'name' is a required field and is not provided

        # Optional: Check the exact error message
        self.assertIn("Missing required fields", str(context.exception))

    def test_insert_exceeding_max_length(self):
        with self.assertRaises(ValueError):
            User.insert(name="A" * 300, age=25)

    def test_insert_invalid_type(self):
        with self.assertRaises(TypeError):
            User.insert(name=12345, age="twenty")

    def test_insert_empty_record(self):
        with self.assertRaises(ValueError):
            User.insert()

    # -----------------------------
    # Tests for update()
    # -----------------------------
    def test_update_without_filters(self):
        with self.assertRaises(ValueError):
            User.update({}, age=30)

    def test_update_no_data(self):
        with self.assertRaises(ValueError):
            User.update({"name": "Alice"})

    def test_update_non_existent_record(self):
        affected_rows = User.update({"name": "NonExistent"}, age=30)
        self.assertEqual(affected_rows, 0)

    def test_update_invalid_type(self):
        User.insert(name="Alice", age=25)
        with self.assertRaises(TypeError):
            User.update({"name": "Alice"}, age="not_a_number")

    # -----------------------------
    # Tests for delete()
    # -----------------------------
    def test_delete_without_filters(self):
        with self.assertRaises(ValueError):
            User.delete()

    def test_delete_non_existent_record(self):
        affected_rows = User.delete(name="NonExistent")
        self.assertEqual(affected_rows, 0)

    # -----------------------------
    # Tests for filter()
    # -----------------------------
    def test_filter_without_conditions(self):
        with self.assertRaises(ValueError):
            User.filter()

    def test_filter_non_existent_field(self):
        with self.assertRaises(Exception):
            User.filter(non_existent_field="value")

    def test_filter_on_empty_table(self):
        filtered_users = User.filter(name="Alice")
        self.assertEqual(len(filtered_users), 0)

    # -----------------------------
    # Tests for all()
    # -----------------------------
    def test_all_on_empty_table(self):
        users = User.all()
        self.assertEqual(len(users), 0)

    def test_all_with_large_number_of_records(self):
        for i in range(10):
            User.insert(name=f"User{i}", age=i)
        users = User.all()
        self.assertEqual(len(users), 10)

    # -----------------------------
    # Combined Tests for All + Update + Delete
    # -----------------------------
    def test_all_update(self):
        User.insert(name="Alice", age=25)
        User.insert(name="Bob", age=30)
        User.all().update(age=40)
        users = User.all()
        self.assertEqual(users[0].age, 40)
        self.assertEqual(users[1].age, 40)

    def test_all_delete(self):
        User.insert(name="Alice", age=25)
        User.insert(name="Bob", age=30)
        User.all().delete()
        users = User.all()
        self.assertEqual(len(users), 0)

    def test_unique_field(self):
        """
        Test inserting a record with a unique field and attempting to insert a duplicate.
        """
        # Insert the first record
        User.insert(name="unique_name", age=30)

        # Attempt to insert a record with the same unique field
        with self.assertRaises(sqlite3.IntegrityError) as context:
            User.insert(name="unique_name", age=25)  # Same `name` field, which is unique

        # Assert that the error message mentions the UNIQUE constraint
        self.assertIn("UNIQUE constraint failed", str(context.exception))


# Run all tests
if __name__ == "__main__":
    unittest.main()

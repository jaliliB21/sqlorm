import unittest
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from models import User



class TestUserModel(unittest.TestCase):
    def setUp(self):
        """
        This method is executed before each test to create a clean table.
        """
        User.create_table()

    def tearDown(self):
        """
        This method is executed after each test to delete all records.
        """
        User.all().delete()

    def test_create_table(self):
        """
        Test the creation of the table for the model.
        """
        try:
            User.create_table()
            self.assertTrue(True)  # If no exception is raised, test passes.
        except Exception as e:
            self.fail(f"create_table raised an exception: {e}")

    def test_insert(self):
        """
        Test inserting a record into the table.
        """
        User.insert(name="Aram", age=20)
        users = User.all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, "Aram")
        self.assertEqual(users[0].age, 20)

    def test_all(self):
        """
        Test the all() method to return all records.
        """
        User.insert(name="Behzad", age=22)
        User.insert(name="babak", age=25)
        users = User.all()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].name, "Behzad")
        self.assertEqual(users[1].name, "babak")

    def test_update(self):
        """
        Test updating a specific record in the table.
        """
        User.insert(name="Aram", age=25)
        User.update({"name": "Aram"}, age=30)
        updated_user = User.filter(name="Aram")[0]
        self.assertEqual(updated_user.age, 30)

    def test_delete(self):
        """
        Test deleting a specific record from the table.
        """
        User.insert(name="Aram", age=25)
        User.delete(name="Aram")
        users = User.all()
        self.assertEqual(len(users), 0)

    def test_filter(self):
        """
        Test filtering records based on specific conditions.
        """
        User.insert(name="Aram", age=25)
        User.insert(name="Behzad", age=30)
        filtered_users = User.filter(age=25)
        self.assertEqual(len(filtered_users), 1)
        self.assertEqual(filtered_users[0].name, "Aram")

    def test_all_update(self):
        """
        Test updating all records using all().update().
        """
        User.insert(name="Aram", age=25)
        User.insert(name="Behzad", age=30)

        # Update all records
        User.all().update(age=40)

        users = User.all()
        self.assertEqual(users[0].age, 40)
        self.assertEqual(users[1].age, 40)

    def test_all_delete(self):
        """
        Test deleting all records using all().delete().
        """
        User.insert(name="Aram", age=25)
        User.insert(name="Behzad", age=30)

        # Delete all records
        User.all().delete()

        users = User.all()
        self.assertEqual(len(users), 0)

    def test_non_duplicate_unique_field(self):
        """
        Test inserting records with different values for the unique field.
        """
        User.insert(name="unique_name1", age=30)
        User.insert(name="unique_name2", age=25)  # Different `name` value

        # Assert that both records are inserted successfully
        all_users = User.all()
        self.assertEqual(len(all_users), 2)
        self.assertEqual(all_users[0].name, "unique_name1")
        self.assertEqual(all_users[1].name, "unique_name2")


if __name__ == "__main__":
    unittest.main()

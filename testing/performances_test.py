import timeit
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ""))
sys.path.append(parent_dir)

# from models import User


def test_insert_performance():
    """
    Measure the performance of the insert method.
    """
    setup_code = """from models import User"""
    test_code = """User.insert(verbose=False, name='PerformanceTest', age=30)"""

    execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1000)
    print(f"Insert method executed 1000 times in: {execution_time:.5f} seconds")


def test_bulk_insert_performance():
    """
    Test performance of the bulk_insert method by inserting multiple records.
    """
    setup_code = """
from models import User
data = [{"name": f"User{i}", "age": i} for i in range(1000)]"""
    test_code = """User.bulk_insert(data)"""
    # Measure execution time
    execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1)
    print(f"Bulk insert method executed 1 time for 1000 records in: {execution_time:.5f} seconds")


def test_all_performance():
    """
    Measure the performance of the all method.
    """
    setup_code = """
from models import User
User.insert(name='User1', age=25)
User.insert(name='User2', age=30)"""
    test_code = """User.all()"""

    execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1000)
    print(f"All method executed 1000 times in: {execution_time:.5f} seconds")


def test_update_performance():
    """
    Measure the performance of the update method.
    """
    setup_code = """
from models import User
User.insert(name='UpdateTest', age=30)"""
    test_code = """User.update(filters={"name": "UpdateTest"}, age=40)"""
    execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1000)
    print(f"Update method executed 1000 times in: {execution_time:.5f} seconds")


def test_delete_performance():
    """
    Measure the performance of the delete method.
    """
    setup_code = """
from models import User
User.insert(name='DeleteTest', age=25)
"""
    test_code = """User.delete(name='DeleteTest')"""
    execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1000)
    print(f"Delete method executed 1000 times in: {execution_time:.5f} seconds")


if __name__ == "__main__":
    # test_insert_performance()
    test_bulk_insert_performance()
    # test_all_performance()
    # test_update_performance()
    # test_delete_performance()

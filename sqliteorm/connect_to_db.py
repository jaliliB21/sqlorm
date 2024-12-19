from settings import DATABASE_NAME
import sqlite3
import importlib


class DatabaseConfig:
    _database_name = None

    @classmethod
    def get_database(cls):
        if cls._database_name is None:
            try:
                settings = importlib.import_module("settings")
                cls._database_name = getattr(settings, "DATABASE_NAME", None)
                if not cls._database_name:
                    raise ValueError("DATABASE_NAME is not set in settings.py.")
            except ModuleNotFoundError:
                raise ValueError("Settings module not found. Please create a 'settings.py' file.")
        return cls._database_name


# def connect_to_database():
#     """
#     Establish a connection to the database.
#     """
#     if not DATABASE_NAME:
#         raise ValueError("DATABASE_NAME is not set in settings.py.")
#     return sqlite3.connect(DATABASE_NAME)

def connect_to_database():
    """
    Establish a connection to the database.
    """
    db_name = DatabaseConfig.get_database()
    return sqlite3.connect(db_name)

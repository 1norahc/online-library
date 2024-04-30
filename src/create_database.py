import sqlite3
from src.lib.books.book import Book
from database import DB
from usr.user import User

class CREATE_DATABASE(Book):
    def __init__(self):
        super().__init__()  # Call the __init__ method of the parent class to initialize Book attributes
        self.create_sql_connection()
        
        # Generate SQL statement dynamically based on Book attributes
        sql_columns = ",\n".join([f"{attr} TEXT" for attr in self.__dict__.keys()])
        sql_statement = f"""
            CREATE TABLE IF NOT EXISTS Books (
                id INTEGER PRIMARY KEY,
                {sql_columns}
            )
        """
        
        self.cursor.execute(sql_statement)
        self.connection.commit()
        self.connection.close()
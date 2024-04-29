from dataclasses import dataclass
import sqlite3
import os

class CREATE_DATABASE:
    def __init__(self): pass    

class DBFileDoesNotExists(Exception):
    def __init__(self, exception = "Data base file does not exists. Please give correct data base file path."):
        self.exception = exception
        super().__init__(self.exception)
        
    def __str__(self):
        return f"{self.exception}"

@dataclass    
class DB:
    """
    DATABASE for online library
    """
    database_file_name: str = "database/online-library.db"
    ERROR: bool = False
    EXCEPTION: str = ""
    
    try:
        if os.path.exists(database_file_name):
            ERROR = False
        else:
            ERROR = True
            raise DBFileDoesNotExists
    except DBFileDoesNotExists as e:
        EXCEPTION += str(e)
    
    def create_sql_connection(self):
        connection = sqlite3.connect(self.database_file_name)
        cursor = connection.cursor()
        return connection, cursor
    
    def _valid_data_structure(self, data_file_name: str):
        """
        @NOTE
        VALIDATE DATA FILE TO IMPORT DATA INTO DATABASE
        : valid data temp. :
            1. txt file (now)
            2. cells -> x;y;z (the first cell is always the primary key (for now!))
            # dodac wybranie opcji klucza glownego
        """
        _ = []
        with open(data_file_name, "r") as dfName:
            record = ""
            for line in dfName:
                line = line.strip()                      # usuń ewentualne białe znaki na początku i końcu linii
                if line:                                 # jeśli linia nie jest pusta
                    record += line                       # dodaj ją do aktualnego rekordu
                    if record.count(';') >= 6:           # jeśli mamy 7 lub więcej średników
                        _.append(record.split(';'))   # podziel rekord i dodaj go do listy danych
                        record = ""                      # zresetuj zmienną rekord
        data = []
        for record in _:
            data.append(record[0:-1])
            
        return data
        
    def push2db(self, data: str): pass

    
    def __str__(self):
        # dodać to zeby bledy byly zapisywane w pliku z data oraz dlugoscia wykonywania progrmau
        string = f"\nTest\n====\n\nError: {self.ERROR}\nException: {self.EXCEPTION}\n"
        return string
    
db = DB()
x = db._valid_data_structure("database/test_data_book.txt")
for i in x:
    print(i)
    



    

        
    
        
        
        
        
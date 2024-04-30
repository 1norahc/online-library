
class Book:
    def __init__(self, id, title, author, release_date, publishing_house, summary, pages):
        self.id = id
        self.title = title
        self.author = author
        self.release_date = release_date
        self.publishing_house = publishing_house
        self.summary = summary
        self.pages = pages
        
    def __str__(self):
        return f"{self.id};{self.title};{self.author};{self.release_date};{self.publishing_house};{self.summary};{self.pages};"
    
"""x = "1;Expanded national product;Frank Diaz;2021-07-30;Morris-Collier;Surface community could brother. Rate reason outside street.Green them executive name base long. Bit security nor stuff key kind determine.;185;"    
x = x.split(";")
d = x[0:-1]
print(x)
book = Book(*d)"""

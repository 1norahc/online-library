
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
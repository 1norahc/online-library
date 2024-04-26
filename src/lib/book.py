from utils import Utils
from ..dtype import DType

class Book(Utils):
    def __init__(self,
                 id: int,
                 name: str,
                 author: str,
                 release_date: DType.date,
                 publishing_house: str,
                 summary: str,
                 pages: int):
        self.id = id
        self.name = name
        self.author = author
        self.release_date = release_date
        self.publishing_house = publishing_house
        self.summary = summary
        self.pages = pages

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Author: {self.author}, Release Date: {self.release_date}, Publishing House: {self.publishing_house}, Summary: {self.summary}, Pages: {self.pages}"


        
    

"""
# Jakie cechy ma ksiazka?

Book("id", "name", "author", "data_premiery","data_wydania", "wydawnictwo", "summary", "pages", )

"""
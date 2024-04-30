import random
from faker import Faker
fake = Faker()
from .lib.books.book import Book

def generate_random_book(id):
    title = fake.catch_phrase()
    author = fake.name()
    release_date = fake.date_time_this_decade().strftime("%Y-%m-%d")
    publishing_house = fake.company()
    summary = fake.text(max_nb_chars=200)
    pages = random.randint(50, 500)
    
    return Book(id, title, author, release_date, publishing_house, summary, pages)

def generate():
    # Generate 50 random books
    with open("./database/test_data_book.txt", "w+") as f:
        for i in range(1, 50+1):
            book_data = generate_random_book(i)
            f.write(str(book_data))
            f.write("\n")
generate()
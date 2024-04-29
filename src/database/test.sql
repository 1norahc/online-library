CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                email TEXT,
                password TEXT
            )

CREATE TABLE if NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    release_date DATE,
    publishing_house TEXT,
    summary TEXT,
    pages INTEGER
)
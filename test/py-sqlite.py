import sqlite3

# Połączenie z bazą danych SQLite
conn = sqlite3.connect('moja_baza.db')
cursor = conn.cursor()

# Stworzenie tabeli
cursor.execute('''CREATE TABLE IF NOT EXISTS Osoby (
                    id INTEGER PRIMARY KEY,
                    imie TEXT NOT NULL,
                    nazwisko TEXT NOT NULL,
                    wiek INTEGER
                )''')

# Zatwierdzenie zmian i zamknięcie połączenia
conn.commit()
conn.close()


# Dodawanie danych
conn = sqlite3.connect('moja_baza.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO Osoby (imie, nazwisko, wiek) VALUES (?, ?, ?)", ('Jan', 'Kowalski', 30))

conn.commit()

# Pobieranie danych
cursor.execute("SELECT * FROM Osoby")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


# Dodawanie danych
conn = sqlite3.connect('moja_baza.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO Osoby (imie, nazwisko, wiek) VALUES (?, ?, ?)", ('Jan', 'Kowalski', 30))

conn.commit()

# Pobieranie danych
cursor.execute("SELECT * FROM Osoby")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

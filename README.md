# Biblioteka Online - tylko ksiązki w pdf :D (póki co :o)
Projekt "Biblioteka Online" to aplikacja webowa oparta na frameworku Django, która umożliwia użytkownikom przeglądanie, dodawanie, edytowanie i usuwanie książek oraz autorów. Aplikacja wykorzystuje bazę danych do przechowywania informacji o książkach i autorach.

## Funkcje

- Rejestracja i logowanie użytkowników.
- Przeglądanie książek i autorów.
- Dodawanie, edytowanie i usuwanie książek i autorów.
- Wyszukiwanie książek.
- Wypożyczanie i zwracanie książek.
- Generowanie rankingów książek.
- Integracja z innym językiem programowania (opcjonalnie).
- Streszaczanie ksiązek

## Technologie i algorytmy

- Baza danych: SQLite lub PostgreSQL.
- Algorytm sortowania: np. quicksort lub mergesort.
- Framework Django.
- Integracja z innym językiem programowania: np. JavaScript z użyciem frameworka React (opcjonalnie).

## Uruchomienie projektu

1. Sklonuj repozytorium: `git clone https://github.com/1norahc/online-library.git`

2. Zainstaluj wirtualne środowisko (MacOS)
    - `python3 -m venv <venv_name>`
    - `source <venv_name>/bin/activate`

3. Zainstaluj wymagane biblioteki: `pip install -r requirements.txt`

4. Utwórz migracje:
`python manage.py makemigrations`
`python manage.py migrate`

5. Uruchom serwer deweloperski: `python manage.py runserver`

6. Przejdź do przeglądarki i otwórz adres `http://localhost:8000/`.

## Kontrybucje

Zachęcamy do zgłaszania problemów i propozycji poprawek poprzez tworzenie zgłoszeń [tutaj](https://github.com/twoja_nazwa_uzytkownika/biblioteka-online/issues)

## Autor

Projekt został stworzony przez [Rajan Bor].

---

Cieszymy się, że zainteresowałeś się naszym projektem! Jeśli masz jakiekolwiek pytania lub sugestie, prosimy o kontakt.

import re

class User:
    def __init__(self, username, email, phone_number, password):
        self.username = username
        if self._validate_email(email):
            self.email = email
        else:
            raise ValueError("Invalid email format.")
        if self._validate_phone_number(phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError("Invalid phone number format.")
        self.password = password
        self.borrowed_books = []
        self.favorite_books = []

    def _validate_email(self, email):
        """Email validator"""
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(pattern, email)

    def _validate_phone_number(self, phone_number):
        pattern = r"\d{3}-\d{3}-\d{3}"
        return re.match(pattern, phone_number)
    
    def _valid_password(self, password):
        return

def test():
    # Przykładowe dane testowe
    username = "john_doe"
    email = "john.doe@example.com"
    phone_number = "123-456-789"
    password = "strongPassword123"

    # Tworzenie obiektu User z danymi testowymi
    try:
        user = User(username, email, phone_number, password)
        print("Utworzono użytkownika:")
        print("Nazwa użytkownika:", user.username)
        print("Email:", user.email)
        print("Numer telefonu:", user.phone_number)
        print("Hasło:", user.password)
    except ValueError as e:
        print("Błąd podczas tworzenia użytkownika:", str(e))

test()
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
        
        if self._valid_password(password):
            self.password = password
        else:
            raise ValueError("Invalid password pattern")
        
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
        pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        return bool(re.match(pattern, password))
    
    def __str__(self):
        return f"{self.username};{self.email};{self.phone_number};{self.password};"

def test():
    # Przykładowe dane testowe
    username = "john_doe"
    email = "john.doe@example.com"
    phone_number = "123-456-789"
    password = "strongPassword123@"
    
    user = User(username, email, phone_number, password)
    print(user)
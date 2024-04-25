import time

class Login:
    def __init__(self):
        self.username = "example_user"
        self.email = "example@example.com"
        self.password = "example_password"
        self.max_attempts = 3
        self.attempts = 0
        self.block_time_30min = None
        self.block_time_24h = None

    def authenticate(self, username_or_email, password):
        if self.block_time_30min and time.time() < self.block_time_30min:
            print("Konto jest zablokowane na 30 minut.")
            return False

        if self.block_time_24h and time.time() < self.block_time_24h:
            print("Konto jest zablokowane na 24 godziny.")
            return False

        if self.attempts >= self.max_attempts:
            print("Konto jest zablokowane na 30 minut.")
            self.block_time_30min = time.time() + 30 * 60
            self.attempts = 0
            return False

        if username_or_email == self.username or username_or_email == self.email:
            if password == self.password:
                print("Zalogowano pomyślnie.")
                self.attempts = 0
                return True
            else:
                print("Błędne hasło.")
                self.attempts += 1
                return False
        else:
            print("Niepoprawny username lub email.")
            self.attempts += 1
            return False

# Przykład użycia
login = Login()
print(login.authenticate("example_user", "wrong_password"))  # False
print(login.authenticate("example_user", "example_password"))  # True

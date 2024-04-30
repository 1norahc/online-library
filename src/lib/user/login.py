import json
import os
import datetime as dt
from dataclasses import dataclass

@dataclass
class Login:
    username: str = "example_user"
    email: str = "example@example.com"
    password: str = "Example_password123$"
    max_attempts: int = 3
    attempts:int = 0
    block_time_30min: int = None
    block_time_24h: int = None

    @classmethod
    def check_attempts(cls, username_or_email):
        log_file = "/Users/norahc/Desktop/Coding/GitHub/online-library/src/database/login_logs.json"
        logs = {}

        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                logs = json.load(file)

        if username_or_email in logs:
            return logs[username_or_email]
        else:
            return {"attempts": 0, "block_time_30min": None, "block_time_24h": None}

    def update_logs(self, username_or_email):
        log_file = "/Users/norahc/Desktop/Coding/GitHub/online-library/src/database/login_logs.json"
        logs = {}

        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                logs = json.load(file)

        logs[username_or_email] = {
            "attempts": self.attempts,
            "block_time_30min": self.block_time_30min,
            "block_time_24h": self.block_time_24h
        }

        with open(log_file, "w") as file:
            json.dump(logs, file, indent=4)

    def authenticate(self, username_or_email, password):
        # Odniesienie się do check_attempts, żeby uzyskać aktualne dane dotyczące prób logowania
        attempts_info = self.check_attempts(username_or_email)
        self.attempts = attempts_info["attempts"]
        self.block_time_30min = attempts_info["block_time_30min"]
        self.block_time_24h = attempts_info["block_time_24h"]

        # Jeśli użytkownik jest zablokowany na 30 minut lub 24 godziny, zwróć False
        if self.block_time_30min is not None and dt.datetime.now() < dt.datetime.fromtimestamp(self.block_time_30min):
            print(f"Użytkownik {self.username} jest zablokowany na 30 minut.")
            return False
        if self.block_time_24h is not None and dt.datetime.now() < dt.datetime.fromtimestamp(self.block_time_24h):
            print(f"Użytkownik {self.username} jest zablokowany na 24 godziny.")
            return False

        # Logika uwierzytelniania
        if password != self.password:
            self.attempts += 1
            if self.attempts >= self.max_attempts:
                self.block_time_30min = dt.datetime.timestamp(dt.datetime.now() + dt.timedelta(minutes=30))
                self.block_time_24h = dt.datetime.timestamp(dt.datetime.now() + dt.timedelta(days=1))
                print("Zbyt wiele nieudanych prób logowania. Konto zostało zablokowane.")
            self.update_logs(username_or_email)
            return False
        else:
            self.attempts = 0  # Zresetuj liczbę prób po udanym logowaniu
            self.update_logs(username_or_email)
            return True

def test():
    with open("/Users/norahc/Desktop/Coding/GitHub/online-library/src/database/users.txt", "r+") as f:
        x = f.read().splitlines()  
        user = x[0].split(";")
        print(user)
        login = Login()
        d = login.authenticate(user[0], user[3])
        print(d)
        
        

        
    
test()

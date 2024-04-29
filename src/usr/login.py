import json
import os
import datetime as dt
from dataclasses import dataclass

@dataclass
class Login:
    username: str = "example_user"
    email: str = "example@example.com"
    password: str = "example_password"
    max_attempts: int = 3
    attempts:int = 0
    block_time_30min: int = None
    block_time_24h: int = None

    @classmethod
    def check_attempts(cls, username_or_email):
        log_file = "./src/database/logs.json"
        logs = {}

        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                logs = json.load(file)

        if username_or_email in logs:
            return logs[username_or_email]
        else:
            return {"attempts": 0, "block_time_30min": None, "block_time_24h": None}

    def update_logs(self, username_or_email):
        log_file = "./src/database/logs.json"
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

        # Logika uwierzytelniania

        # Aktualizacja logów
        self.update_logs(username_or_email)

# Przykład użycia
login = Login()
print(login.authenticate("example_user", "wrong_password"))  # False
print(login.authenticate("example_user", "example_password"))  # True

class Register:
    def __init__(self, username, email, phone_number, password):
        if self.user_exists(username, email):
            print(f"Użytkownik o nazwie użytkownika {username} lub adresie e-mail {email} już istnieje.")
        else:
            self.new_user = f"{username};{email};{phone_number};{password}"
            with open("/Users/norahc/Desktop/Coding/GitHub/online-library/src/database/users.txt", "w+") as f:
                f.write(self.new_user+"\n")
            print("Nowy użytkownik został zarejestrowany pomyślnie.")
    
    def user_exists(self, username, email):
        with open("/Users/norahc/Desktop/Coding/GitHub/online-library/src/database/users.txt", "r+") as file:
            for line in file:
                user_data = line.strip().split(";")
                if user_data[0] == username or user_data[1] == email:
                    return True
        return False
    
    def __str__(self) -> str:
        return  self.new_user
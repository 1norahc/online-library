from faker import Faker
from user.register import Register
fake = Faker()

def generate_test_users(num_users):
    username = fake.user_name()
    email = fake.email()
    phone_number = fake.phone_number()
    password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return Register(username, email, phone_number, password)



def generate():
    # Generate 50 random books
    with open("/Users/norahc/Desktop/Coding/GitHub/online-library/src/database/users.txt", "w+") as f:
        for i in range(1, 50+1):
            testowe_dane = generate_test_users(5)
            f.write(str(testowe_dane))
            f.write("\n")
generate()

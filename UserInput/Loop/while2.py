#WHILE LOOP PASSWORD

user_password = input("Enter your password: ")
while user_password != '123':
    print("Incorrect password, try again")
    user_password = input("Enter your password: ")
print("Welcome to the system")
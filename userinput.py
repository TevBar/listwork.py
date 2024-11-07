#user input data processer

first_name = input("Enter your first name: ")
last_name = input("Enter your last name:")

if len(first_name) < 2: 
    print("Error: username must be more than 2 characters")
elif len(last_name) < 2:
    print("Error: username must be more than 2 characters.")

if len(first_name) >=2 and len(last_name) >=2:
    print("Username is valid")
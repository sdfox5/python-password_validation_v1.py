def validation():
    password = input("Enter your password: \n")
    
    
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return
    
    
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
        return
    
    
    if not any(char.isalpha() for char in password):
        print("Password must contain at least one letter.")
        return
    
    if not any(not char.isalnum() for char in password):
        print("Password must contain at least one symbol.")
        return
    
    print("Password is valid.")

conditioner = input("Welcome to password validation! Enter /help to see conditions: \n")
if conditioner == "/help":
    print('''
        PASSWORD VALIDATION RULES:
        - Password must be at least 8 characters long.
        - Password must contain letters, numbers, and symbols.
    ''')
else:
    print("Let's validate your password.")

while True:
    validation()
    choice = input("Do you want to validate another password? (yes/no): \n").strip().lower()
    if choice != "yes":
        print("Goodbye!")
        break
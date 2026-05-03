#Login Authentication System

username = input("Please enter your username:\n").strip()
password = input("Please enter you password:\n").strip()

def validate_login(username, password):
    
    if len(username) < 5:
        print("Error: Username must be at least 5 characters")
    elif len(username)>= 5:
        print("Good username")
        if len(password)<8:
            print("Error: Password must be at least 8 characters")
        elif len(password)>= 8:
            has_number = False
            for char in password:
                if char.isdigit():
                    has_number = True
                    break
            if has_number == True:
                print("Strong password")
                print("Login successful")
            elif has_number == False:
                print("Error: Password must contain at least one digit")
            else:
                print("ERROR!")
    else:
        print("ERROR!")

validate_login(username, password)
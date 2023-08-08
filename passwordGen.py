import random
import string

def generate_password():
    password = ''
    needsMore = True

    while (len(password) < 12 or needsMore):
        newVal=random.randint(1,4)

        if (newVal == 1):
            password += str(random.choice(string.ascii_uppercase))
        elif (newVal == 2):
            password += str(random.choice(string.ascii_lowercase))
        elif (newVal == 3):
            password += str(random.choice(string.digits))
        else:
            password += str(random.choice(string.punctuation))
            
        if (verify_password(password) == True ):
            return password

        if (len(password) == 12):
            password = password[1:]

def verify_password(password):
    u = False
    l = False
    n = False
    p = False
    size = len(password)

    for c in password:
        if c.isupper():
            u = True
        elif c.islower():
            l = True
        elif c.isdigit():
            n = True
        elif c in string.punctuation:
            p = True
            
    if u and l and n and p and size == 12:
        return True
    else:
        return False
        
# Main program

while True:
    print("\nWhat would you like to do?")
    print("1. Generate a new password")
    print("2. Verify a password")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        password = generate_password()
        print(f"\nYour new password is: {password}")
    elif choice == '2':
        while True:
            user_password = input("Enter the password you want to verify: ")
            if verify_password(user_password):
                print("The password meets minimum password requirements")
                break
            else:
                print(f"Does not meet complexity rules, it must be 12 characters long and contain a minimum of one of the following characters:\n\t-uppercase letter\n\t-lowercase letter\n\t-digit\n\t-special character\n\n\tExample: {generate_password()}\nPlease try again\n")
    elif choice == '3':
        break
    else:
        print("Invalid choice, please enter 1, 2, or 3.")

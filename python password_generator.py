import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_name_based_password(name):
    # Naam me random numbers & symbols mix kare
    symbols = "!@#$%^&*"
    numbers = str(random.randint(100, 999))
    random_symbol = random.choice(symbols)
    # First letter capital, baaki mix
    password = name.capitalize() + random_symbol + numbers
    return password

print("=== Password Generator ===")
choice = input("1: Random Password\n2: Name-based Password\nChoose option (1 or 2): ")

if choice == "1":
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_random_password(length))

elif choice == "2":
    name = input("Enter your name: ")
    print("Generated Password:", generate_name_based_password(name))

else:
    print("Invalid choice! Please run again.")

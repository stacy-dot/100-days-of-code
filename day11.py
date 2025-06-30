import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    has_letters = any(char.isalpha() for char in password)
    has_digits = any(char.isdigit() for char in password)
    has_symbols = any(char in string.punctuation for char in password)
    length = len(password)

    if length < 6:
        return "Weak"
    elif length <= 10 and has_letters and has_digits:
        return "Moderate"
    elif length > 10 and has_letters and has_digits and has_symbols:
        return "Strong"
    else:
        return "Weak"


while True:
    print("\n Password Generator with Strength Meter")
    try:
        length = int(input("Enter password length (or 0 to exit): "))
        if length == 0:
            print("Goodbye!")
            break
        elif length < 4:
            print("Too short! Must be at least 4 characters.")
        else:
            pwd = generate_password(length)
            strength = check_strength(pwd)
            print(f"\nGenerated Password: {pwd}")
            print(f" Strength: {strength}")
    except ValueError:
        print("Please enter a valid number.")

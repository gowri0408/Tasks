import random
import string

def generate_password(length):
    """Generates a random password of the specified length."""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired password length (at least 4): "))
            if length < 4:
                print("Please enter a length of at least 4.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    password = generate_password(length)
    print("Generated Password:", password)

    main()
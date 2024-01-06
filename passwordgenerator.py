import random
import string

def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: Please select at least one character set."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password 

# Get user input
length = int(input("Enter the length of the password: "))
use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Generate and print the password
password = generate_password(length, use_letters, use_numbers, use_symbols)
print("Generated Password:", password)
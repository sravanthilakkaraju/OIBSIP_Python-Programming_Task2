import random
import string

print("=== Random Password Generator ===")

length = int(input("Enter password length: "))

print("Select character types:")
use_upper = input("Include Uppercase letters? (y/n): ").lower()
use_lower = input("Include Lowercase letters? (y/n): ").lower()
use_numbers = input("Include Numbers? (y/n): ").lower()
use_symbols = input("Include Symbols? (y/n): ").lower()

characters = ""

if use_upper == 'y':
    characters += string.ascii_uppercase
if use_lower == 'y':
    characters += string.ascii_lowercase
if use_numbers == 'y':
    characters += string.digits
if use_symbols == 'y':
    characters += string.punctuation

if characters == "":
    print("❌ Error: No character type selected")
else:
    password = ""
    for _ in range(length):
        password += random.choice(characters)

    print("\n✅ Generated Password:")
    print(password)
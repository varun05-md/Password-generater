import random
import string

def generate_password(length, use_digits, use_symbols):
    characters = string.ascii_letters
    
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation 

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Check Strength
def check_strength(password):
    strength = 0

    if len(password) >= 5:
        strength += 1
    elif any(char.isdigit() for char in password):
        strength += 1
    elif any(char in string.punctuation for char in password):
        strength += 1
    elif any(char.isupper() for char in password):
        strength += 1

    if strength == 4:
        return "Strong"
    elif strength == 3:
        return "Medium "
    else:
        return "Weak "


length = int(input("Enter password length: "))
use_digits = input("Include numbers? (y/n): ") == 'y'
use_symbols = input("Include symbols? (y/n): ") == 'y'

password = generate_password(length, use_digits, use_symbols)

print("Generated Password:", password)
print("Strength:", check_strength(password))

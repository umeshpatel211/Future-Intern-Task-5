'''Create a program that generates random passwords based on criteria defined by the user, 
such as length and complexity (e.g., including uppercase letters, lowercase letters, numbers, 
and special characters). The user inputs the desired length and selects the types of characters
to include. The program then generates and displays a random password meeting these specifications,
ensuring strong security and usability.'''

import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    if character_pool == '':
        return "Error: No character types selected!"
    
    # Generate the random password from the selected character pool
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    try:
        length = int(input("Enter the desired password length (e.g., 12): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Prompt the user for their preferences
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits (0-9)? (y/n): ").lower() == 'y'
    use_special = input("Include special characters (e.g., @, #, !)? (y/n): ").lower() == 'y'
    
    if length < 1:
        print("Error: Password length must be at least 1.")
        return
    
    # Generate and display the password
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    print(f"Generated Password: {password}")

# Run the program
main()

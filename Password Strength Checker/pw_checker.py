import re

def check_password_strength(password):
    # Implement password strength criteria
    # Example: Minimum length, use of uppercase, lowercase, digits, and special characters
    length = len(password) >= 8
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~" for char in password)

    # Calculate password strength score
    score = sum([length, uppercase, lowercase, digit, special_char])

    # Provide feedback based on the score
    if score == 5:
        return "Strong Password"
    elif score >= 3:
        return "Moderate Password"
    else:
        return "Weak Password"

if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(f"Password Strength: {result}")

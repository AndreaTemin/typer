import re


# Email validations
def is_valid_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False
    
# def duplicated_email(email, session)
    
    
    
    
# Name Validation
def is_valid_name(name):
    # Check if the name is not empty
    if not name:
        return False
    # Check if the name contains any special characters
    if re.search(r'[^\w\s]', name):
        return False
    return True

# Password validation
def is_valid_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    # Check if the password contains a mix of uppercase and lowercase letters, numbers, and special characters
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`' for char in password):
        return False
    return True
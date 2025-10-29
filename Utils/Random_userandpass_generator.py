import random
import string
def generate_random_username():
    # Generate a username with no spaces, containing a mix of lowercase and uppercase letters
    length = random.randint(8, 12)  # Random length between 8 and 12
    username = ''.join(random.choices(string.ascii_letters, k=length))
    return username



def generate_random_password():
    """
    Generate a password that satisfies the following constraints:
    - At least 1 uppercase letter
    - At least 1 lowercase letter
    - At least 1 digit
    - At least 1 special character
    - Minimum length of 8 characters
    """
    # Define minimum password length and special characters
    min_length = 8  # Minimum length
    max_length = 15  # Maximum length
    special_characters = "!@#$%^&*()-+=<>?/|~"

    # Ensure at least one character of each required type
    password = [
        random.choice(string.ascii_uppercase),  # At least one uppercase letter
        random.choice(string.ascii_lowercase),  # At least one lowercase letter
        random.choice(string.digits),           # At least one digit
        random.choice(special_characters),      # At least one special character
    ]

    # Fill remaining length randomly with all allowed characters
    remaining_length = random.randint(max(min_length, len(password)), max_length)
    password += random.choices(string.ascii_letters + string.digits + special_characters, k=remaining_length - len(password))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    # Ensure password is returned as a string
    return ''.join(password)
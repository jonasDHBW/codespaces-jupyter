
import random

import string



def generate_random_password(length=12):

    # Define the character set for the password

    characters = string.ascii_letters + string.digits + string.punctuation

    

    # Generate a random password using the defined character set

    password = ''.join(random.choice(characters) for _ in range(length))

    

    return password



# Specify the desired length of the password (default is 12)

password_length = 16



# Generate a random password

random_password = generate_random_password(password_length)



# Display the generated password

print("Generated Password:", random_password)




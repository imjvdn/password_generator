import random
import string

# Set the length of the password
password_length = 20

# Generate a random password of the specified length
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))

# Print the generated password
print(password)

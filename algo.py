import hashlib
import timeit
import random
import string

def generate_salt():
    # Create a string of uppercase letters and digits
    characters = string.ascii_uppercase + string.digits
    
    # Generate a random salt of length 8
    salt = ''.join(random.choice(characters) for _ in range(16))
    
    return salt

WORK_FACTOR = 20

def hash_password(salt, password, work_factor, pepper):
    # Create a string that concatenates the salt, the password, the work factor, and the pepper
    string = salt + password + pepper

    # Hash the string 2^work_factor times
    for _ in range(2 ** int(work_factor)):
        string = hashlib.sha256(string.encode()).hexdigest()

    # Return the hashed string
    return string

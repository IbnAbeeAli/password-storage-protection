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

def hash_password(salt, password, work_factor, pepper):
    # Create a string that concatenates the salt, the password, the work factor, and the pepper
    string = salt + password + pepper

    # Hash the string 2^work_factor times
    for _ in range(2 ** int(work_factor)):
        string = hashlib.sha256(string.encode()).hexdigest()

    # Return the hashed string
    return string


# Create a function that times how long it takes to hash a password, and then returns an optimal work factor
# The work factor should be the smallest integer that results in a hash time of at least target_time_in_seconds

def find_work_factor(salt, password, pepper, target_time_in_seconds=1):
    # Initialize the work factor
    work_factor = 0

    # Initialize the hash time
    hash_time = 0

    # Loop until the hash time is at least 0.1 seconds
    while hash_time < target_time_in_seconds:

        # Increment the work factor
        work_factor += 1

        # Calculate the hash time
        hash_time = timeit.timeit(stmt=lambda: hash_password(salt, password, work_factor, pepper), number=1)

    # Return the work factor
    return work_factor



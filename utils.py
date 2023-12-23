from algo import hash_password

# A function that times how long it takes to hash a password, and then returns an optimal work factor
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


salt = 'salt'
password = 'password'
pepper = 'pepper'
print(f"Work factor: {find_work_factor(salt, password, pepper)}")
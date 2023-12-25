import timeit
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
        hash_time = timeit.timeit(stmt=lambda: hash_password(salt, password, pepper, work_factor), number=1)

    # Return the work factor
    return work_factor


salt = "SALT"
password = "PASSWORD"
pepper = "PEPPER"
target_time_in_seconds = 1

print("Salt:", salt)
print("Password:", password)
print("Pepper:", pepper)
print("Target time (seconds):", target_time_in_seconds)
print()
print("Finding optimal work factor...")
work_factor = find_work_factor(salt, password, pepper, target_time_in_seconds=target_time_in_seconds)
print("Work factor:", work_factor)
print()
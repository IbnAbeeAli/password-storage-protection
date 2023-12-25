import hashlib
import string
import sqlite3
import itertools
import timeit
from algo import hash_password

def brute_force_pepper(username, known_password, pepper_length, work_factor, peppers_to_try=10, db_file='test.db'):
    characters = string.ascii_letters + string.digits

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        table_name = 'user_credentials'
        db_entry = f"SELECT * FROM {table_name} WHERE username = '{username}'"

        cursor.execute(db_entry)
        rows = cursor.fetchall()

        if len(rows) == 0:
            print("User does not exist")
            return False

        salt = rows[0][3]
        hashed_password = rows[0][2]

        start_time_first_10 = timeit.default_timer()
        all_combinations_first_10 = itertools.islice(itertools.product(characters, repeat=pepper_length), peppers_to_try)
        for combination in all_combinations_first_10:
            brute_force_pepper = ''.join(combination)
            brute_force_hash = hash_password(salt, known_password, brute_force_pepper, work_factor)

            if brute_force_hash == hashed_password:
                end_time_first_10 = timeit.default_timer()
                elapsed_time_first_10 = end_time_first_10 - start_time_first_10
                print(f"Brute force successful for first 10!\nUsername: {username}\nSalt: {salt}\nPepper: {brute_force_pepper}")
                print(f"Time taken for first 10: {elapsed_time_first_10} seconds")
                break
        else:
            elapsed_time_first_10 = timeit.default_timer() - start_time_first_10
            print("Brute force unsuccessful for first 10 and the time taken is: ", elapsed_time_first_10)


        estimated_time_for_all = elapsed_time_first_10 * (len(characters) ** pepper_length) / peppers_to_try / 2

        estimated_days_for_all = estimated_time_for_all / (60 * 60 * 24 * 365 * 1000000000)

        print(f"Estimated average time for all peppers: {estimated_days_for_all} billion years")

        return True

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False

    finally:
        if conn:
            conn.close()

def main():
    username = 'Maaz'
    known_password = 'Maazahmed'
    # hashed_password = 'hashed_password'
    pepper_length = 18
    work_factor = 20

    brute_force_pepper(username, known_password, pepper_length, work_factor)

if __name__ == "__main__":
    main()

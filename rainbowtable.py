import hashlib
import getpass

def load_rainbow_table(file_path):
    rainbow_table = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if ':' in line:
                    try:
                        hash_value, original_password = line.strip().split(':', 1)
                        rainbow_table[hash_value] = original_password
                    except ValueError:
                        print(f"Error splitting line: {line}")
    except Exception as e:
        print(f"Error reading the file: {e}")

    return rainbow_table


def check_against_rainbow_table(username, password_hash, rainbow_table):
    if password_hash in rainbow_table:
        print("Password found in rainbow table!")
        print(f"Username: {username}")
        print(f"Original Password: {rainbow_table[password_hash]}")
        return True
    else:
        print("Password not found in rainbow table.")
        return False

def sign_in(rainbow_table_path):
    print("Sign in")

    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    rainbow_table = load_rainbow_table(rainbow_table_path)

    if check_against_rainbow_table(username, hashed_password, rainbow_table):
        return True
    else:
        print("Username or password is incorrect.")
        return False

rainbow_table_path = 'sha256_RainbowTable.txt'

sign_in_result = sign_in(rainbow_table_path)

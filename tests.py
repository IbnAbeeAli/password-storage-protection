import unittest
import sqlite3
from authentication import add_to_db, check_against_db, get_db_rows, clear_db_rows
from algo import hash_password, generate_salt, get_pepper_from_file

class TestAuthentication(unittest.TestCase):

        def setUp(self):
            self.username = "test_user"
            self.password = "test_password"
            self.db_name = "test.db"
            self.pepper = get_pepper_from_file()
            self.salt = generate_salt()
            self.password_hash = hash_password(self.salt, self.password, self.pepper)

        def test_1_add_to_db(self):
            print()
            print('Printing rows at the start of the test')
            rows = get_db_rows(self.db_name)
            self.assertEqual(len(rows), 0)
            print("Number of rows in the database: ", len(rows))


            print(f"Adding '{self.username}' with password '{self.password}' to the database...")
            # Add the user to the database
            self.assertTrue(add_to_db(self.username, self.password_hash, self.salt, self.db_name))

            # Check if the user was added to the database
            rows = get_db_rows(self.db_name)
            print('Number of rows in the database: ', len(rows))

            print(f"Asserting that '{self.username}' is in the database...")
            for row in rows:
                print(f"{row[1]}\t{row[2]}\t{row[3]}")
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0][1], self.username)
            self.assertEqual(rows[0][2], self.password_hash)
            self.assertEqual(rows[0][3], self.salt)
            print(f"'{self.username}' is in the database")
            print()

        def test_2_check_against_db(self):
            print()
            print(f"Logging in as '{self.username}'... with password '{self.password}'")
            # Check if log in is successful
            self.assertTrue(check_against_db(self.username, self.password, self.db_name))
            print(f"'{self.username}' logged in successfully")
            print()

        def test_3_check_incorrect_password(self):
            print()
            print(f"Logging in as '{self.username}'... with password 'incorrect_password'")
            # Check if log in is successful
            self.assertFalse(check_against_db(self.username, 'incorrect_password', self.db_name))
            print(f"'{self.username}' failed to log in")
            print()

        def test_4_non_existant_user(self):
            print()
            print("Asserting that a 'non_existant_user' does not exist in the database...")
            rows = get_db_rows(self.db_name)
            for row in rows:
                print(f"{row[1]}\t{row[2]}\t{row[3]}")
            # Check if the user does not exist in the database
            self.assertFalse(check_against_db("non_existent_user", "non_existent_password", self.db_name))
            print("'non_existant_user' does not exist in the database")
            print()

        def test_5_clearing_db(self):
            print()
            print('Clearing the database...')
            clear_db_rows(self.db_name)
            print('Database cleared')

            print('Printing rows after clearing the database')
            print('Number of rows in the database: ', len(get_db_rows(self.db_name)))
            self.assertEqual(len(get_db_rows(self.db_name)), 0)
            print()

        def tearDown(self):
            return


if __name__ == '__main__':
    unittest.main()
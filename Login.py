# Guess a random number game 1-100, 1-10
# Made by Christopher Lee Christensen June 2020.
# Imports
import sys
import time


# Login Function

def login():
    print('Enter correct username and password to continue')
    login_tries = 1
    while login_tries < 4:

        print('***************************')
        username = input('-Enter username: ')
        password = input('-Enter password: ')
        print('***************************')
        if password == 'pass' and username == 'ad':
            print('\n***************************')
            print('*     Access granted!     *')
            print('***************************')
            break
        elif login_tries == 3:
            password != 'pass' and username != 'ad'
            print('\n***************************\nToo many incorrect attempts\n***************************')
            sys.exit(1)
        else:
            print('Access denied. Try again.')
            time.sleep(1)
            login_tries += 1

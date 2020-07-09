# Imports
import sys
import time



# Login Function

def login():
    print('Enter correct username and password to continue')
    login_tries = 1
    while login_tries < 4:
        usr_name = ['ad']
        pw = ['pass']
        print('***************************')
        username = input('Enter username: ')
        password = input('Enter password: ')
        print('***************************')
        print(password)
        if username in usr_name and password in pw:
            print('\n***************************')
            print('*     Access granted!     *')
            print('***************************')
            break
        elif login_tries == 3:
            print('***************************\nToo many incorrect attempts\n***************************')
            sys.exit(1)
        else:
            print('Access denied.. Try again..')
            time.sleep(1)
            login_tries += 1


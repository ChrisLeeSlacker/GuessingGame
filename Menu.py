# Imports
import sys


# Menu
def menu():
    print('\n************MAIN MENU*************')
    choice = input('''
            A: 1-100
            B: 1-10
            C: NONE
            Q: Quit

    Please enter your choice: ''')
    print('**********************************')
    choice = choice.lower()
    if choice in {'a'}:
        # Local Import
        from Game import enterNum100
        enterNum100()
    elif choice in {'b'}:
        # Local Import
        from Game import enterNum10
        enterNum10()

    elif choice in {'c'}:
        print('Nothing Here')
        menu()
    elif choice in {'q'}:
        print('   Thanks for using the program')
        print('**********************************')
        sys.exit(0)
    else:
        print('You may only select either A,B or C.')
        print('Please try again')
        menu()
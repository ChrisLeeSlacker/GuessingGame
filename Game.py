# Guess a random number game 1-100, 1-10
# Made by Christopher Lee Christensen June 2020.
# Imports
import random
import sys


def ask_input(text_prompt):
    # Wait for valid numerical input
    while True:
        guess = input(text_prompt)
        try:
            # Try to typecast the input to an integer
            int(guess)
        except ValueError:
            # Catch the exception if it is not a number
            print("ERROR: Syn: Invalid Num")


# Game
def enterNum100():
    num = random.randint(1, 100)
    print("Guess the number 1 - 100")
    print("You have 5 attempts")
    print("Are you ready?\n ")

    ################################
    # The number you have to guess #
    # print(num)                   #
    ################################

    tries = 1
    while tries <= 5:
        print('Attempt No.: ', tries)
        valid = False
        while not valid:
            guess = input('Enter your guess:\n')
            if not guess.isnumeric():
                print("Please enter a number between 1-100.")
            else:
                guess = int(guess)
                if guess < 0 or guess > 100:
                    print("Please enter a number between 1-100")
                else:
                    valid = True

        # Winning
        if guess == num:
            if num >= 10:
                print('**********************\n*    Correct Guess   *\n*  The Number =', num, '  *\n'
                                                                                              '**********************')
                break
            if num < 10:
                print('**********************\n*    Correct Guess   *\n*  The Number =', num, '   *\n'
                                                                                              '**********************')
                break
        else:
            if guess > num:
                remarks = 'high'
            else:
                remarks = 'low'
            print("Wrong number!\n**********************\nYour guess is too", remarks, "\nTry "
                                                                                       "Again\n**********************")
            print("You have", 5 - tries, "left!")
            if tries == 4:
                # Last Try
                print("**********************\n***    LAST TRY    ***\n**********************")
        tries += 1
    else:
        # Game Over
        if num >= 10:
            print('**********************\n*      GAME OVER     *\n*  The Number =', num, '  *\n'
                                                                                          '**********************')

        if num < 10:
            print('**********************\n*      GAME OVER     *\n*  The Number =', num, '   *\n'
                                                                                          '**********************')

    # PLAY AGAIN OPTION
    play_again = input('\nDo you wanna try again:? \n<Y> Yes | <M> Menu | <Any key to exit> ')
    play_again = play_again.lower()
    if play_again in {'y', 'yes'}:
        print('**********************************')
        enterNum100()
    elif play_again in {'m', 'menu'}:
        print('Returning to menu')
        from Menu import menu
        menu()
    else:
        sys.exit(0)


def enterNum10():
    num = random.randint(1, 10)
    print("Guess the number 1 - 10")
    print("You have 3 attempts")
    print("Are you ready?\n ")

    ################################
    # The number you have to guess #
    # print(num)                   #
    ################################

    tries = 1
    while tries <= 3:
        print('Attempt No.: ', tries)
        valid = False
        while not valid:
            guess = input('Enter your guess:\n')
            if not guess.isnumeric():
                print("Please enter a number between 1-10.")
            else:
                guess = int(guess)
                if guess < 0 or guess > 10:
                    print("Please enter a number between 1-10")
                else:
                    valid = True

        # Winning
        if guess == num:
            if num == 10:
                print('**********************\n*    Correct Guess   *\n*  The Number =', num, '  *\n'
                                                                                              '**********************')
                break
            if num < 10:
                print('**********************\n*    Correct Guess   *\n*  The Number =', num, '   *\n'
                                                                                              '**********************')
                break
        else:
            if guess > num:
                remarks = 'high'
            else:
                remarks = 'low'
            print("Wrong number\nYour guess is too", remarks, "\nTry Again\n**********************\n")
            print("You have", 5 - tries, "left!")
            if tries == 4:
                # Last Try
                print("**********************\n***    LAST TRY    ***\n**********************")
        tries += 1
    else:
        # Game Over
        if num >= 10:
            print('**********************\n*      GAME OVER     *\n*  The Number =', num, '  *\n'
                                                                                          '**********************')

        if num < 10:
            print('**********************\n*      GAME OVER     *\n*  The Number =', num, '   *\n'
                                                                                          '**********************')

    # PLAY AGAIN OPTION
    play_again = input('\nDo you wanna try again:? \n<Y> Yes | <M> Menu | <Any key to exit> ')
    play_again = play_again.lower()
    if play_again in {'y', ' yes'}:
        print('**********************************')
        enterNum10()
    elif play_again in {'m', 'menu'}:
        print('Returning to menu')
        from Menu import menu
        menu()
    else:
        sys.exit(0)

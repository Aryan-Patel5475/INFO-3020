import random   # importing random module

# creating function to generate radnom functions
def random_card_generator():
    rand_num = random.randint(0, len(list) - 1)
    num = list[rand_num]
    list.pop(rand_num)

    return num

# creating function to simulate the game
def game():
    # assigning two card to user and computer, and adding them up
    user_num = random_card_generator() + random_card_generator()
    computer_num = random_card_generator() + random_card_generator()

    # displaying total of user first two card
    print('Your two hand total value is', user_num)

    # assigning 'y' to user choice so it will atleast loop one time
    user_choice = 'y'

    # looping until user keeps enetering 'y' or 'Y'
    while user_choice == 'y' or user_choice == 'Y':
        user_choice = input('Would you like to take another card? (y/n): ')

        # if user decided to play drawing one card and adding it to existing total of user
        if user_choice == 'y' or user_choice == 'Y':
            user_num += random_card_generator()

            # checking if user has gone BUST or not
            if user_num <= 21:
                print('Your hand now has total value of', user_num)
            else:
                print('You BUSTED with a total value of', user_num)
                print('\n ** You lose. **\n')
                return 0

    # Creating a variable to store random card
    num = random_card_generator()

    # if computer is below 21 draw another card and add it to computer
    while computer_num + num <= 21:
        computer_num += num
        num = random_card_generator()

    # displaying final value of user and computer hands
    print('You have stopped taking more cards with a hand value of', user_num)
    print('The dealer was dealt a had with a value of', computer_num)

    # checking is user won or not
    if user_num >= computer_num:
        print('\n** You Win! **\n')
    else:
        print('\n** You lose. **\n')

if __name__ == '__main__':
    # initializing list with all the available cards
    list = [1, 1, 1, 1, 2, 2, 2, 2,
            3, 3, 3, 3, 4, 4, 4, 4,
            5, 5, 5, 5, 6, 6, 6, 6,
            7, 7, 7, 7, 8, 8, 8, 8,
            9, 9, 9, 9, 10, 10, 10, 10]

    # simulating game one time atleast
    game()

    # assigning 'y' to choise so it will loop atleast one time
    choice = 'y'

    # looping until user decide to not play
    while choice == 'y' or choice == 'Y':
        # askign for user choice
        choice = input('Would you like to play again? (y/n): ')

        # playing the game or existing
        if choice == 'y' or choice == 'Y':
            # initializing list again so the desk dosen't get empty
            list = [1, 1, 1, 1, 2, 2, 2, 2,
                    3, 3, 3, 3, 4, 4, 4, 4,
                    5, 5, 5, 5, 6, 6, 6, 6,
                    7, 7, 7, 7, 8, 8, 8, 8,
                    9, 9, 9, 9, 10, 10, 10, 10]
            game()
        else:
            print('Thanks for playing!')
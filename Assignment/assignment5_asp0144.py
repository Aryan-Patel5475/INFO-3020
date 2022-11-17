import random

# function to take in list of card from a file and adding it into local list
def set_card_deck(card_deck):

    # clearing the deck
    card_deck.clear()

    # openign the file as read only
    file = open('cards.txt', 'r')

    # looping until end of the file is not reached
    for x in file:
        # storing line from the file in a string
        line_string = x
        # spliting the string and storing it into the list
        line_list = line_string.split(',')
        # adding the list to the card_deck list
        card_deck.append(line_list)

# function to deal cards
def deal_card(card_deck):

    # genereating random number between a given range
    # range decrease as card are drawn out of the deck
    rand_num = random.randint(0, len(card_deck) - 1)

    # storing the card value of the randomly selected card in a variable
    card_value = card_deck[rand_num][0]

    # poping the card out of deck so we don't draw it again
    card_deck.pop(rand_num)

    #returning integer value associated with the card value
    if card_value == 'Ace' or card_value == '1':
        return 1
    elif card_value == 'King' or card_value == 'Queen' or card_value == 'Jack':
        return 10
    else:
        return int(card_value)

# function to keep track of user score and computer score
def get_score(card_deck):

    # drawing two cards from user and computer and adding there value up
    user_score = deal_card(card_deck) + deal_card(card_deck)
    computer_score = deal_card(card_deck) + deal_card(card_deck)

    # printing out the user score after drawing two cards
    print('Your two hand total value is:', user_score)

    # asking if user would like to draw another card
    user_choice = input('Would you like to take another card? (y/n): ')

    # looping until user doesn't wanna draw any more card
    while user_choice == 'y' or user_choice == 'Y':
        # drawing another card and adding it into exisiting user score
        user_score += deal_card(card_deck)

        # if user score is less than 21 keep looping other wise exit the loop
        if user_score <= 21:
            print('Your hand now has total value of', user_score)
        else:
            return user_score, -1

        user_choice = input('Would you like to take another card? (y/n): ')

    # adding more cards to computer so it gets closer to 21
    # creating the variable to store the card value
    temp_num = deal_card(card_deck)

    # checking if adding temp variable into exisitng computer score would lead it to bust
    # if computer doesn't bust add the card value into computer score
    # else exit the loop
    while computer_score + temp_num <= 21:
        computer_score += temp_num
        temp_num = deal_card(card_deck)

    # printing out final value of user score and computer score
    print('You have stopped taking more cards with a hand value of', user_score)
    print('The dealer was dealt a hand with a value of', computer_score)

    # returning user score and computer score
    return user_score, computer_score

# main function
def main():

    # creating empty card deck
    card_deck = []

    # adding the cards into the empty deck
    set_card_deck(card_deck)

    user_choice = 'y'

    # looping until user doesn't decide to contine
    while user_choice == 'y' or user_choice == 'Y':

        #storing the result we get from get_score in local variable
        user_n, computer_n = get_score(card_deck)

        # if user score is above 21, then user busted and lost
        if user_n > 21:
            print('You BUSTED with a total value of', user_n)
            print('\n ** You lose. **\n')
        # if user score us less than computer score then print user lost
        elif user_n < computer_n:
            print('\n** You lose. **\n')
        # if user score is greater than computer score print user win
        elif user_n >= computer_n:
            print('\n** You Win! **\n')

        # reinitializing the deck, so it doesn't get empty
        set_card_deck(card_deck)

        # asking for user input again
        user_choice = input('Would you like to play again? (y/n): ')

    print('Thanks for playing!')

main()
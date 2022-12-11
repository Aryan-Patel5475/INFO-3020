# importing random module to pick out random card from the deck
import random

def set_card_deck(card_deck):

    # clearing the deck
    card_deck.clear()

    # opening the file as read only
    file = open('cards.txt', 'r')

    # looping until the end of the file is not reached
    for x in file:
        # storing line from the file in a string
        line_string = x
        # splitting the string and storing it into the list
        line_list = line_string.split(',')
        # adding the list to the card_deck list
        card_deck.append(line_list)

# function to deal cards
def deal_card(card_deck, scores, who):

    # generating random number between 0 and size of the deck
    rand_num = random.randint(0, len(card_deck) - 1)

    # storing the information about card in card
    card = card_deck[rand_num]
    # removing card from the deck as it's in play now
    card_deck.pop(rand_num)

    # if it's user then add card to his personal deck
    if who == 'user':
        scores['player']['cards'].append(card)
    # or else add it into dealer's personal deck
    else:
        scores['dealer']['cards'].append(card)

    # storing value of the card in num
    num = card[0]

    # checking what a value of card is and returning appropriate card value
    if num == 'Ace' or num == '1':
        return 1
    elif num == 'King' or num == 'Queen' or num == 'Jack':
        return 10
    else:
        return int(num)

# function to print out user cards
def show_card(scores):

    # setting i to 0
    i = 0
    # looping until the end of the player deck is not reached
    while (i < len(scores['player']['cards'])):
        # printing player card value and it's suit
        print(scores["player"]["cards"][i][0], scores["player"]["cards"][i][1], end='')
        # incrementing by 1
        i += 1

# function to keep track of the score
def get_score(card_deck, scores):

    # asking user choice
    user_choice = input('Would you like to take another card? (y/n): ')

    # looping until user says yes
    while user_choice == 'y' or user_choice == 'Y':

        # drawing one card for user and dealer
        scores["player"]["score"] += deal_card(card_deck, scores, 'user')
        scores["dealer"]["score"] += deal_card(card_deck, scores, 'dealer')

        # calling the show card function to print out user cards
        show_card(scores)
        print('Your hand total is', scores["player"]["score"])

        # if dealer total card value is over 21 then return to main function
        if scores["dealer"]["score"] > 21:
            return None
        # if user total card value is over 21 then return to main function
        elif scores["player"]["score"] > 21:
            return None

        # asking for the user input and if input is y then looping again
        user_choice = input('Would you like to take another card? (y/n): ')

    # printing out the total value of user cards and dealer card as by now they have both stop taking cards
    print('Your have stopped taking more cards with a hand value of', scores["player"]["score"])
    print('The dealer was dealt a hand with a value of', scores["dealer"]["score"])

    # returning user total card value and total dealer card value
    return None

# main function
def main():

    # declaring empty list
    card_deck = []

    # assigning user choice to y, so it will loop at least one time
    user_choice = 'y'

    # looping until user enters y
    while user_choice == 'y' or user_choice == 'Y':

        # empty dictionary
        scores = {"player": {"score": 0, "cards": []},
                  "dealer": {"score": 0, "cards": []}}

        # calling the set function to fill out empty deck
        set_card_deck(card_deck)

        # drawing two cards and adding it to player and dealer list
        scores["player"]["score"] += deal_card(card_deck, scores, 'user')
        scores["player"]["score"] += deal_card(card_deck, scores, 'user')
        scores["dealer"]["score"] += deal_card(card_deck, scores, 'dealer')
        scores["dealer"]["score"] += deal_card(card_deck, scores, 'dealer')

        # displaying user cards
        show_card(scores)

        # printing out sum of user card value after drawing two cards
        print('The sum of the first two cards is:', scores["player"]["score"])

        # calling get score function
        get_score(card_deck, scores)

        # if user total card value is above 21 print busted
        if scores["player"]["score"] > 21:
            print('You BUSTED with a total value of', scores["player"]["score"])
            print('\n** You lose. **\n')
        # if dealer total card value is above 21 print busted
        elif scores["dealer"]["score"] > 21:
            print('Dealer BUSTED with a total value of', scores["dealer"]["score"])
            print('\n** You Win! **\n')
        # if user total card value is less than dealer total card value print appropriate message
        elif scores["player"]["score"] < scores["dealer"]["score"]:
            print('\n** You lose. **\n')
        # if user total card value is greater than or equal to dealer total card value print appropriate message
        elif scores["player"]["score"] >= scores["dealer"]["score"]:
            print('\n** You Win! **\n')

        user_choice = input('Would you like to play again? (y/n): ')

    print('Thanks for playing!')

main()
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from replit import clear
from art import logo
from random import randint

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

dealer_hand, player_hand = [], []

players = {
    'dealer': dealer_hand,
    'player': player_hand,
}

game_over = False


def get_cards(how_many):
    return [cards[randint(0, (len(cards) - 1))] for _ in range(how_many)]


def deal_cards(to_who, amount):
    for who in to_who:
        card = get_cards(amount[to_who.index(who)])
        players[who].extend([card[0] - 10] if (card[0] == 11) and (calculate_score(players[who]) + card[0] > 21) else card)


def show_hands(state):
    if state == 'current':
        print('Your cards: {player_cards}, current score: {player_score}'.format(player_cards=player_hand, player_score=calculate_score(player_hand)))
        print('Computer\'s first card: {dealer_cards}'.format(dealer_cards=dealer_hand))
    elif state == 'final':
        print('Your final hand: {player_cards}, final score: {player_score}'.format(player_cards=player_hand, player_score=calculate_score(player_hand)))
        print('Computer\'s final hand: {dealer_cards}, final score: {dealer_score}'.format(dealer_cards=dealer_hand, dealer_score=calculate_score(dealer_hand)))


def calculate_score(hand):
    return sum(hand)


def reveal_the_winner():
    # Dealer wins: D = 17, P = 15 | D = 19, P = 22
    if (calculate_score(dealer_hand) > calculate_score(player_hand)) and (calculate_score(dealer_hand) <= 21):
        print('You lose 😤')
    elif (calculate_score(dealer_hand) < calculate_score(player_hand)) and (calculate_score(player_hand) > 21):
        print('You went over. You lose 😭')
    # Player wins: P = 17, P = 15 | P = 19, D = 22
    elif (calculate_score(player_hand) > calculate_score(dealer_hand)) and (calculate_score(player_hand) <= 21):
        print('You win 😃')
    elif (calculate_score(player_hand) < calculate_score(dealer_hand)) and (calculate_score(dealer_hand) > 21):
        print('Opponent went over. You win 😁')
    # Draw: D = 20 | P = 20
    else:
        print('Draw 🙃')


while input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ') == 'y':
    if (not dealer_hand) and (not player_hand):
        clear()
        print(logo)
        deal_cards(('dealer', 'player'), (1, 2))

    show_hands('current')

    while (not game_over) and (calculate_score(dealer_hand) < 21) and (calculate_score(player_hand) < 21):
        hit_me = input(f'Type \'y\' to get another card, type \'n\' to pass: ')

        if hit_me == 'y':
            deal_cards(('player', ), (1, ))

            if calculate_score(player_hand) < 21:
                show_hands('current')
        elif hit_me == 'n':
            while calculate_score(dealer_hand) < 17:
                deal_cards(('dealer', ), (1, ))
            else:
                game_over = True
    else:
        game_over = False

        show_hands('final')

        reveal_the_winner()

        dealer_hand, player_hand = [], []
        
        # ***************************
        players = {
            'dealer': dealer_hand,
            'player': player_hand,
        }
        # ***************************

        # dealer_hand.clear()
        # player_hand.clear()
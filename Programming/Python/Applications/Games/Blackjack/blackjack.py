from cards_list import cards
from logo import logo
import random
import os

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Returns a random card from the deck.
def deal():
    cards
    card = random.choice(cards)
    return card

# Take a list of cards, then return the score from the cards.
def cal_score(cards):
    # check for a blackjack, then return 0.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # replace the ace, if score is > 21.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# If you and the ai are both over, you lose.
# if AI and player have same score, then it's a draw.
# if player has blackjack, then player wins.
# if AI has blackjack, the player loses.
def compare(player_score, ai_score):
    if player_score > 21 and ai_score > 21:
        return "You went over. You lose!"
    
    if player_score == ai_score:
        return "Draw"
    
    elif ai_score == 0:
        return "AI has blackjack. You lose!"
    
    elif player_score == 0:
        return "You have blackjack. You Win!"
    
    elif player_score > 21:
        return "You went over. You lose!"
    
    elif ai_score > 21:
        return "AI went over. You Win!"
    
    elif player_score > ai_score:
        return "You Win!"
    
    else:
        return "You lose!"

def play():
    print(logo)

    player_cards = []
    ai_cards = []
    is_game_end = False
    
    for _ in range(2):
        player_cards.append(deal())
        ai_cards.append(deal())
        
# score needs to be rechecked with every new card drawn, and repeats until game ends.
# id ai or player has blackjack or if player gets over 21, gaame ends.
    while not is_game_end:
        player_score = cal_score(player_cards)
        ai_score = cal_score(ai_cards)
        
        print(f"Your cards: {player_cards}\nYour score: {player_score}")
        print(f"AI's 1st card: {ai_cards[0]}")
        
        # if player wants to draw another card, continue game.
        # if not, end game.
        if player_score == 0 or ai_score == 0 or player_score > 21:
            is_game_end = True
        else:
            draw_another = input("Draw another card? y/n: ")
            if draw_another == 'y':
                player_cards.append(deal())
            else:
                is_game_end = True
    
    # Once player is finished, the AI plays.
    # AI keeps drawing cards as long as it scores less than 17.
    while ai_score != 0 and ai_score < 17:
        ai_cards.append(deal())
        ai_score = cal_score(ai_cards)
        
    print(f"Final card: {player_cards}\nFinal score: {player_score}")
    print(f"AI's final card: {ai_cards}\nAI's final score: {ai_score}")
    print(compare(player_score, ai_score))
    
# If player wish to restart game, clear console to play new game.
# If not, print out ending greeting.
while input("Play blackjack? y/n: ") == 'y':
    clear()
    play()








































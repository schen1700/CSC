from rps_art import rock, paper, scissors
import random

gamePlay = [rock, paper, scissors]

start = input("Start game? y/n: ")
if start == 'y':   
    # Lets player enter a choice
    player_choice = int(input("Which one would you throw?\n0: Rock\n1: Paper\n2: Scissors\n\nEnter choice: "))
    
    if player_choice >= 3 or player_choice < 0:
        print("Invalid key! ")
        player_choice = int(input("0: Rock\n1: Paper\n2: Scissors\n\nPlease enter valid key: "))
    else:
        print(gamePlay[player_choice])
    
    # AI throws random choice
    ai_choice = random.randint(0, 2)
    print("Computer throws: ")
    print(gamePlay[ai_choice])
    
    # Conditional Statements
    if player_choice == 0 and ai_choice == 2:
        print("You Win!")
    
    elif ai_choice == 0 and player_choice == 3:
        print("AI Wins, You lose!")
        
    elif ai_choice > player_choice:
        print("AI Wins, You lose!")
        
    elif player_choice > ai_choice:
        print("You Win!")
        
    elif ai_choice == player_choice:
        print("It is a draw!")
else:
    print("Thank you, See you later!")

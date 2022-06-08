### Hangman
import random
from hangman_words import word_list
from hangman_stage import stages, logo

blanks = []

#TODO 1: Start the game, then generate random words from lists, assign to a variable.
print(logo)
player_lives = len(stages) - 1
end_game = False

def start_game():
    print()   
start_game()
play = input("Play Game? y/n: ")
    
chosen = random.choice(word_list)

for _ in range(len(chosen)):
    blanks += "_"
   
while not end_game:
    if play == 'y':   
        #TODO 2: Ask the user to guess a letter and assign their guessed letter to a variables.
        guess_letter = input("Guess a letter: ").lower()
        
        if guess_letter in blanks:
            print("\nYou've already guessed this letter!")
        
        #TODO 3: Check if the letter is one of the letter in the chosen word.
        for position in range(len(chosen)):
            letter = chosen[position]
            if letter == guess_letter:
                blanks[position] = letter
                
        #TODO 4: Check if user guessed the letters.
        if guess_letter not in chosen:
            print(f"\n{guess_letter} is not in the word. -1 life.")
            player_lives -= 1
            if player_lives == 0:
                end_game = True
                print(f"\nYou lose! The word is {chosen}.")
                
        print(f"{' '.join(blanks)}")
        if "_" not in blanks:
            end_game = True
            print("\nYou win!")
            
        #TODO 5: Check corresponding numbers of stages of lives remaining.
        print(stages[player_lives])
        
    else:
       print("Thank you for playing Hangman.\nHave a great day!")
       break
       
       
       
       
       
       
       
       
       
       
       
       
       
       
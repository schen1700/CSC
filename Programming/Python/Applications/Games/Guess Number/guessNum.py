import random

# sets difficulty level
normal_level = 10
hard_level = 5

print("Guess a number between 1 - 50.")
# Ask user to start game
def startGame():
    print()
startGame()
start = input("Start game? y/n: ")

if start == 'y':     
    # sets level to its difficulty
    def setDiff():
        level = int(input("Pick a level:\n1: Normal\n2: Hard\n= "))
        if level == 1:
            return normal_level
        else:
            return hard_level
        
    # check user's guess
    def checkUser(guess, answer, attempts):
        if guess > answer:
            print("too high! ")
            return attempts - 1
        elif guess < answer:
            print("too low!")
            return attempts - 1
        else:
            print(f"You got it! The answer was {answer}")
    
    # Generates a random integer number (1, 50)
    def playGame():
        answer = random.randint(1, 50)
        
        attempts = setDiff()
        guess = 0
        while guess != answer:
            print(f"You have {attempts} left to guess.")
            
            # user guess a number
            guess = int(input("Guess a number: "))
            
            # Track attempts
            attempts = checkUser(guess, answer, attempts)
            if attempts == 0:
                print("You run out of attempts!")
                print(f"{answer} is the right answer!")
                return
            elif guess != answer:
                print("Try again.")
                
    playGame()

else:
    print("Thank you, see you again!")
## this app allows multiple digits to operate.
from calc_art import calculator_art
import os

print(calculator_art)
print("Welcome, this calculator can calculate multiple numbers.")

# If Machine is running on Windows, use cls
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# ask the player to start game
def start():
    print()
start()
begin = input("Start Calculation? y/n: ")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y

if begin == 'y':
    # Lets user choose one among these operators.
    operators = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "%": modulo
        }
    
    def calculator():
        n1 = float(input("Enter first number: "))
        
        for number in operators:
            print(number)
        continue_cal = True
        
        while continue_cal:
            num_operation = input("Choose an operation: ")
            n2 = float(input("Enter second number: "))
            
            calculation = operators[num_operation]
            result = calculation(n1, n2)
            print(f"{n1} {num_operation} {n2} =  {round(result, 2)}")
            
            # Lets user continue to calculate.
            if input(f"Continue calculation? y/n: ") == 'y':
                n1 = result
            else:
                continue_cal = False
                clear()
                calculator()
    calculator()

else:
    print("See you later!")  
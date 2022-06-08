# A Simple Calculator in Python
# Adding two numbers
def add(x, y):
    return x + y

# Subtracting two numbers
def subtract(x, y):
    return x - y

# Multiply two numbers
def multiply(x, y):
    return x * y

# Divide two numbers
def divide(x, y):
    return y / x

# Options to choose from
def menu():
    print()

# prints a welcoming message
print("\nWelcome! This is a Basic Calculator in Python");

# Prompt user to choose an operator
menu()
option = input("Select an operation:\n" \
               "1: Addition\n" \
               "2: Subtraction\n" \
               "3: Multiplication\n" \
               "4: Division\n")
    
# Take input from user
while True:
    if option in ('1', '2', '3', '4'):
        num_x = int(input("Enter First Number: "))
        num_y = int(input("Enter Second Number: "))

        if option == '1':
            print(num_x, " + ", num_y, " = ",
                  add(num_x, num_y))

        elif option == '2':
            print(num_x, " - ", num_y, " = ",
                  subtract(num_x, num_y))

        elif option == '3':
            print(num_x, " * ", num_y, " = ",
                  multiply(num_x, num_y))

        elif option == '4':
            print(num_y, " / ", num_x, " = ",
                  divide(num_x, num_y))
            
        # Choose operator from the menu to continue forward 
        # with the calculations
        again_cal = input("\nCalculate again (y / n)? ")
        
        if again_cal == 'y':
            menu()
            option = input("Enter key to select an operator: ")
            
        elif again_cal == 'n':
            print("Thank you, See you again later...")
            break
        
        else:
            again_cal = input("Enter Valid key y/n: ")
            menu()
            option = input("Enter key to select an operator: ")
            
        
    # Invalid if wrong key   
    else:
        menu()
        option = input("Invalid Key!\n" \
                       "Please select the correct key: ")

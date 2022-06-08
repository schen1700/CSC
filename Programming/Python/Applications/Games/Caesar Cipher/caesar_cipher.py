### Caesar Cipher
from cc_alphabet import alphabet

#TODO 1: Define the functions into a single unit.
def caesar_cipher(begin_text, shift_amt, cipher_code):
    end_text = ""
    if cipher_code == 2:
        shift_amt *= -1
    for letter in begin_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amt
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"{end_text}")

#TODO 2: Ask user to encode and decode again.
again = True
while again:
    #TODO 3: Prine out statements with inputs to prompt users.
    code = int(input("Choose from options:\n1: Encode\n2: Decode\n"))
    text = input("Input your message: \n")
    shift = int(input("Input your shift number: \n"))
    
    #TODO 4: Enter a shift with a greater number.
    shift = shift % 26
    
    #TODO 5: Call the functions with a keyword parameter.
    caesar_cipher(begin_text = text, shift_amt = shift, cipher_code = code)
    
    run_again = input("Encode and Decode again? y/n: ")
    if run_again == 'n':
        again = False
        print("Thank you, see you again!")
  
    
    
    
    
    
    
    
    
    
    
    
    
    
#Password Generator Project
import random
from random_item import item_randomly

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
print('Use this tool to create an strong password for each of your internet logins.\n')

while True:
  while True:
    try:
      nr_letters= int(input("How many letters would you like in your password?\n")) 
      nr_symbols = int(input(f"How many symbols would you like?\n"))
      nr_numbers = int(input(f"How many numbers would you like?\n"))
        
        
      op1 = item_randomly(nr_letters, letters)
      op2 = item_randomly(nr_symbols, symbols)
      op3 = item_randomly(nr_numbers, numbers)
      ops = op1 + op2 + op3
          
      #Eazy Level - Order not randomised:
      #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
      ez_password = ''.join(ops)
          
      #Hard Level - Order of characters randomised:
      #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
      random.seed(random.randint(0, 99999))
      hd_password = ''.join(random.sample(ez_password, len(ez_password)))
          
      #print(ez_password)
      print(hd_password)
      break
    
    except ValueError:
        print('Plese, type a number.\n')
      
  again = input('Do you want to generate another password? (Y/N)\n').lower()
  if again == 'n':
    print('\nThanks for using the tool. \nWe hope to see you again. \nBye!!')
    break
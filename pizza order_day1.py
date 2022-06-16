print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

total = 0

#toppings
if extra_cheese.upper() == 'Y':
    total += 1

if add_pepperoni.upper() == 'Y':
    if size.upper() in ['M', 'L']:
        total += 3 
    else:
        total += 2 
        
#size
size_dict = {'S':15, 'M':20, 'L':25}
if size.upper() in size_dict.keys():
    total += int(size_dict[size.upper()])

print(f'Your final bill is: ${total}.')

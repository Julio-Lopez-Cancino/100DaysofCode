from counter import get_var_value

welcome = 'Welcome to the Tip Calculator.'
print('*' * (len(welcome)), sep = '')
print('\n')
print(welcome)
print('\n')
print('*' * len(welcome), sep = '')
print('\n')

total = float(input('What was the total bill?\n'))
people = float(input('How many people to split the bill?\n'))
percentage = int(input('What percentage tip would you like to give? 10, 12, or 15?\n')) / 100

split = total / people
tip_each = split * (1 + percentage)

msg_result = f'Each person should pay: ${round(tip_each, 2)}'
print(msg_result, sep='\n\n')

print('Thank you for using the tip calculator!')

counter = get_var_value()

print(f'You\'re the {counter} using the tip calculator 😊✌️')

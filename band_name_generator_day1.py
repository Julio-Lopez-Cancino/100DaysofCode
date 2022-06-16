var1 = 'Welcome to the Band Name Generator\n'
var2 = 'Press q to terminate the program\n'

while True:
    print(var1)
    print(var2)
    
    city = input('What\'s name of the city you grew up in?\n')
    if city == 'q':
        check = input('Do you want to terminate the program? (Y/N)\n')
        if check.lower() == 'y':
            print('Bye!')
            break
        
    name = input('What\'s your pet\'s name?\n')
    if name == 'q':
        check = input('Do you want to terminate the program? (Y/N)\n')
        if check.lower() == 'y':
            print('Bye!')
            break
        
    var3 = f'Your band name could be {city} {name}'
    print(var3)

    again = input('Do you want to try again? (Y/N)\n')
    if again.lower() == 'n':
        print('Bye!')
        break

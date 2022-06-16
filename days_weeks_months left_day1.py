while True:
    try:
        #user age
        age = float(input("What is your current age?\n"))
        #life expectation
        life_limit = 90
        years_left = life_limit - age
        #days left
        x = 365 * years_left
        #weeks left
        y = 52 * years_left
        #months left
        z = 12 * years_left

        print(f'You have {round(x)} days, {round(y)} weeks, and {round(z)} months left.')
        break

    except:
        print('Please, type a number!')

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Function to count the letter of True and Love in the names
def check_love(a, b):
    c = a.lower() + b.lower()
    in_true = ['t', 'r', 'u', 'e']
    in_love = ['l', 'o', 'v', 'e']
    num1 = 0
    num2 = 0
    for x in in_true:
        if x in c:
            num1 += c.count(x)
    for x in in_love:
        if x in c:
            num2 += c.count(x)
    return str(num1) + str(num2)

#pass the names to the fucntion to calculate the score
score = int(check_love(name1, name2))

#messages for the score
x = f'Your score is {score}, you go together like coke and mentos.'
y = f'Your score is {score}, you are alright together.'
z = f'Your score is {score}.'

#validating and printing score
if score < 10 or score > 90:
    print(x)
elif score >= 40 and score <= 50:
    print(y)
else:
    print(z)





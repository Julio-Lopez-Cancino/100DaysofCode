import random
import time
from decision import decision

choice = {
  0 : '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  ''',

  1 : '''
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
  ''',
  
  2 : '''
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  '''
}

print('Welcome to Rock-Paper-Scissor game!! \nTest your luck, and play against the Matrix')

print('\nOn \"shoot\" type 0 for Rock, 1 for Paper or 2 for Scissors...')

while True:
  
  while True:
    a = input('\nAre you ready?? (Y/N) \n').lower()
    if a == 'y':
      break
    else:
      time.sleep(2)
      continue
  
  try:
    player = int(input('\nrock, paper, scissors, shoot!\n'))
    random.seed(random.randint(0,99999))
    matrix = random.randint(0,2)
  
    print(f'\n{choice[player]}')
    print('\nMatrix chose:')
    print(f'\n{choice[matrix]}')
    
    game = decision(player, matrix)
    print(f'\n{game}')
  
  except ValueError:
    print('\nRemember type 0 for Rock, 1 for Paper or 2 for Scissor...')

  again = input('\nPlay again? (Y/N)\n').lower()
  if again != 'y':
    print('\nGood game!! Bye...\n')
    break
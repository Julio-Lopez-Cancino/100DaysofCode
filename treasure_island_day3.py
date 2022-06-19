banner = '''
   _                                     _     _                 _ 
  | |                                   (_)   | |               | |
  | |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
  | __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
  | |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
   \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |___~start~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\\
 \_/__________________________________________________________________/
'''
print('*' * 70)
print('\n')
print(banner)
print('\n')
print('*' * 70)

print('Welcome to Treasure Island. \n\nYour mission is to find the treasure. \nChoose wisely 🦉')

print('\nYou just reached the shore. Among all those trees you glimpse two separte paths...')

while True:

  a = input('\nDo you want go left or right?\n')
  if a.lower() == 'right':
    print('You fall into a hole 🕳️ ... \nGame Over 💀')
    break 
  elif a.lower() == 'left':
    print('...')
    #break
  else:
    print('\nOpps!!!')
    print('Right or Left? 🤔\n')
    continue
  
  print('\nAfter a long walk, you got stuck in front of a lake... you can simply swin or wait until you build a raft...')
  while True:
    b = input('\nDo you want to swin or wait?\n')
    if b.lower() == 'swin':
      print('Gash!! You were attacked by trouts 🐟🐠  ... \nGame Over 💀')
      break
    elif b.lower() == 'wait':
      print('...')
      break
    else:
      print('\nOpps!!!')
      print('Swin or Wait? 🤔\n')
      continue

  while True:
    print('\nShack ahoy!! but ain\'t going to be easy peasy... there are no windows, just three doors...')

    c = input('\nWhich door will you choose? Red, Yellow, or Blue?\n')
    if c.lower() == 'red':
      print('\nBurned by fire 🔥🔥🔥 ... \nGame over 💀')
      break
    elif c.lower() == 'blue':
      print('\nEaten by beasts 🦖🦖... \nGame over 💀')
      break
    elif c.lower() == 'yellow':
      print('\nYou found it!!! 💰💰💰 \nWell done 👏👏... \nYou win 🎈🎊🎉🎊🎈')
      break
    else:
      print('\n... \nGame over 💀')
      break
  
  break
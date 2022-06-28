# from replit import clear  # uncomment in case the replit module is installed.
import random
from hangman_art import stages, logo
from hangman_words import word_list


random.seed(random.randint(0, 99999))
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(f'{logo}\n')

display = ['_' for letter in chosen_word]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # clear the screen for having a better user experience
    # clear()

    # Check if letter has been guessed already.
    if guess in display:
        print(f'You\'ve already guessed {guess}')

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(
            f'You guessed {guess}, that\'s not in the word. You lose a life.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    if end_of_game == True and '_' in display:
        print(f'The word was: {chosen_word}.')

    print(stages[lives])

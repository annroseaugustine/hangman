
from string import ascii_lowercase
from words import get_random_word

def get_num_attempts():
	#write code here

def get_min_word_length():
	#write code here 

def get_display_word(word, idxs):
	#write code here

def get_next_letter(remaining_letters):
	#write code here

def play_hangman():
	print('Starting a game of Hangman...')
    	attempts_remaining = get_num_attempts()
    	min_word_length = get_min_word_length()

    	# Randomly select a word
    	print('Selecting a word...')
    	word = get_random_word(min_word_length)
    	print()

    	# Initialize game state variables
    	idxs = [letter not in ascii_lowercase for letter in word]
    	remaining_letters = set(ascii_lowercase)
    	wrong_letters = []
    	word_solved = False

    	# Main game loop
    	while attempts_remaining > 0 and not word_solved:
        	# Print current game state
        	print('Word: {0}'.format(get_display_word(word, idxs)))
        	print('Attempts Remaining: {0}'.format(attempts_remaining))
        	print('Previous Guesses: {0}'.format(' '.join(wrong_letters)))

        # Get player's next letter guess
        next_letter = get_next_letter(remaining_letters)

        # Check if letter guess is in word
        if next_letter in word:
            # Guessed correctly
            print('{0} is in the word!'.format(next_letter))

            # Reveal matching letters
            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            # Guessed incorrectly
            print('{0} is NOT in the word!'.format(next_letter))

            # Decrement num of attempts left and append guess to wrong guesses
            attempts_remaining -= 1
            wrong_letters.append(next_letter)

        # Check if word is completely solved
        if False not in idxs:
            word_solved = True
        print()

    # The game is over: reveal the word
    print('The word is {0}'.format(word))

    # Notify player of victory or defeat
    if word_solved:
        print('Congratulations! You won!')
    else:
        print('Try again next time!')

    # Ask player if he/she wants to try again
    try_again = input('Would you like to try again? [y/Y] ')
    return try_again.lower() == 'y'

if __name__ == '__main__':
	#write code here



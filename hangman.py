
from string import ascii_lowercase
from words import get_random_word

def get_num_attempts():
	#write code here

def get_min_word_length():
	#write code here 

def get_display_word(word, idxs):
	#write code here

def get_next_letter(remaining_letters):
	"""Get the user-inputted next letter."""
    if len(remaining_letters) == 0:
        raise ValueError('There are no remaining letters')
    while True:
        next_letter = input('Choose the next letter: ').lower()
        if len(next_letter) != 1:
            print('{0} is not a single character'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print('{0} is not a letter'.format(next_letter))
        elif next_letter not in remaining_letters:
            print('{0} has been guessed before'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter

def play_hangman():
	#write code here

if __name__ == '__main__':
	#write code here



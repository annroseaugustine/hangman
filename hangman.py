
from string import ascii_lowercase
from words import get_random_word

def get_num_attempts():
	#write code here

def get_min_word_length():
	while True:
		min_word_length=input("Enter the minimum word length [4-16] : ")
		try:
			min_word_length=int(min_word_length)
			if 4<=min_word_length<=16 :
				return min_word_length
			else:
				print("{0} is not in the range 4-16".format(min_word_length))
		except ValueError:
			print("{0} is not an integer between 4 and 16".format(min_word_length))

			

def get_display_word(word, idxs):
	"""Get the word suitable for display."""
    if len(word) != len(idxs):
        raise ValueError('Word length and indices length are not the same')
    displayed_word = ''.join(
        [letter if idxs[i] else '*' for i, letter in enumerate(word)])
    return displayed_word.strip()

def get_next_letter(remaining_letters):
	#write code here

def play_hangman():
	#write code here

if __name__ == '__main__':
	#write code here



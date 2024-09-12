#!/usr/bin/env python3

import string

def get_available_letters(letters_guessed):
		"""
		letters_guessed: list, what letters have been guessed so far
		returns: string, comprised of letters that represents what letters have not
			yet been guessed.
		"""
		available = ""
		for letter in string.ascii_lowercase:
				if letter not in letters_guessed:
						available += letter
		return available

def is_word_guessed(secret_word, letters_guessed):
		"""
		secret_word: string, the word the user is guessing
		letters_guessed: list, what letters have been guessed so far
		returns: boolean, True if all the letters of secret_word are in letters_guessed;
			False otherwise
		"""
		for c in secret_word:
				if c not in letters_guessed:
						return False
		return True


def get_guessed_word(secret_word, letters_guessed):
		"""
		secret_word: string, the word the user is guessing
		letters_guessed: list, what letters have been guessed so far
		returns: string, comprised of letters and underscores that represents
			what letters in secret_word have been guessed so far.
		"""
		guessed_so_far = ""
		for c in secret_word:
				if c in letters_guessed:
						guessed_so_far += c
				else:
						guessed_so_far += " _ "
		return guessed_so_far


def hangman(letters_guessed):
		"""
		letters_guessed: list, what letters have been guessed so far
		returns: string, comprised of letters that represents what letters have not
			yet been guessed.
		"""
		available = ""
		for letter in string.ascii_lowercase:
				if letter not in letters_guessed:
						available += letter
		return available


def hangman(secret_word):
	print("Welcome to the game, Hangman!")
	print(f"I am thinking of a word that is {len(secret_word)} letters long.")
	print("-------------")
	
	letters_guessed = []
	nr_of_guesses = 8
	mistakes_made = 0
	
	while mistakes_made < nr_of_guesses:
		print(f"You have {nr_of_guesses - mistakes_made} guesses left.")
		available_letters = get_available_letters(letters_guessed)
		print("Available letters:", available_letters)
		guessed = input("Please guess a letter: ").lower()
		
		if len(guessed) == 1 and guessed in string.ascii_lowercase:
			if guessed in letters_guessed:
				print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
			elif guessed not in secret_word:
				print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
				mistakes_made += 1
				letters_guessed.append(guessed)
			else:
				letters_guessed.append(guessed)
				print("Good guess:", get_guessed_word(secret_word, letters_guessed))
				if is_word_guessed(secret_word, letters_guessed):
					print("-------------")
					print("Congratulations, you won!")
					break
		else:
			print("Invalid input, please enter a single letter.")
			
		print("-------------")
		
	if mistakes_made == nr_of_guesses:
		print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
		
# For testing purposes. Remove for submit
if __name__ == "__main__":
	secret_word = "python"
	hangman(secret_word)
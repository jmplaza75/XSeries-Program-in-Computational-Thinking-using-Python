#!/usr/bin/env python3

class Message(object):
	def __init__(self, text):
		self.message_text = text
		self.valid_words = load_words(WORDLIST_FILENAME)
		
	def get_message_text(self):
		return self.message_text
	
	def get_valid_words(self):
		return self.valid_words[:]
	
	def build_shift_dict(self, shift):
		self.shiftDict = {}
		for i in range(len(string.ascii_lowercase)):
			if i <= 25 - shift:
				self.shiftDict[string.ascii_lowercase[i]] = string.ascii_lowercase[i + shift]
				self.shiftDict[string.ascii_uppercase[i]] = string.ascii_uppercase[i + shift]
			else:
				self.shiftDict[string.ascii_lowercase[i]] = string.ascii_lowercase[i -26 + shift]
				self.shiftDict[string.ascii_uppercase[i]] = string.ascii_uppercase[i -26 + shift]
				
		return self.shiftDict
	
	
	def apply_shift(self, shift):
		
		self.list = []
		for char in self.message_text:
			try:
				self.list.append(self.build_shift_dict(shift)[char])
			except:
				self.list.append(char)
				
		return ''.join(self.list)
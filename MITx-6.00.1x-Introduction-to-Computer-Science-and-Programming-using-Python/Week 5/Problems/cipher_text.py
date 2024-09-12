#!/usr/bin/env python3

class CiphertextMessage(Message):
	def __init__(self, text):
		Message.__init__(self, text)
		
	def decrypt_message(self):
		count = 0
		bestShift = 0
		for shift in range(26):
			self.build_shift_dict(shift)
			self.apply_shift(shift)
			validWordCount = 0
			for word in self.apply_shift(shift).split(' '):
				if  word in self.valid_words:
					validWordCount += 1
			if validWordCount > count:
				count = validWordCount
				bestShift = shift
		return (bestShift, self.apply_shift(bestShift))     
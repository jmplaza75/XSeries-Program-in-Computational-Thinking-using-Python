#!/usr/bin/env python3

class PlaintextMessage(Message):
	def __init__(self, text, shift):
		Message.__init__(self, text)
		self.shift = shift
		self.encrypting_dict = self.build_shift_dict(shift)
		self.message_text_encrypted = self.apply_shift(shift)
		
	def get_shift(self):
		return self.shift
	
	def get_encrypting_dict(self):
		self.encrypting_dict_copy = self.encrypting_dict.copy()
		return self.encrypting_dict_copy
	
	def get_message_text_encrypted(self):
		return self.message_text_encrypted
	
	def change_shift(self, shift):
		self.shift = shift
		self.encrypting_dict = self.build_shift_dict(shift)
		self.message_text_encrypted = self.apply_shift(shift)
#!/usr/bin/env python3

class vowels:
	def __init__(self, word):
		self.word = word
		self.i = 0
		self.i_max = len(word)
	def __iter__(self): 
		self.letter = self.word[self.i]
		return self 
	def __next__(self):
		while 1:
			self.i = self.i + 1
			if self.i == self.i_max:
				raise StopIteration()
			l =  self.word[self.i]
			vowels = ['a','e','i','o','u']			
			if l in vowels:
				break	
		return self.word[self.i]
                

for i in vowels("Johanna"):
    print(i) 

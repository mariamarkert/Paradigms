#!/usr/bin/env python3

import sys


# Your iterator implementation here
class move_robot:
	def __init__(self, moves):

		self.x = 0
		self.y = 5
		self.dx = 5
		self.dy = -5
		self.counter = -1
		self.moves = moves
	
	def __iter__(self):

		return self

	def __next__(self): 
		
		self.counter += 1

		if self.counter <= self.moves:

			if self.counter % 2 or self.counter ==0 :

				self.y = self.y + self.dy
				self.dy = self.dy * -1

			else:

				self.x = self.x + self.dx
				self.dx = self.dx * -1
			
			return [self.x, self.y]

		raise StopIteration

# Keep the lines below
def main():
	n = int(sys.argv[1])
	for v in move_robot(n):
		print(v)

if __name__ == '__main__':
	main()

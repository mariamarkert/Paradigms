#!/usr/bin/env python3

import sys

# Your generator implementation here
def move_robot(value):
	x = 0
	y = 0
	dx = 5
	dy = 5
	m_counter = 0
	yield [x,y]
	while m_counter < value:
		m_counter +=1
		if m_counter % 2:
			y = y + dy
			dy = -1 * dy
		else:
			x = x + dx
			dx = -1 * dx
		
		yield [x,y]
		



# Keep the lines below
def main():
	n = int(sys.argv[1])
	for v in move_robot(n):
		print(v)

if __name__ == '__main__':
	main()

#!/usr/bin/env python3
import math

class Point:

	def __init__(self, x,y):
		
		self.x = x
		self.y = y

	def print(self):
		print("(",self.x,",",self.y,")")

	def __gt__(self, other):
		r1 = math.sqrt(self.x * self.x + self.y * self.y)
		r2 = math.sqrt(other.x * other.x + other.y * other.y)
		if r1 > r2: return True
		else: return False

	def __ge__(self, other):
		r1 = math.sqrt(self.x * self.x + self.y * self.y)
		r2 = math.sqrt(other.x * other.x + other.y * other.y)
		if r1 >= r2: return True
		else: return False

	def __eq__(self, other):
		r1 = math.sqrt(self.x * self.x + self.y * self.y)
		r2 = math.sqrt(other.x * other.x + other.y * other.y)
		if r1 == r2: return True
		else: return False

	def __lt__(self, other):
		r1 = math.sqrt(self.x * self.x + self.y * self.y)
		r2 = math.sqrt(other.x * other.x + other.y * other.y)
		if r1 < r2: return True
		else: return False

	def __le__(self, other):
		r1 = math.sqrt(self.x * self.x + self.y * self.y)
		r2 = math.sqrt(other.x * other.x + other.y * other.y)
		if r1 <= r2: return True
		else: return False


p1 = Point(2,3)  
p2 = Point(-3,1) 
p3 = Point(-2,-3)
print(p1 > p2) 
print( True) # p1 is more distant to the origin than p2
print(p1 == p2)
print( False) # p1 and p2 are not equally distant to the origin 
print(p1 < p2)
print( False) # p1 is not closer to the origin as compared to p2
print(p1 == p3)
print( True )# p1 and p3 are equally distant to the origini	
p1.print()

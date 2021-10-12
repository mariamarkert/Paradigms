#!/usr/bin/env python3

#def main():
	# your logic
	# you're welcome to breakdown your code into functions or classes


from tkinter import * 
root = Tk()
wd = 400
ht = 300
canvas = Canvas(root, width=wd, height=ht)
canvas.pack()
r_length = 15
r_height = 15


class Rectangle():
	def __init__(self):
		self.x1 = int((wd/2) - (r_length/2))
		self.x2 = int((wd/2) + (r_length/2))
		self.y1 = int((ht/2) - (r_height/2))
		self.y2 = int((ht/2) + (r_height/2))
		self.fill = 'blue'
		self.item = canvas.create_rectangle(self.x1, self.y1,self.x2,self.y2, fill = self.fill)
		canvas.bind("<Button-1>", self.change_color)
		root.bind('<Left>', self.left)
		root.bind('<Right>', self.right)
		root.bind('<Up>', self.up)
		root.bind('<Down>', self.down)
		canvas.pack()
		

	def change_color(self, event):
		if self.fill == 'blue':
			self.fill = 'green'
		else:
			self.fill = 'blue'
		canvas.itemconfig(self.item, fill = self.fill)	
	
	def left(self, event):	
		[x1, y1, x2, y2] = canvas.coords(self.item)
		if x1 -5 >= 0:	
			canvas.move(self.item, -5, 0)

	def right(self, event):
		[x1, y1, x2, y2] = canvas.coords(self.item)
		if x2 + 5 <= wd:
			canvas.move(self.item, 5, 0)

	def up(self, event):
		[x1, y1, x2, y2] = canvas.coords(self.item)
		if y1-5 >= 0:	
			canvas.move(self.item, 0, -5)

	def down(self, event):
		[x1, y1, x2, y2] = canvas.coords(self.item)
		if y2 + 5 <= ht:
			canvas.move(self.item, 0, 5)

		

# Get an instance of the MouseMover object
rr = Rectangle()
#mm = MouseMover()

root.mainloop()

#if __name__ == '__main__':
#	main()


from tkinter import *

root = Tk()


colours = ["#ff0000", "#ff7d00", "#ffff00", "#00ff00", "#007dff", "#0000ff", "#7d00ff"]
name_colour = ["Красный", "Оражневый", "Желтый", "Зеленый", "Голубой", "Cиний", "Филолетовый"]

button = [None] * 7
def seven_colours(colours):
	# for i in range (7):
	button[0] = Button(root, bg = colours[0], height = "1", width = "30", command = lambda: text_adder(0))
	button[0].pack()

	button[1] = Button(root, bg = colours[1], height = "1", width = "30", command = lambda: text_adder(1))
	button[1].pack()

	button[2] = Button(root, bg = colours[2], height = "1", width = "30", command = lambda: text_adder(2))
	button[2].pack()

	button[3] = Button(root, bg = colours[3], height = "1", width = "30", command = lambda: text_adder(3))
	button[3].pack()

	button[4] = Button(root, bg = colours[4], height = "1", width = "30", command = lambda: text_adder(4))
	button[4].pack()

	button[5] = Button(root, bg = colours[5], height = "1", width = "30", command = lambda: text_adder(5))
	button[5].pack()

	button[6] = Button(root, bg = colours[6], height = "1", width = "30", command = lambda: text_adder(6))
	button[6].pack()

		
def text_adder(number):
	textin.delete(0, END)
	textin.insert(0, colours[number])
	textout.configure(text= name_colour[number])

def create_all():
	global textin, textout
	textout = Label(root, height = "2" ,width = "20")
	textout.pack()
	textin = Entry(root,  width = "36", justify = CENTER)
	textin.pack()
	seven_colours(colours)







create_all()

root.mainloop()
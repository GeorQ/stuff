from tkinter import *
from random import randint 
def create_arc(start, end, colour):
	xy = 50,50,500,500
	return canvas.create_arc(xy, start = start, extent = end, fill = colour)

 
	pass
def create_gui():
	light_colour = ['#ffcccb', '#add8e6', '#90ee90', '#ffffed']
	for i in range(4):
		arc.append(create_arc(i * 90 , 90, light_colour[i]))
	
	global text, score_text 
	text = canvas.create_text(700, 275, fill = "white", font = "Times 20 italic bold", text = "Get Ready !!!")
	score_text = canvas.create_text(900, 20, fill = "white", font = "Times 20 italic bold", text = "Score: 0 ")
	canvas.pack()

def flash_loop(flash_count):
	flash_count -= 1
	r = randint (0,3)
	seq_list.append(r)
	canvas.after(1000, light_arc, r)

def light_arc(r):
	colour = ['red', 'blue', 'green', 'yellow']
	canvas.itemconfigure(arc[r], fill = colour[r])
	canvas.after(500, dim_arc, r) 

def dim_arc(r):
	colour = ['#ffcccb', '#add8e6', '#90ee90', '#ffffed']
	canvas.itemconfigure(arc[r], fill = colour[r])
	
score = 0 
score_text = None
text = None

window = Tk()
canvas = Canvas(window, bg = "black", width = 1000, height = 550)

arc = []

seq_list = []

create_gui()

canvas.after(2000, flash_loop, 5)

window.mainloop() 

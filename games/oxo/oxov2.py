from tkinter import *
from random import randint
from time import sleep
moves = []

counter = 0

oxo = [
['','',''],
['','',''],
['','','']

] 






def main_menu():
	global root
	root = Tk()

	root.geometry("300x300")
	root['bg'] = "gray"
	Button_0 = Button(root, height = "2" , width = "20" ,command = Two_players, text = "Two players")
	Button_0.grid(row = 0, column = 0)

	Button_1 = Button(root, height = "2" , width = "20", command = Easy, text = "Easy", bg = "yellow")
	Button_1.grid(row = 1, column = 0)

	Button_2 = Button(root, height = "2" , width = "20", comand = None, text = "Medium")
	Button_2.grid(row = 2, column = 0)

	Button_3 = Button(root, height = "2" , width = "20", comand = None, text = "Hadr")
	Button_3.grid(row = 3, column = 0)

	Button_4 = Button(root, height = "2" , width = "20", comand = None, text = "Okey, you can try")
	Button_4.grid(row = 4, column = 0)

	root.mainloop()


def Two_players():
	root.destroy()
	window = Tk()
	window.title("OXO Game")
	window.geometry("300x300")
	available_space = PhotoImage(file="images/myButton.png")
	player1_taken = PhotoImage(file="images/myButtonP2.png")
	player2_taken = PhotoImage(file="images/myButtonP1.png")
	winner = PhotoImage(file="images/winner.png")
	square = [None] * 9

	def create_buttons():
		square[0] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(0))
		square[0].place(x = 0, y = 0)

		square[1] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(1))
		square[1].place(x = 100, y = 0)

		square[2] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(2))
		square[2].place(x = 200, y = 0)

		square[3] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(3))
		square[3].place(x = 0, y = 100)

		square[4] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(4))
		square[4].place(x = 100, y = 100)

		square[5] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(5))
		square[5].place(x = 200, y = 100)

		square[6] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(6))
		square[6].place(x = 0, y = 200)

		square[7] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(7))
		square[7].place(x = 100, y = 200)

		square[8] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(8))
		square[8].place(x = 200, y = 200)

	def handle_button_click(button_number):
		global counter 
		print("Button ", button_number, "was clicked")
		square[button_number].configure(image = player1_taken, command = square_taken)
		if counter % 2 == 0:
			square[button_number].configure(image=player1_taken,
				                            command=square_taken)
			update_move(button_number, 1)
		else:
			square[button_number].configure(image=player2_taken,
				                            command=square_taken)
			update_move(button_number, 2)
		counter += 1



	def square_taken():
		messagebox.showinfo("Square Taken", "Square already taken choose another!")
	def update_move(square_number, player_number):
		square_to_oxo_map = [[0, 0], [0, 1], [0, 2],
	 						[1, 0], [1, 1], [1, 2],
							[2, 0], [2, 1], [2, 2]]
		m = square_to_oxo_map
		p = player_number
		s = square_number

		oxo[m[s][0]][m[s][1]] = p
		check_win()

	def check_win():
		won = []
		won.append(oxo[0][0] == oxo[1][1] == oxo[2][2] and oxo[0][0] != '')
		won.append(oxo[0][2] == oxo[1][1] == oxo[2][0] and oxo[0][2] != '')
		for row in range(3):
			won.append(oxo[row][0] == oxo[row][1] == oxo[row][2] and oxo[row][0] != '')
		for col in range(3):
			won.append(oxo[0][col] == oxo[1][col] == oxo[2][col] and oxo[0][col] != '')
		if True in won:
			button = Button(window, image = winner, width = "300",
							height = "300")
			button.pack()

	create_buttons()

	window.mainloop()	






#
#
#
#
#
#








def Easy():



	root.destroy()
	window = Tk()
	window.title("OXO Game")
	window.geometry("300x300")
	available_space = PhotoImage(file="images/myButton.png")
	player1_taken = PhotoImage(file="images/myButtonP2.png")
	player2_taken = PhotoImage(file="images/myButtonP1.png")
	winner = PhotoImage(file="images/winner.png")
	square = [None] * 9

	def create_buttons():
		square[0] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(0))
		square[0].place(x = 0, y = 0)

		square[1] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(1))
		square[1].place(x = 100, y = 0)

		square[2] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(2))
		square[2].place(x = 200, y = 0)

		square[3] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(3))
		square[3].place(x = 0, y = 100)

		square[4] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(4))
		square[4].place(x = 100, y = 100)

		square[5] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(5))
		square[5].place(x = 200, y = 100)

		square[6] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(6))
		square[6].place(x = 0, y = 200)

		square[7] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(7))
		square[7].place(x = 100, y = 200)

		square[8] = Button(window, image = available_space, width = "100",
								   height = "100", command = lambda: handle_button_click(8))
		square[8].place(x = 200, y = 200)

	def handle_button_click(button_number):
		global counter 
		moves.append(button_number)
		print("Button ", button_number, "was clicked")


		square[button_number].configure(image=player1_taken,
		                            command=square_taken)
	
		update_move(button_number, 1)
		print("hello")
		sleep(1)
		ai_generator()


	def ai_generator():
		square_num = ai_move()
		square[square_num].configure(image=player2_taken,
			                            command=square_taken)
		update_move(square_num, 2)
	



	def square_taken():
		messagebox.showinfo("Square Taken", "Square already taken choose another!")
	def update_move(square_number, player_number):
		square_to_oxo_map = [[0, 0], [0, 1], [0, 2],
	 						[1, 0], [1, 1], [1, 2],
							[2, 0], [2, 1], [2, 2]]
		m = square_to_oxo_map
		p = player_number
		s = square_number

		oxo[m[s][0]][m[s][1]] = p
		check_win()

	def ai_move():
		random_move = randint(0, 8)
		while random_move in moves:
			random_move = randint(0, 8)
		moves.append(random_move)
		if [1,2,3,4,5,6,7,8] in moves:
			main_menu()
		return random_move






	def check_win():
		won = []
		won.append(oxo[0][0] == oxo[1][1] == oxo[2][2] and oxo[0][0] != '')
		won.append(oxo[0][2] == oxo[1][1] == oxo[2][0] and oxo[0][2] != '')
		for row in range(3):
			won.append(oxo[row][0] == oxo[row][1] == oxo[row][2] and oxo[row][0] != '')
		for col in range(3):
			won.append(oxo[0][col] == oxo[1][col] == oxo[2][col] and oxo[0][col] != '')
		if True in won:
			button = Button(window, image = winner, width = "300",
							height = "300")
			button.pack()

	create_buttons()

	window.mainloop()	



main_menu()
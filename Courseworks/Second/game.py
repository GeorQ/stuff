from tkinter import * 

def menu():
	def bye():
		menu.destroy()

	global menu
	name = nick
	menu = Tk()
	menu.geometry("1920x1080")
	label = Label(menu, bg ="#012", width = "200", height = "200")
	label.pack(side = "top", fill = "x")
	text = "Welcome to the Game\n" + name
	welcome = Label(menu, bg ="#012", text = text, font=("Courier", 44), fg = "white")
	welcome.place(x ="630", y = "130")

	frame = Frame(menu, bg = "#012")
	frame.place(x = "800", y ="360")

	button1 = Button(frame, bg ="grey", width = "20", height = "2", text = "Start the game!", font=("Courier", 20), fg = "white")
	button1.grid(row = 0, column = 0, pady = 2)

	button2 = Button(frame, bg ="grey", width = "20", height = "2", text = "Choose the level", font=("Courier", 20), fg = "white")
	button2.grid(row = 1, column = 0, pady = 2)

	button3 = Button(frame, bg ="grey", width = "20", height = "2", text = "Shop and meditation", font=("Courier", 20), fg = "white")
	button3.grid(row = 2, column = 0, pady = 2)

	button4 = Button(frame, bg ="grey", width = "20", height = "2", text = "Bestiary", font=("Courier", 20), fg = "white")
	button4.grid(row = 3, column = 0, pady = 2)

	button5 = Button(frame, bg ="grey", width = "20", height = "2", text = "log off", font=("Courier", 20), fg = "white")
	button5.grid(row = 4, column = 0, pady = 2)

	button6 = Button(frame, bg ="grey", width = "20", height = "2", text = "Exit", font=("Courier", 20), fg = "white", command = bye)
	button6.grid(row = 5, column = 0, pady = 2)

	menu.mainloop()

def register():
	global register
	def check():
		global nick
		nickname = entry3.get()
		password = entry4.get()

		text = "users/" + nickname + ".txt"
		file = open(text)
		info = file.read()
		file.close()
		info = info.split()
		nick = info[0]
		password2 =  info[1]

		if (nickname == nick) and (password == password2):
			go_into.destroy()
			register.destroy()
			menu()







	def reg():
		nickname = entry1.get()
		password = entry2.get()
		file = open("users/nicknames.txt")
		nicks = file.read().split()

		if (password == "") or (nickname == "") or (nickname in nicks):
			entry1.delete(0, "end")
			entry2.delete(0, "end")
		else:
			name = "users/" + nickname + ".txt"
			file = open(name, "w")
			text = nickname + "\n" + str(password)
			file.write(text)
			file.close()
			file = open("users/nicknames.txt", "a")
			text_v2 = nickname + "\n" 
			file.write(text_v2)
			file.close()
			registerv2.destroy()





	def bye():
		register.destroy()
	
	def sign_up():
		# register.destroy()
		global entry1, entry2, registerv2
		registerv2 = Toplevel()
		# file = open("users/1", "w")
		# file.write("loool")
		registerv2.geometry("1920x1080")
		label = Label(registerv2, bg ="#012", width = "200", height = "200")
		label.pack(fill = "x")

		frame = Frame(registerv2, bg = "#012")
		frame.place(x = "700", y ="360")

		label1 = Label(frame, text = "Enter your nickname",font=("Courier", 20), fg = "white", bg = "gray")
		label1.grid(row = 0, column = 0, padx = 2, pady = 2)
		entry1 = Entry(frame, width = 10, font=("Courier", 20), bg = "#736d84", fg = "white")
		entry1.grid(row = 0, column = 1)

		label2 = Label(frame, text = "Enter your password",font=("Courier", 20), fg = "white", bg = "gray")
		label2.grid(row = 1, column = 0, padx = 2, pady = 2)
		entry2 = Entry(frame, width = 10, font=("Courier", 20), bg = "#736d84", fg = "white")
		entry2.grid(row = 1, column = 1, pady = 20)

		button = Button(frame, bg ="grey", width = "20", height = "2", text = "Sign Up", font=("Courier", 20), fg = "white", command = reg)
		button.grid(row = 2, columnspan = 2 ,pady = 2)
		registerv2.mainloop()

	def sign_in():

		global entry3, entry4, go_into

		go_into = Toplevel()

		go_into.geometry("1920x1080")
		label = Label(go_into, bg ="#012", width = "200", height = "200")
		label.pack(fill = "x")

		frame = Frame(go_into, bg = "#012")
		frame.place(x = "700", y ="360")

		label1 = Label(frame, text = "Enter your nickname",font=("Courier", 20), fg = "white", bg = "gray")
		label1.grid(row = 0, column = 0, padx = 2, pady = 2)
		entry3 = Entry(frame, width = 10, font=("Courier", 20), bg = "#736d84", fg = "white")
		entry3.grid(row = 0, column = 1)

		label2 = Label(frame, text = "Enter your password",font=("Courier", 20), fg = "white", bg = "gray")
		label2.grid(row = 1, column = 0, padx = 2, pady = 2)
		entry4 = Entry(frame, width = 10, font=("Courier", 20), bg = "#736d84", fg = "white")
		entry4.grid(row = 1, column = 1, pady = 20)

		button = Button(frame, bg ="grey", width = "20", height = "2", text = "Sign In", font=("Courier", 20), fg = "white", command = check)
		button.grid(row = 2, columnspan = 2 , pady = 2)
		go_into.mainloop()















	global register
	register = Tk()
	register.geometry("1920x1080")
	label = Label(register, bg ="#012", width = "200", height = "200")
	label.pack(side = "top", fill = "x")
	welcome = Label(register, bg ="#012", text = "Welcome to PUBG", font=("Courier", 44), fg = "white")
	welcome.place(x ="700", y = "130")
	frame = Frame(register, bg = "#012")
	frame.place(x = "800", y ="360")
	button1 = Button(frame, bg ="grey", width = "20", height = "2", text = "Sign Up", font=("Courier", 20), fg = "white", command  = sign_up)
	button1.grid(row = 0, column = 0, pady = 2)
	button2 = Button(frame, bg ="grey", width = "20", height = "2", text = "Sign In", font=("Courier", 20), fg = "white", command = sign_in)
	button2.grid(row = 1, column = 0, pady = 2)
	button3 = Button(frame, bg ="grey", width = "20", height = "2", text = "Exit", font=("Courier", 20), fg = "white", command = bye)
	button3.grid(row = 5, column = 0, pady = 2)
	register.mainloop()

register()
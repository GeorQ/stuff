from tkinter import * 
import hashlib 






def menu():
	def bye():
		menu.destroy()

	global menu
	name = nick
	menu = Tk()
	ws = menu.winfo_screenwidth()
	hs = menu.winfo_screenheight()
	menu.geometry(("%dx%d" % (ws,hs)))
	menu.state('zoomed')
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
		hashed_pass = hashlib.md5(password.encode()).hexdigest()

		if (nickname == nick) and (hashed_pass == password2):
			go_into.destroy()
			register.destroy()
			menu()







	def reg():
		nickname = cre_login.get()
		password = cre_pass.get()
		hashed_pass = hashlib.md5(password.encode()).hexdigest()

		file = open("users/nicknames.txt")
		nicks = file.read().split()

		if (password == "") or (nickname == "") or (nickname in nicks):
			cre_login.delete(0, "end")
			cre_pass.delete(0, "end")

		else:
			name = "users/" + nickname + ".txt"
			file = open(name, "w")
			text = nickname + "\n" + str(hashed_pass)
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
		global cre_login, cre_pass, registerv2
		registerv2 = Toplevel()
		# file = open("users/1", "w")
		# file.write("loool")
		ws = registerv2.winfo_screenwidth()
		hs = registerv2.winfo_screenheight()
		registerv2.geometry(("%dx%d" % (ws,hs)))
		registerv2.state('zoomed')
		label = Label(registerv2, bg ="#012", width = "200", height = "200")
		label.pack(fill = "x")

		frame = Frame(registerv2, bg = "#012")
		frame.place(x = "700", y ="360")

		label1 = Label(frame, text = "Enter your nickname",font=("Courier", 20), fg = "white", bg = "gray")
		label1.grid(row = 0, column = 0, padx = 2, pady = 2)
		cre_login = Entry(frame, width = 10, font=("Courier", 20), bg = "#736d84", fg = "white")
		cre_login.grid(row = 0, column = 1)

		label2 = Label(frame, text = "Enter your password",font=("Courier", 20), fg = "white", bg = "gray")
		label2.grid(row = 1, column = 0, padx = 2, pady = 2)
		cre_pass = Entry(frame, width = 10, font=("Courier", 20), bg = "#736d84", fg = "white", show = "*")
		cre_pass.grid(row = 1, column = 1, pady = 20)

		button = Button(frame, bg ="grey", width = "20", height = "2", text = "Sign Up", font=("Courier", 20), fg = "white", command = reg)
		button.grid(row = 2, columnspan = 2 ,pady = 2)
		registerv2.mainloop()

	def sign_in():

		global entry3, entry4, go_into

		go_into = Toplevel()
		ws = go_into.winfo_screenwidth()
		hs = go_into.winfo_screenheight()
		go_into.geometry(("%dx%d" % (ws,hs)))
		go_into.state('zoomed')
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
	ws = register.winfo_screenwidth()
	hs = register.winfo_screenheight()
	register.geometry(("%dx%d" % (ws,hs)))
	# register.attributes('-fullscreen', True)
	register.state('zoomed')
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
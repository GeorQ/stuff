from tkinter import * 
import hashlib 
import time




def menu():
	def bye():
		menu.destroy()

	global menu
	name = nick
	menu = Tk()
	ws = menu.winfo_screenwidth()
	hs = menu.winfo_screenheight()
	menu.geometry(("%dx%d" % (ws,hs)))
	menu.attributes('-fullscreen', True)
	label = Label(menu, bg ="#012", width = "200", height = "200")
	label.pack(side = "top", fill = "x")
	text = "Welcome to the Game\n" + name
	welcome = Label(menu, bg ="#012", text = text, font=("Courier", 44), fg = "white")
	welcome.place(x =ws/3 - 30, y = "130")

	frame = Frame(menu, bg = "#012")
	frame.place(x = ws/2 - 150, y ="360")

	new_game = Button(frame, bg ="grey", width = "20", height = "2", text = "Start the game!", font=("Courier", 20), fg = "white", command = start)
	new_game.grid(row = 0, column = 0, pady = 2)


	continue_game = Button(frame, bg ="grey", width = "20", height = "2", text = "Continue", font=("Courier", 20), fg = "white", state = DISABLED)
	continue_game.grid(row = 1, column = 0, pady = 2)

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
		global nick, nickname
		nickname = ex_login.get()
		password = ex_pass.get()

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

		file = open(name, "w")
		if (password == "") or (nickname == "") or (nickname in nicks):
			cre_login.delete(0, "end")
			cre_pass.delete(0, "end")

		else:
			name = "users/" + nickname + ".txt"
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
		def go_back():
			registerv2.destroy()
		# register.destroy()
		global cre_login, cre_pass, registerv2
		registerv2 = Toplevel()
		# file = open("users/1", "w")
		# file.write("loool")
		ws = registerv2.winfo_screenwidth()
		hs = registerv2.winfo_screenheight()
		registerv2.geometry(("%dx%d" % (ws,hs)))
		registerv2.attributes('-fullscreen', True)
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
		button = Button(frame, bg ="grey", width = "20", height = "2", text = "Go back", font=("Courier", 20), fg = "white", command = go_back)
		button.grid(row = 3, columnspan = 2 , pady = 2)
		registerv2.mainloop()

	def sign_in():
		def go_back():
			go_into.destroy()
		global ex_login, ex_pass, go_into

		go_into = Toplevel()

		ws = go_into.winfo_screenwidth()
		hs = go_into.winfo_screenheight()
		go_into.geometry(("%dx%d" % (ws,hs)))
		go_into.attributes('-fullscreen', True)
		label = Label(go_into, bg ="#012", width = "200", height = "200")
		label.pack(fill = "x")

		frame = Frame(go_into, bg = "#012")
		frame.place(x = "700", y ="360")

		l_log = Label(frame, text = "Enter your nickname",font=("Courier", 20), fg = "white", bg = "gray")
		l_log.grid(row = 0, column = 0, padx = 2, pady = 2)
		ex_login = Entry(frame, width = 10, font=("Courier", 20), bg = "#736d84", fg = "white")
		ex_login.grid(row = 0, column = 1)

		l_pass = Label(frame, text = "Enter your password",font=("Courier", 20), fg = "white", bg = "gray")
		l_pass.grid(row = 1, column = 0, padx = 2, pady = 2)
		ex_pass = Entry(frame, width = 10, font=("Courier", 20), bg = "#736d84", fg = "white", show = "*")
		ex_pass.grid(row = 1, column = 1, pady = 20)

		button = Button(frame, bg ="grey", width = "20", height = "2", text = "Sign In", font=("Courier", 20), fg = "white", command = check)
		button.grid(row = 2, columnspan = 2 , pady = 2)

		button = Button(frame, bg ="grey", width = "20", height = "2", text = "Go back", font=("Courier", 20), fg = "white", command = go_back)
		button.grid(row = 3, columnspan = 2 , pady = 2)

		go_into.mainloop()



	global register
	register = Tk()
	ws = register.winfo_screenwidth()
	hs = register.winfo_screenheight()
	register.geometry(("%dx%d" % (ws,hs)))
	register.attributes('-fullscreen', True)
	register.state('zoomed')
	label = Label(register, bg ="#012", width = "200", height = "200")
	label.pack(side = "top", fill = "x")
	welcome = Label(register, bg ="#012", text = "Welcome to Space Defender", font=("Courier", 44), fg = "white")
	welcome.place(x = ws/4, y = "130")
	frame = Frame(register, bg = "#012")
	frame.place(x = ws/2 - 200, y ="360")
	button1 = Button(frame, bg ="grey", width = "20", height = "2", text = "Sign Up", font=("Courier", 20), fg = "white", command  = sign_up)
	button1.grid(row = 0, column = 0, pady = 2)
	button2 = Button(frame, bg ="grey", width = "20", height = "2", text = "Sign In", font=("Courier", 20), fg = "white", command = sign_in)
	button2.grid(row = 1, column = 0, pady = 2)
	button3 = Button(frame, bg ="grey", width = "20", height = "2", text = "Exit", font=("Courier", 20), fg = "white", command = bye)
	button3.grid(row = 5, column = 0, pady = 2)
	register.mainloop()

def start():
	menu.destroy()
	start_game()





def start_game():
	health = 100
	money = 0
	exp = 0
	def exit():
		gamewin.destroy()
	def leftKey(event):
		canvas.move(hero, -10, 0)
	def rightKey(event):
		canvas.move(hero, 10, 0)
	def upKey(event):
		canvas.move(hero, 0, -10)
	def downKey(event):
		canvas.move(hero, 0, 10)




	gamewin = Tk()
	gamewin.focus_force()
	mainhero = PhotoImage(file = "images/mainhero.png")
	ws = gamewin.winfo_screenwidth()
	hs = gamewin.winfo_screenheight()
	gamewin.geometry(("%dx%d" % (ws+10 ,hs + 10)))
	gamewin.attributes('-fullscreen', True)
	gamewin.attributes("-topmost", True)
	nhs = hs - 100
	canvas = Canvas(gamewin, height = nhs, width = ws, bg = "#af854c")


	canvas.bind("<Left>", leftKey)
	canvas.bind("<Right>", rightKey)
	canvas.bind("<Up>", upKey)
	canvas.bind("<Down>", downKey)
	canvas.focus_set()
	mainscene = PhotoImage(file = "images/main.jpg")
	canvas.create_image(0,0, anchor = NW, image = mainscene)
	canvas.pack()
	buttonex = Button(gamewin,height= 5, text = "Save and Exit" , font=("Courier", 20) ,bg = "grey", command = exit)
	buttonex.pack(side = "right")
	buttonpause = Button(gamewin,height= 5, width = 10,text = "Pause" , font=("Courier", 20) ,bg = "grey", command = exit)
	buttonpause.pack(side = "right")
	shop = Button(gamewin,height= 5, width = 10, text = "shop" , font=("Courier", 20) ,bg = "grey", command = exit)
	shop.pack(side = "right")

	health_text = "HP: " + str(health) + "/100"
	money_text = "Money: " + str(money) + "/100"
	exp_text = "Exp: " + str(exp) + "/100"

	exp = Label(gamewin, height = 5, width = 14, text = exp_text, font=("Courier", 20) ,bg = "grey")
	exp.pack(side = "right")
	money = Label(gamewin, height = 5, width = 14, text = money_text, font=("Courier", 20) ,bg = "grey")
	money.pack(side = "right", padx = 3)
	health = Label(gamewin, height = 5, width = 14, text = health_text, font=("Courier", 20) ,bg = "grey")
	health.pack(side = "right")
	hero = canvas.create_image(500,500, image = mainhero)
	canvas.move(hero, 100, 100)
	first = Button(gamewin,height= 5, text = "First ability" , font=("Courier", 20) ,bg = "grey", command = exit)
	first.pack(side = "left")
	second = Button(gamewin,height= 5, text = "Second Ability" , font=("Courier", 20) ,bg = "grey", command = exit)
	second.pack(side = "left")
	gamewin.after(1, lambda: gamewin.focus_force()) #In order to set focus on the main window
	gamewin.mainloop()























































	
register()
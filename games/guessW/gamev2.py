import random

words_file = open("eng.txt", "rt")
words = words_file.read().split()
words_file.close()
word = random.choice(words)
len_word = len(word)

def cheat(words, all_guesses):
	global word
	new_word = random.choice(words)
	# print(new_word[0], new_word)
	while (word[0] in all_guesses):
		word = random.choice(words)
	return word

while True:
	all_guesses = []
	game_mode = str(input("\t\tHello to the Game!!!\n\t\n\t1. Easy\n\t2. Medium\n\t3. Hard\n\t4. You will lose don't worry\n\nPlease choose the game mode: "))
	while (game_mode != "1" and game_mode != "2" and game_mode != "3" and game_mode != "4"):
		game_mode = input("Please enter one of the four options: ")

	if game_mode == "1":
		while len_word < 10:
			word = random.choice(words)
			len_word = len(word)
	elif game_mode == "2":
		while len_word >= 10 or len_word < 6:
			word = random.choice(words)
			len_word = len(word)
	elif game_mode == "3":
		while len_word >= 6:
			word = random.choice(words)
			len_word = len(word)
	elif game_mode == "4":
		loose = 0
		while loose != 10:
			print("Okey bro)))) let's play in this game")
			print (word)
			guess = input("Enterg guess " + str(loose) + "/10: ")
			all_guesses.append(guess)
			loose += 1
			if guess[0] == word[0]:
				word = cheat(words, all_guesses)
				print (word)

	# print(len_word, " ", word)
	#
	# print(word)
	# count = 0
	# win = False
	#
	# guesses = ""
	# answer = "-" * int(len_word)
	# print (answer)
	# while (count < 10 and win is False):
	# 	count += 1
	# 	guess = input("Enterg guess " + str(count) + "/10: ")
	# 	while guess in all_guesses:
	# 		guess = input("Enter the different guess this already was")
	#
	# 	all_guesses.append(guess)
	# 	guesses += guess
	# 	tmp = ""
	# 	i = 0
	# 	while (i < len(word)):
	# 	 	if (word[i] == guess):
	# 	 		tmp += guess
	# 	 	else:
	# 	 		tmp += answer[i]
	# 	 	i += 1
	# 	if (answer != tmp):
	# 		print("good guess")
	# 		count = count - 1
	# 		answer = tmp
	#
	# 	else:
	# 		print("Not a great guess")
	# 	if (answer == word):
	# 		print("Well done you win!")
	# 		win = True
	# 	print(str(10 - count) + " guesses left.")
	# 	print("your guesses: " + guesses)
	# 	print("The word so far: " + answer)
	# 	print("These all your guesses: ", all_guesses)
	# if (count == 10 and win is False):
	# 	print("Sorry, but you loose, correct word was: " + word)
	# cho = input("Do you want play again? ").lower()
	# if cho == "yes" or cho == "y":
	# 	continue
	# else:
	# 	break

input("Enter")

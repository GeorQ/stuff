from datetime import datetime
from time import time
from difflib import SequenceMatcher
from os import path

def main_scene(): #main scene which will be shown at the start of the program
	print("\n" + ("  █" + "▀"+"▀"*43+"█\n") + ("  █" + "   S P E L L   C H E C K E R "+" "*15+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "     1. Check a file "+" "*23+"█\n") + ("  █" + "     2. Check a sentense "+" "*19+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "     0. Quit "+" "*31+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "▄"+"▄"*43+"█")) #▂
	choice = input(("  █\n") + ("  █" + "▄▄" * 9 + "▄█"+" Enter choice: "))
	return choice

def file_scene(): #scene which is apperas when we want to input the name of the file
	print("\n" + ("  █" + "▀"+"▀"*43+"█\n") + ("  █" + "    L O A D   F I L E "+" "*22+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "      Enter the file name "+" "*18+"█\n") + ("  █" + "      then press [enter] "+" "*19+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "▄"+"▄"*43+"█")) #▂
	file_name = input(("  █\n") + ("  █" + "▄▄" * 6 + "▄█"+" File name: "))
	return file_name

def first_word_scene(word, different_word): #scene when we want to change or nor the word
	print("\n" + ("  █" + "▀"+"▀"*43+"█\n") + ("  █" + "    W O R D   N O T   F O U N D "+" "*12+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "      "+ word +" "*(44 - int(len(word)) - 6)+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "      Did you mean " + " "*25+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "      " + different_word + " " * (44 - int(len(different_word)) - 6) +"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "▄"+"▄"*43+"█")) #▂
	choice = input(("  █\n") + ("  █" + "▄▄" * 6 + "▄█"+" Enter [y] or [n]: "))
	return choice

def second_word_scene(word): #scene of actions with wrong words
	print("\n" + ("  █" + "▀"+"▀"*43+"█\n") + ("  █" + "    W O R D   N O T   F O U N D "+" "*12+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "      "+ word +" "*(44 - int(len(word)) - 6)+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "      1. Ignore the word. " + " " * 18 + "█\n") + ("  █" + "      2. Mark the word as incorrect. " + " " * 7 + "█\n") + ("  █" + "      3. Add the word to dictionary. " + " " * 7 + "█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "▄"+"▄"*43+"█")) #▂
	choice = input(("  █\n") + ("  █" + "▄▄" * 6 + "▄█"+" Enter choice: "))
	return choice

while True: #main loop, which allow us to work with program as long as we want
	total = 0
	correct = 0
	wrong = 0
	wrong_ignor = 0
	wrong_mark = 0
	wrong_dict = 0
	alpha_char = "qwertyuioplkmnjhbgvfcxdzsa " # var of alpha characters and space to keep words separatly
	mode_choice = main_scene()
	print("\n\n\n")
	if mode_choice == "0": #if they want to quit from the application
		break
	elif mode_choice == "1": # mode for checking the file
		file_name = file_scene()
		while (not path.isfile(file_name)): # check for presence of the file in oreder to avoid the error because of misclick
			print("\n\nYou should put correct file name\n")
			file_name = file_scene()
		start = time() # start of the timer
		file_to_check = open(file_name, "rt")
		file_content = file_to_check.read()
		file_to_check.close()

		file_content = file_content.lower() # make all character in sentense lower case, because all word in dictionry have lower case

		for letter in file_content: # This loop cheack for alpha chars in words and if they are not alpha char it delete it
			if letter not in alpha_char:
				file_content = file_content.replace(letter, "")


		file_content = file_content.split() #now this became a list, we should use list here because?
		dictionary = open("01_EnglishWords.txt", "rt")
		test = dictionary.read() #put all words from file 0_1EnglishWords.txt inside the var "test"
		dictionary.close()
		test = test.strip() #delete space from beginig and end?
		test = test.split() #slpit all words in list
		# print(file_content)
		wrong_words = []

		for word in file_content:

			if word in test:
				pass
			else:
				wrong_words.append(word)
		end = time() # one more start of the time in var "end"



		now_time = datetime.now()# their difference = time of executing of this loop



		report_words = ""
		for word in file_content: #checking every word in file
			total += 1
			if word not in wrong_words: #if the word correct then just put it in new file without changes
				report_words += word + " "
				correct += 1
			else:
				ratio = 0
				changed_word = ""
				for item in test: #loop which finds the most similar word
					if (ratio < SequenceMatcher(None, word, item).ratio()):
						ratio = SequenceMatcher(None, word, item).ratio()
						changed_word = item

				change_not = first_word_scene(word, changed_word)
				while change_not not in ("y", "Y", "n", "N"):
					print("\n\nYou have to print one of the following funcions\n")
					change_not = first_word_scene(word, changed_word)
				if change_not == "y" or change_not == "Y":
					report_words += changed_word + " "
					correct += 1
				else: # branch for the actions with uncorrect words
					wrong += 1
					decision = second_word_scene(word)

					while (decision != "1" and decision != "2" and decision != "3"):
						print("\n\nYou have to print one of the following funcions\n")
						decision = second_word_scene(word)

					if decision == "1":#mark as ingored word
						word = "!" + word + "! "
						report_words += word
						wrong_ignor += 1
					elif decision == "2":#mark as wrong
						word = "?" + word + "? "
						report_words += word
						wrong_mark += 1
					elif decision == "3": #add to the dictionary
						dictionary = open("01_EnglishWords.txt", "a")
						dictionary.write("\n" + word)
						dictionary.close()
						word = "*" + word + "* "
						report_words += word
						wrong_dict += 1

		print("\n Number of words: ",total, "\n Number of correctly spelt words: ", correct, "\n Number of incorrectly spelt words: ", wrong, "\n\t Number ignored: " + str(wrong_ignor)+ "\n\t Number added to dictionary: " + str(wrong_dict) + "\n\t Numer marked: " + str(wrong_mark) + "\n")
		print(" Time elapsed ",(int((end - start)* 10**6)), " microseconds")
		report_list = str(now_time) + "\n"+"Number of words: " + str(total) + "\nNumber of correctly spelt words: " + str(correct) + "\nNumber of incorrectly spelt words: " + str(wrong) + "\n"
		report_list += "\t\tNumber ignored:" + str(wrong_ignor) + "\n\t\tNumber added to dictionary: " + str(wrong_dict) + "\n\t\tNumber marked: " + str(wrong_mark) + "\n\n" + report_words
		report = open("report.txt", "w")
		report.write(report_list)
		report.close()



	elif mode_choice == "2": #mode for checking the sentense
		sentense = input("Please enter the sentense, which you want to check: ")
		# sentense = "lol1 121l  flf1'fe1     lfefk.     21;f lfe lfefe wsqsa cxczxas qwe asx"
		sentense = sentense.lower() # make all character in sentense lower case, because all word in dictionry have lower case


		for x in sentense: # This loop check for alpha chars in words and if it now alpha char it delete it
			if x not in alpha_char:
				sentense = sentense.replace(x, "")

		print (sentense, "\n")

		sentense = sentense.split() # split sentense to the list of word in order to work with each of them

		dictionary = open("01_EnglishWords.txt", "rt")
		test = dictionary.read() #put all words from file 0_1EnglishWords.txt inside the var "test"
		dictionary.close()
		test = test.strip() #deleate space from beginig and end?
		test = test.split() #slpit all words in list



		total = len(sentense)

		for x in sentense: # Loop will check for every word in sentense to be in dictionary or not
			if x in test:
				correct += 1
				print(x + " spelt correctly")
			else:
				wrong += 1
				print (x + " not found in dictionary")

		print ("\n")

		print("Number of words: ", total)
		print("Number of correctly spelt words: ", correct)
		print("Number of incorrectly spelt words: ", wrong)

	else:
		print("\n\n") #some space to begin with
		continue

	continue_exit = input("Press 'q' [enter] to quit or any other key [enter] to go again: ")
	if continue_exit == "q" or continue_exit == "Q":
		break
	else:
		print("\n\n") #some space to begin with
		continue



input("Eneter")
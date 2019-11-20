import time, datetime

while True: #main loop, which allow us to work with program as long as we want
	total = 0
	correct = 0
	wrong = 0
	wrong_ignor = 0
	wrong_mark = 0
	wrong_dict = 0
	alpha_char = "qwertyuioplkmnjhbgvfcxdzsa " # var of alpha characters and space to keep words separatly
	print("\tS P E L L   C H E C K E R\n")
	mode_choice = input("\t  1. Check a file\n\t  2. Check a sentense\n\n\t  0. Quit\n\n Enter choice: ")
	if mode_choice == "0": #if they want to quit from the application 
		break
	elif mode_choice == "1": # mode for checking the file
		file_name = input(" Enter the name of the file to spellcheck: ")
		start = time.time()
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
		test = test.strip() #deleate space from beginig and end?
		test = test.split() #slpit all words in list
		# print(file_content)
		wrong_words = []
		for word in file_content:
			total += 1
			if word in test:
				correct += 1
			else:
				wrong +=1
				wrong_words.append(word)
		end = time.time()



		now_time = datetime.datetime.now()


		report_list = str(now_time) + "\n"+"Number of words: " + str(total) + "\nNumber of correctly spelt words: " + str(correct) + "\nNumber of incorrectly spelt words: " + str(wrong) + "\n\n"

		for word in file_content:
			if word not in wrong_words:
				report_list += word + " "
			else:
				decision = input("\n" + word + " not found\n\n\n 1.  Ignore the word.\n\n\n 2.  Mark the word as incorrect.\n\n\n 3.  Add word to dictionary.\n\n\n Enter choice: ")
			
				while (decision != "1" and decision != "2" and decision != "3"):
					decision = input("Please choose one of the three options!\n Enter option: ") 

				if decision == "1":
					word = "!" + word + "! "
					report_list += word
					wrong_ignor += 1
				elif decision == "2":
					word = "?" + word + "? "
					report_list += word
					wrong_mark += 1
				elif decision == "3":
					dictionary = open("01_EnglishWords.txt", "a")
					dictionary = dictionary.write("\n" + word)
					dictionary.close()#whant to change
					word = "*" + word + "* "
					report_list += word
					wrong_dict += 1
		print("\n Number of words: ",total, "\n Number of correctly spelt words: ", correct, "\n Number of incorrectly spelt words: ", wrong, "\n\t Number ignored: " + str(wrong_ignor)+ "\n\t Number added to dictionary: " + str(wrong_dict) + "\n\t Numer marked: " + str(wrong_mark) + "\n")
		print(" Time elapsed ",(int((end - start)* 10**6)), " microseconds")

		report = open("report.txt", "w")
		report.write(report_list)
		report.close()








	elif mode_choice == "2": #mode for checking the sentense
		sentense = input("Please enter the sentense, which you want to check: ")
		# sentense = "lol1 121l  flf1'fe1     lfefk.     21;f lfe lfefe wsqsa cxczxas qwe asx"
		sentense = sentense.lower() # make all character in sentense lower case, because all word in dictionry have lower case


		for x in sentense: # This loop cheack for alpha chars in words and if it now alpha char it delete it
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

		for x in sentense: # Loop will check for every word in sentense to be in dictionaty or not
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

		answer = input("Press 'q' [enter] to quit or any other key [enter] to go again: ")
		if answer == "q" or answer == "Q":
			break
		else:
			print("\n\n") #some space to begin with
			continue

	else: 
		print("\n\n") #some space to begin with
		continue



input("Enter")

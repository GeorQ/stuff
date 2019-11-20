import time, datetime

while True:
	total = 0
	correct = 0
	wrong = 0
	alpha_char = "qwertyuioplkmnjhbgvfcxdzsa " # var of characters and space to keep words separatly
	print("\tS P E L L   C H E C K E R\n")
	mode_choice = input("\t  1. Check a file\n\t  2. Check a sentense\n\n\t  0. Quit\n\n Enter choice: ")
	if mode_choice == "0":
		break
	elif mode_choice == "1":
		file_name = input(" Enter the name of the file to spellcheck: ")
		start = time.time()
		file_to_check = open(file_name, "rt")
		file_content = file_to_check.read()
		file_to_check.close()

		file_content = file_content.lower() # make all character in sentense lower case, because all word in dictionry have lower case


		for letter in file_content: # This loop cheack for alpha chars in words and if it now alpha char it delete it
			if letter not in alpha_char:
				file_content = file_content.replace(letter, "")


		file_content = file_content.split()
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

		print("\n Number of words: ",total, "\n Number of correctly spelt words: ", correct, "\n Number of incorrectly spelt words: ", wrong, "\n")
		print(" Time elapsed ",(int((end - start)* 10**6)), " microseconds")

		now_time = datetime.datetime.now()


		report_list = str(now_time) + "\n"+"Number of words: " + str(total) + "\nNumber of correctly spelt words: " + str(correct) + "\nNumber of incorrectly spelt words: " + str(wrong) + "\n\n"

		for word in file_content:
			if word not in wrong_words:
				report_list += word + " "
			else:
				word = "?" + word + "? "
				report_list += word

		report = open("report.txt", "w")
		report.write(report_list)
		report.close()

	elif mode_choice == "2":
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

		for x in sentense: # Loop will
			if x in test: #check for every word in sentense to be in dictionaty or not
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
			print("\n\n") #some space to begin with?
			continue

input("Enter")

while True:
	print("\tS P E L   C H E C K E R\n")
	choice = input("\t  1. Check a file\n\t  2. Check a sentense\n\n\t  0. Quit\n\n Enter choice: ")
	if choice == "2":
		sentense = input("Please enter the sentense, which you want to check: ")
		# sentense = "lol1 121l  flf1'fe1     lfefk.     21;f lfe lfefe wsqsa cxczxas qwe asx"
		sentense = sentense.lower() # make all character in sentense lower case, because all word in dictionry have lower case
		alpha_char = "qwertyuioplkmnjhbgvfcxdzsa " # var of characters and space to keep words separaly

		for x in sentense: # This loop cheack for alpha chars in words and if it now alpha char it delete it
			if x not in alpha_char:
				sentense = sentense.replace(x, "") 

		print (sentense, "\n")

		sentense = sentense.split() # split sentense to the list of word in order to work with each of them

		dictionary = open("01_EnglishWords.txt", "rt") 
		test = dictionary.read() #put all words from file 0_1EnglishWords.txt inside the var "test" 
		test = test.strip() #deleate space from beginig and end?
		test = test.split() #slpit all words in list

		total = 0
		correct = 0
		wrong = 0

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


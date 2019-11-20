sentense = input("Please enter the sentense, which you want to check: ")
sentense = sentense.split() # split sentense to the list of word in order to work with each of them

dictionary = open("01_EnglishWords.txt", "rt") 
test = dictionary.read() #put all words from file 0_1EnglishWords.txt inside the var "test" 
test = test.split()
for x in sentense: # Loop will 
	if x in test: #check for every word in sentense to be in dictionaty or not
		print(x, " spelt correctly")
	else:
		print (x + " not found in dictionary")
input("Enter")


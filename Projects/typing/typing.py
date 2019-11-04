import random
words = open("words.txt")
letters = words.read()
score = 0
print("if you want finish practic tap '...' instead of answer")
while True:
	word = ""
	for i in range (random.randint(3,6)):
		word += letters[random.randint(0, int(len(letters) - 1))]
	word = word.strip()
	tr = input("Enter the word as soon as possible '{}': ".format(word))
	if tr == "...":
		break
	while tr != word:
		if score > 0:
			score -= 1
		tr = input ("try again, tap '{}': ".format(word))
	score += 1
	print ("Your current score is: ", score)
words.close()
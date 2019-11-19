from random import randint

def GenerateGrid():
    grid = [["-" for x in range(colMax)] for y in range (rowMax)]
    return grid
    
def DisplayGrid():
    for row in range (rowMax):
        for col in range (colMax):
            print(grid[row][col] + " ", end ="")
        print()

def GetWords():
    theWords = ["happy", "cheerful", "chopper", "effervesecent", "jaunty", "jolly"]
    return theWords

def GetWordsFromUser():
    theWords = []
    while True:
        word = input ("Enter a word and press <enter> (or just press <enter> to finish) :")
        if word != "":
            theWords.append(word)
        else:
            return theWords

def DisplayWords():
    words = GetWords()
    for word in words:
        print(word)

def PlaceWords():
    for word in words:
        if len(word) > rowMax or len(word) > colMax: 
            continue
        count = 0
        foundValidLocation = False
        while not foundValidLocation and count < 10:
            count += 1
            foundValidLocation = True
            direction = randint(0,3)
            if direction == 0:
                print("placing", word, "from left to right")
                min = 0
                max = colMax - len(word)
            elif direction == 1:
                print("placing", word, "from right to left")
                min = len(word) - 1
                max = colMax - 1
            elif direction == 2:
                print("placing", word, "from top to bottom")
                min = 0
                max = rowMax - len(word)
            elif direction == 3:
                print("placing ", word, "from bottom to top")
                min = len(word) - 1
                max = rowMax - 1

            print("Word lenght is ", len(word), " so:")
            print("min: ", min, " max:", max)
            square = randint(min, max)
            print("Square chosen is ", square)
            if direction < 2:
                row = randint(0, rowMax - 1)
                col = square
                print("row is ", row)
            else:
                col = randint(0, colMax - 1)
                row = square
                print("column is ", col)
            
            foundValidLocation = CheckWordWillFit(word, row, col, direction)
            if foundValidLocation:
                PlaceWord(word,row,col,direction)
                guess_words.append(word)
            print("\n")

def PlaceWord(word, row, col, direction):
    for charOfWord in range(len(word)):
        grid[row][col] = word[charOfWord]
        if direction == 0: 
            col += 1
        elif direction == 1:
            col -=1
        elif direction == 2:
            row +=1
        elif direction == 3:
            row -=1

def FillingTheRest():
    alphabet = "qazxswedcvfrtgbnhyujmikolp" 
    for x in range(rowMax):
        for y in range(colMax):
            if grid[x][y] == "-":
                grid[x][y] = alphabet[randint(0, len(alphabet)-1)]

def CheckWordWillFit(word, row, col, direction):
    for charOfWord in range(len(word)):
        if grid[row][col] == "-" or grid[row][col] == word[charOfWord]:
            if direction == 0: col +=1
            if direction == 1: col -=1
            if direction == 2: row +=1 
            if direction == 3: row -=1
        else: 
            print ("Word will not fit")
            return False
    return True



# rowMax = int(input("Enter number of rows: "))
# colMax = int(input("Enter number of columns: "))
words = GetWords()
rowMax = 10
colMax = 10

guess_words = []


grid = GenerateGrid()

print("\n\n\n")
PlaceWords()
DisplayGrid()
print("\n\n\n")
FillingTheRest()
DisplayGrid()
print("\n Try to find all these words: ", guess_words)


input("Enter")
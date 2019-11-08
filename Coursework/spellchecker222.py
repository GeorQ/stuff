# file_name = input("Enter the file name")
# dictionary = open(file_name, "rt").read()
# print(dictionary)



def main_scene():
	print("\n" + ("  █" + "▀"+"▀"*43+"█\n") + ("  █" + "   S P E L L   C H E C K E R "+" "*15+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "     1. Check a file "+" "*23+"█\n") + ("  █" + "     1. Check a sentense "+" "*19+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "     0. Quit "+" "*31+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "▄"+"▄"*43+"█")) #▂
	choice = input(("  █\n") + ("  █" + "▄▄" * 9 + "▄█"+" Enter choice: "))
	return choice

def file_scene():
	print("\n" + ("  █" + "▀"+"▀"*43+"█\n") + ("  █" + "    L O A D   F I L E "+" "*22+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "      Enter the file name "+" "*18+"█\n") + ("  █" + "      then press [enter] "+" "*19+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "▄"+"▄"*43+"█")) #▂
	file_name = input(("  █\n") + ("  █" + "▄▄" * 6 + "▄█"+" File name: "))
	return file_name

def first_word_scene(word, different_word):
	print("\n" + ("  █" + "▀"+"▀"*43+"█\n") + ("  █" + "    W O R D   N O T   F O U N D "+" "*12+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "      "+ word +" "*(44 - int(len(word)) - 6)+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "      Did you mean " + " "*25+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "      " + different_word + " " * (44 - int(len(different_word)) - 6) +"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "▄"+"▄"*43+"█")) #▂
	choice = input(("  █\n") + ("  █" + "▄▄" * 6 + "▄█"+" Enter [y] or [n]: "))
	return choice

def second_word_scene():
	print("\n" + ("  █" + "▀"+"▀"*43+"█\n") + ("  █" + "    W O R D   N O T   F O U N D "+" "*12+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "      "+ word +" "*(44 - int(len(word)) - 6)+"█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "      1. Ignore the word. " + " " * 18 + "█\n") + ("  █" + "      1. Mark the word as incorrect. " + " " * 7 + "█\n") + ("  █" + "      1. Add the word to dictionary. " + " " * 7 + "█\n") + ("  █" + " "+" "*43+"█\n") + ("  █" + "▄"+"▄"*43+"█")) #▂
	choice = input(("  █\n") + ("  █" + "▄▄" * 6 + "▄█"+" Enter choice: "))
	return choice


word = "lofesfsssssssssssssss"

different_word = "flelelfe"



input("Enter")

































# print(("  "+"▂" *40))																																																																						  
																																																																											# " "
# +"▃"*52 + "▐ ▌,▛) ("  ▌" + "▃"+"▃"*24+"  ▐")
# input("\n\n\nEnter")▌
# ▐▐
# ▌▌▐▐
# mode_choice = input("\t  1. Check a file\n\t  2. Check a sentense\n\n\t  0. Quit\n\n Enter choice: ")
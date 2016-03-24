# #How to Learn Python the Hard Way exercises

# #ex5

# cars = 100
# print(cars)

# #ex6

# my_height = 164
# my_cars = 1
# plates = "ECT 786"
# print("My height is %d cm,"
		# "I have %d car and '%s' is it's rego"
		# % (my_height, my_cars, plates))

# #ex7

# print('.' * 10) # that did cool things

# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"

# print(end1 + end2 + end3 + end4 + end5 + end6,
		# end7 + end8 + end9 + end10 + end11 +end12)

# #ex8

# formatter = "%r %r %r %r"

# print(formatter
	# % ("I'd this thing.",
	# "That you could type up right.",
	# "But it didn't sing.",
	# "So I said goodnight."))

# #ex9


# print("""
	# There's something going on here.
	# Even the new lines are a part of the output.
	# """)

# months = "Jan \nFeb" # note the new line
# print("Here are the months", months)

# #ex10

# tabby_cat = "\tI'm tabbed in."
# persian_cat = "I'm split \non a line"
# backslash_cat = "I'm \\ a \\ cat."

# fat_cat = '''
# I'll do a list:
# \t* Cat Food
# \t* Fishies
# \t* Catnip\n\t* Grass
# '''

# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat)

# # don't actually run this bit of code, that while loop is as bad as it looks
# #while True:
# #	for i in ["/","-","|","\\","|"]:
# #		print("%s\r" % i)

# #ex11

# # print("How old are you?",end=" ")
# # age = input()
# # print("You are %s years old" % age)

# #ex12

# # age = input("How old are you? ")

# #ex13

# from sys import argv

# script, first, second = argv
# third = input("What is your third input? ")

# print("The script is called: ", script)
# print("Your first variable is: ", first)
# print("Your second variable is: ", second)
# print("Your third variable is: ", third)

# #ex14

# from sys import argv

# script, user_name = argv
# prompt = '> '

# print("\nHi %s, I'm the %s script." % (user_name, script))
# print("I'd like to ask you a few questions.")
# print("Do you like me %s?" % user_name)
# likes = input(prompt)

# print("Where do you live?")
# lives = input(prompt)

# print("What kind of computer do you have?")
# computer = input(prompt)

# print("""
# Alright, so you said %r about liking me.
# You live in %r. Not sure where that is.
# And you have a %r computer. Nice.
# """ % (likes, lives, computer))

# #ex15

# from sys import argv

# script, filename = argv

# txt = open(filename)

# print("Here's your file %r:" % filename)
# print(txt.read())

# txt.close()

# print("Type the filename again:")
# file_again = input(">")

# txt_again = open(file_again)

# print(txt_again.read())

# txt_again.close()
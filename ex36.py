# ex36

# Every if statement must have an else.
# If the else should never run then it needs a way to exit the block and an error message.
# Never nest if statements more than two deep.
# Treat if statements like paragraphs (sets of sentences) with space before and after.
# Boolean tests should be simple. If they are complex move their calculations elsewhere with a variable.

# custom game

from sys import exit

def landing_pad():
	print("You find yourself on the landing pad of planet Manhattan.")
	print("You see a ship on the pad,",
	"a ship dealer, a bar and the city skyline.")
	print("Which way do you go?")
	
	choice = input("> ")
	
	if "dealer" in choice:
		ship_dealer("landing_pad")
	elif "ship" in choice:
		ship_on_pad()
	elif "bar" in choice:
		bar()
	elif "city" in choice:
		city()
	else:
		death("You fail to notice the edge of the landing platform and fall to your death.")
	
def ship_on_pad():
	print("Walking up to the ship you see that it is expensive",
		"and heavily armed.")
	print("What do you do?")
	
	choice = input("> ")
	
	if "back" in choice:
		landing_pad()
	elif "get in" in choice or "open" in choice or "fly" in choice or "steal" in choice:
		space_criminal()
	else:
		death("The ship's engines suddenly flare to life and cook you alive.")

def city():
	print("The city is busy and very metropolitan, with lots of winding",
		"streets and a large monument in the distance.")
		
	choice = input("> ")
	
	if "monument" in choice:
		monument()
	elif "street" in choice or "explore" in choice or "look" in choice:
		streets()
	elif "back" in choice or "landing" in choice:
		landing_pad()
	else:
		death("You get lost, mugged, and thrown in a dumpster")

def monument():
	print("When you arrive at the monument entrance you look up at the huge facade.")
	print("It looks like a whole colony ship that has been turned into a museum.")
	
	choice = input("> ")
	
	if "street" in choice or "back" in choice:
		streets()
	elif "explore" in choice or "look" in choice or "enter" in choice:
		museum()
	else:
		death("You get lost, knocked out and have your kidneys stolen.")

def museum():
	print("You explore the museum, finding out out all sorts of history.")
	print("This ship came from earth with others, to escape a huge war.")
	print("The Liberty colonists have grown, prospered and flourished over 800 years.")
	monument()

def streets():
	print("You wander the streets back and forward, trying not to get lost.")
	print("There are lots of strange establishments that look expensive.")
	print("You see the occasional homeless person huddled beneath the high city skyline.")

	choice = input("> ")
	
	if "city" in choice or "back" in choice:
		city()
	elif "landing" in choice:
		landing_pad()
	elif "monument" in choice:
		monument()
	elif "help" in choice or "homeless" in choice:
		print("Your efforts do not go unnoticed and you are given a job with the government and live happily ever after.")
	else:
		death("You wind up walking all day but getting lost and somehow get eaten by the Kraken.")

def ship_dealer(entry):
	if entry == "patron":
		print("You arrive at the ship dealer and get given the cheapest ship available with armour like paper.")
		space_lawful()
	elif entry == "landing_pad":
		print("You walk into the ship dealer, going past a long line of very expensive looking ships.")
		print("Having no money however you can't buy any of them and eventually",
			"wander back out to the landing pad")
		landing_pad()
	else:
		death("You brake the game and cease to exist.")

def bar():
	print("Walking into the bar you see a bar tender busy behind the bar and some official looking people sitting at a table.")
	
	choice = input("> ")
	
	if "bar" in choice or "drink" in choice:
		bartender()
	elif "people" in choice or "table" in choice:
		bar_patron()
	else:
		print("You can't seem to achieve that and end up wandering out before you make a fool of yourself.")
		landing_pad()

def bartender():
	print("You talk to the bar tender and he gives you a drink.")
	print("Without prompting him he tells you that the people at the table might have some work for you.")
	print("The table he points out is next to the door")
	
	choice = input("> ")
	
	if "people" in choice or "table" in choice:
		bar_patron()
	elif "door" in choice or "leave" in choice:
		landing_pad()
	else:
		death("You trip over a chair and brake your wrist, ending up in hospital where all your limbs have to be amputated.")

def bar_patron():
	print("Walking up to the table you ask them what they are talking about.")
	print("The one who appears to be a police woman talks about how it's hard to find good hired guns.")
	print("She offers to pay you well and give you a ship if you will help her out.")
	
	choice = input("> ")
	
	if "accept" in choice or "yes" in choice or "help" in choice:
		print("She tells you to meet her at the ship dealer to collect the ship.")
		ship_dealer("patron")
	elif "no" in choice or "refuse" in choice or "leave" in choice:
		print("She repeats her point about finding good help and then says goodbye.")
		death("Unable to find any other work you quickly go broke and starve to death.")
	else:
		print("You end up mumbling so that no one can understand you and leave in embarrassment.")
		landing_pad()

def space_lawful():
	print("When you get into space you barely get a moment to enjoy the view before adventure sweeps you off your feet.")
	print("You are the main character after all.")
	exit()

def space_criminal():
	print("Flying into space you make a quick escape to the less travelled part of the system and begin your life of crime.")
	exit()

def death(text):
	print(text)
	print("Try again? Y/N")
	
	choice = input("> ")
	
	if "y" in choice or "Y" in choice:
		landing_pad()
	elif "n" in choice or "N" in choice:
		exit()
	else:
		death("I hope you enjoy infinite loops.")

landing_pad()
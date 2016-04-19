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
		ship_dealer()
	elif "ship" in choice:
		ship_on_pad()
	elif "bar" in choice:
		bar()
	elif "city" in choice:
		city()
	else:
		death("You fail to notice the edge of the landing platform and fall to your death.")
	
def ship_on_pad():
	print("Walking up to the ship you see that it is expencive",
		"and heavily armed.")
	print("What do you do?")
	
	choice = input("> ")
	
	if "back" in choice:
		landing_pad()
	elif "get in" or "open" or "fly" or "steal" in choice:
		space_criminal()
	else:
		death("The ship's engines suddenly flare to life and cook you alive.")

def city():
	print("The city is busy and very metropolitan, with lots of winding",
		"streets and a large monument in the distance.")
		
	choice = input("> ")
	
	if "monument" in choice:
		monument()
	elif "street" or "explore" or "look" in choice:
		streets()
	elif "back" or "landing" in choice:
		landing_pad()
	else:
		death("You get lost, mugged, and thrown in a dumpster")

def monument():
	print("When you arrive at the monument entrance you look up at the huge facade.")
	print("It looks like a whole colony ship that has been turned into a museum.")
	
	choice = input("> ")
	
	if "street" or "back" in choice:
		streets()
	elif "explore" or "look" or "enter" in choice:
		museum()
	else:
		death("You get lost, knocked out and have your kidneys stolen.")

def museum():
	print("You explore the museum, finding out out all sorts of history.")
	print("This ship came from earth with others, to escape a huge war.")
	print("The Liberty colonists have grown, prospered and flourished over 800 years.")
	monument():

def streets():
	print("You wander the streets back and forward, trying not to get lost.")
	print("There are lots of strange establishments that look expencive.")
	print("You see the occational homeless person huddled beneath the high city skyline.")

	choice = input("> ")
	
	if "city" or "back" in choice:
		city()
	elif "landing" in choice:
		landing_pad()
	elif "monument" in choice:
		monument()
	elif "help" or "homeless" in choice:
	else:
		death("You wind up walking all day but getting lost and somehow get eaten by the Kraken.")

def ship_dealer():
	print("SHIP DEALER TEST")
	exit()

def bar():
	print("BAR TEST")
	exit()

def bartender():
	print("BARTENDER TEST")
	exit()

def bar_patron():
	print("BAR PATRON TEST")
	exit()

def space_lawful():
	print("SPACE LAWFUL TEST")
	exit()

def space_criminal():
	print("SPACE CRIMINAL TEST")
	exit()

def death(text):
	print(text)
	exit()

landing_pad()
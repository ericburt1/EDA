def holder():
	player = input(f"What do you want to do?\n").lower()
	if player in ("n","north"):
		pass
	elif player.lower() == "e" or player.lower() == "east":
		pass
	elif player.lower() == "s" or player.lower() == "south":
		pass
	elif player.lower() == "w" or player.lower() == "west":
		pass
	elif player.lower() == "u" or player.lower() == "north":
		pass
	elif player.lower() == "g" or player.lower() == "grab":
		pass
	elif player == "?" or player.lower() == "help":
		pass
	elif player.lower() == "q" or player.lower() == "quit":
		quit()
	else:
		print("That is not possible.")
		start()
		
#Room one layout each set of parenthasis is an area with its functon ame 
#(start)(keyR1)
#(c1r2) (c1r2)
#(doorR1)

def gamelose(cause):
	print("\n"*5)
	print(cause)
	print("Game over!")
	

def helpdisplay(area):
	print("\n"*5)
	print("""
	Actions:
	Grab (g)
	Use (u)
	North (n)
	East (e)
	South (s)
	West (w)
	Help (?)
		""")
	leave = input("Back to game (y)")
	if leave.lower() == "y":
		area()
	else:gamestarted = False


def welcome():
	output = int(input(f"""
	Welcome to EDA.

	What do you want to do?
	1) Start Game
	2) Quit
			\n"""))
	if output == 1:
		start()
	elif output == 2:
		quit()
	
def validate(values, prompt=f"What do you want to do?\n"):
	while True:
		response = input(prompt).lower()
		if response[0] in values:
			return response

def start(started = False):
	valid = False
	while not valid:
		print("\n"*5)
		if started == False:
			print("Welcome to EDA USER. If you need a reminder of controls type '?'")
			print("You wake up in the corner of a white room.")
		else:
			print("You are back by your bed.")
		print("You notice a door south of you.")
		print("\nMoveable directions: East, South.")
		player = validate("nsewugq")
		started = True
		if player == "n":
			print("You walk north into a wall.")
		elif player.lower() == "e" or player.lower() == "east":
			print("You move east.")
		elif player.lower() == "s" or player.lower() == "south":
			print("You move south.")
		elif player.lower() == "w" or player.lower() == "west":
			print("You walk west into a wall.")
		elif player.lower() == "u" or player.lower() == "use":
			print("You go ignore what is happeneding around you and go back to sleep")
			gamelose("You went to sleep and woke up in your house.")
		elif player.lower() == "g" or player.lower() == "grab":
			print("You look around and don't see anything to pick up.")
		elif player == "?" or player.lower() == "help":
			helpdisplay(start)
		elif player.lower() == "q" or player.lower() == "quit":
			quit()
		else:
			print("That is not possible.")


def keyR1():
	print("You look around and see an empty area other than ...")
	print("a key! Laying there right on the ground!")
	print("\nMoveable directions: North, South, West.")
	player = input(f"What do you want to do?\n")
	if player.lower() == "n" or player.lower() == "north":
		pass
	elif player.lower() == "e" or player.lower() == "east":
		print("You walk west into a wall.")
	elif player.lower() == "s" or player.lower() == "south":
		pass
	elif player.lower() == "w" or player.lower() == "west":
		start()
	elif player.lower() == "u" or player.lower() == "north":
		pass
	elif player.lower() == "g" or player.lower() == "grab":
		pass
	elif player == "?" or player.lower() == "help":
		pass
	elif player.lower() == "q" or player.lower() == "quit":
		quit()
	else:
		print("That is not possible.")
		keyR1()



# FUCNTIONS DO NOT GO PAST HERE


# VARIABLES START HERE
started = False


welcome()
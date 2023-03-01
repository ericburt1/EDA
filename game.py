


def holder():
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			pass
		elif player == "e" :
			pass
		elif player == "s":
			pass
		elif player == "w":
			pass
		elif player == "u":
			pass
		elif player == "g":
			gamelose("You left the game :(")
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

		
#Room one layout each set of parenthasis is an area with its functon ame 
#(start)(keyR1)
#(doorR1) (FillerR2)
#(doorR1)

#
# ACTIONS START ACTIONS START ACTIONS START ACTIONS START ACTIONS START ACTIONS START ACTIONS START ACTIONS START
#
def gamelose(cause):
	print("\n"*2)
	print(cause)
	print("Game over!")
	quit()

def helpdisplay(area):
	print("\n"*2)
	print("""
	Actions:
	Grab (g)
	Use (u)
	North (n)
	East (e)
	South (s)
	West (w)
	Inventory (i)
	Help (?)
		""")
	valid = False
	while valid == False:
		leave = input("Back to game (y)\n").lower()
		if leave[0] == "y":
			area()

def welcome():
	output = int(input(f"""
	Welcome to EDA.

	What do you want to do?
	1) Start Game
	2) Controls
	3) Quit
			\n"""))
	if output == 1:
		start()
	elif output == 2:
		helpdisplay(welcome)
	elif output == 3:
		quit()
	elif output == 890:
		develop_testing()
	

def develop_testing():
	print("\n"*5)
	print("""
	OPTIONS:
	1) start
	2) keyR1
	3) doorR1
	4) mapR2
	5)
	""")
	area = input(f"What room do you want to go to?")
	if area == "start":
		start()
	elif area == "keyR1":
		keyR1()
	elif area == "doorR1":
		doorR1()
	elif area == "mapR2":
		mapR2()
	else: 
		print(f"Invalid command")

def validate(values, prompt=f"What do you want to do?\n"):
	while True:
		response = input(prompt).lower()
		if response[0] == "q":
			gamelose("You left the game :(")
		elif response[0] in values:
			return response


def displayInventory():
	print("Inventory:\n")
	for i in range(len(inventory)):
		part = inventory[i]
		print(f"{i+1}: {part}")
	print()
	return


#
# ACTIONS END ACTIONS END ACTIONS END ACTIONS END ACTIONS END ACTIONS END ACTIONS END ACTIONS END ACTIONS END ACTIONS END
#







#
# ROOM 1 START ROOM 1 START ROOM 1 START ROOM 1 START ROOM 1 START ROOM 1 START ROOM 1 START ROOM 1 START ROOM 1 START
#


def start():
	print("\n"*2)
	print("Welcome to EDA USER. If you need a reminder of controls type '?'")
	print("You are in the corner of a white room.")
	print("You notice a door south of you.")
	print("\nMoveable directions: East, South.")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			print("You walk north into a wall.")
		elif player == "e":
			keyR1()
		elif player == "s":
			doorR1()
		elif player == "w":
			print("You walk west into a wall.")
		elif player == "u":
			print("You go ignore what is happeneding around you and go back to sleep")
			gamelose("You went to sleep and woke up in your house.")
		elif player == "g":
			print("You look around and don't see anything to pick up.")
		elif player == "?":
			helpdisplay(start)
		elif player == "i":
			displayInventory()
		else:
			print("Invalid Input.")

def keyR1():
	if "key" not in inventory:
		print("You look around and see an empty area other than ...")
		print("a key this may come in handy.")
	else:
		print("You are back in the room were the key was.")
		print("The walls are very white.")
	print("\nMovable directions: South, West.")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			print("You walk north into a wall.")
		elif player == "e" :
			print("You walk east into a wall.")
		elif player == "s":
			fillerR1()
		elif player == "w":
			print("You move West.")
			start()
		elif player == "u":
			print("You try to use the key.")
			print("This wall is keyhole-less")
		elif player == "g":
			if "key" in inventory:
				print("You already picked up the key!!")
			else:
				inventory.append("key")
		elif player == "?":
			helpdisplay(keyR1)
		elif player == "i":		
			print("You try to use the key.")
			print("This wall is keyhole-less")
		else:
			print("Invald Input.")

def doorR1():
	print("You notice everything is white except a metal door.")
	print("\nMovable directions: North, East.")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			start()
		elif player == "e" :
			fillerR1()
		elif player == "s":
			print("The door is here. It's locked.")
		elif player == "w":
			print("You walk west into a wall.")
		elif player == "u":
			if "key" in inventory:
				print("You hear a click in the door. The key is stuck in the door.")
				print("The door slides open.")
				for i in range(len(inventory)):
					part = inventory[i]
					if part == "key":
						inventory.remove(inventory[i])
						rooms = 1
				mapR2()
		elif player == "g":
			print("There is nothing to pick up")
		elif player == "?":
			helpdisplay(doorR1)
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def fillerR1():
	print("This appears to be a kitchen.")
	print("The kitchen is very clean. No food appears to be there.")
	print("\nMovable directions: North, West.")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			keyR1()
		elif player == "e" :
			print("You try walking through the wall. It does'nt work very well.")
		elif player == "s":
			print("You try walking through the wall. It does'nt work very well.")
		elif player == "w":
			doorR1()
		elif player == "u":
			if "key" in inventory:
				print("You try to use the key on the oven.")
				print("Nothing happens what did you expect.")
			else:
				print("You don't have anything to use")
		elif player == "g":
			print("There is nothing to pick up")
		elif player == "?":
			helpdisplay(fillerR1)
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

#
# ROOM 1 END ROOM 1 END ROOM 1 END ROOM 1 END ROOM 1 END ROOM 1 END ROOM 1 END ROOM 1 END ROOM 1 END ROOM 1 END ROOM 1 END ROOM 1 END
#



def displayMap(mapp,area):
	print(f"""
	Key:
	X is player
	|, --- are walls
	+ are doors
	* moveable spaces
	M is an interactable
	
	MAP:
	{mapp}
	""")
	area()


#Map for Room2

#  (mapR2)         wall(buttonR2)
#  (hallwayR2)     wall door
#  (keyR2)(hallway2R2)(doorR2)
#  (exitDoorR2)
#

#
# ROOM 2 START ROOM 2 START ROOM 2 START ROOM 2 START ROOM 2 START ROOM 2 START ROOM 2 START ROOM 2 START ROOM 2 START
#

def mapR2():
	print("You can't go back the door locked when you went through.")
	print("You look around and notice a chest.")
	print("\nMovable directions: South")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			print("That was the last room your were in. The door won't budge.")
		elif player == "e" :
			print("You notice the wall has gone to a grey color.")
		elif player == "s":
			pass
		elif player == "w":
			print("You notice the wall has gone to a grey color.")
		elif player == "u":
			if "map" in inventory:
				print("To acces the map enter 'm'")
		elif player == "g":
			if "map" not in inventory:
				print("You move towards the chest and open it.")
				print("You found a MAP. To veiw the map enter 'm'" )
				inventory.append("map")
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			print(inventory)
			if "map" in inventory:
				displayMap("""
		---------
		| X | M |
		| * | + |
		| * * * |
		--+------
				""",mapR2)
		else:
			print("Invald Input.")

#
# ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END
#

# FUCNTIONS DO NOT GO PAST HERE


# VARIABLES START HERE
rooms = 0
started = False
inventory = []

welcome()


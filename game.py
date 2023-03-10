


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
			pass
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
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
	5) keyR2
	""")
	area = input(f"What room do you want to go to?\n")
	if area == "1":
		start()
	elif area == "2":
		keyR1()
	elif area == "3":
		doorR1()
	elif area == "4":
		mapR2()
	elif area == "5":
		keyR2()
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
	print("\n"*2)
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
	print(f"Welcome to EDA {playerName}. If you need a reminder of controls type '?'")
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
	print("\n"*2)
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
	print("\n"*2)
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
	print("\n"*2)
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
	print("\n"*2)
	if "map" not in inventory:
		print(f"EDA: 'Good job {playerName}. That was you first trial. See if you can do this next one.'")
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
			hallWayR2()
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

def hallWayR2():
	print("\n"*2)
	print("You walk into a hallway that appears to have nothing in it.")
	print("\nMovable directions: North, South")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			mapR2()
		elif player == "e" :
			print("As you walk east you notice you aren't moving.")
			print("Must be because of the wall.")
		elif player == "s":
			lockedDoorR2()
		elif player == "w":
			print("You walk west and bump into the wall. Can't go that way.")
		elif player == "u":
			print("The hallway is empty you can't use anything.")
			print("Did you mean to acces the map 'm'")
		elif player == "g":
			print("There's nothing to grab.")
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------
		| * | M |
		| X | + |
		| * * * |
		--+------
				""",mapR2)
		else:
			print("Invald Input.")

def lockedDoorR2():
	print("\n"*2)
	print("You enter this room and notice a door that is south of you.")
	print("It appears to have a lock on it.")
	print("\nMovable directions: North, East, South")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			hallWayR2()
		elif player == "e" :
			hallWay2R2()
		elif player == "s":
			print("The door is locked you can't get through it without a key.")
		elif player == "w":
			print("You walk west and bump into the wall. Can't go that way.")
		elif player == "u":
			if "key" in inventory:
				if 'small cube' not in inventory:
					print('You want to go one but feel like your missing something.')
					print('Look in all the rooms and see if you can find anything.')
				else:
					print('You put the key into the slot and the door shutters and slides open.')
					print('You walk through the door to the next')
			else:
				print("Looks like you need a key for the door.")
		elif player == "g":
			print("You grab the door handle and you can't open the door.")
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------
		| * | M |
		| * | + |
		| X * * |
		--+------
				""",mapR2)
		else:
			print("Invald Input.")

def hallWay2R2():
	print("\n"*2)
	print("You are in a damp and what looks like ruined hallway.")
	print("Ceiling panels look loose. You might want to get into a different room.")
	print("One of the wall panels looks like it could be plied off. Only if you had something to ply it off with.")
	print("\nMovable directions: East, West")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			print("You walk north into a wall.")
		elif player == "e" :
			doorR2()
		elif player == "s":
			print("There is a wall that way, no use going there.")
		elif player == "w":
			lockedDoorR2()
		elif player == "u":
			if 'glass shard' in inventory:
				print("You put the glass shard in the little opening and pry.")
				print("A small peice of the wall comes out reveiling a small cube in the compartment.")
				print("You grab the small cube. It may come in handy later.")
				inventory.append('small cube')
			print("The hallway is empty you can't use anything.")
			print("Did you mean to acces the map 'm'")
		elif player == "g":
			print("Unless you want rotten items theres nothing to grab.")
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------
		| * | M |
		| * | + |
		| * X * |
		--+------
				""",mapR2)
		else:
			print("Invald Input.")

def doorR2():
	print("\n"*2)
	print("You enter a room that has a door up North.")
	print("Otherwise nothing else in this room. What is this place.")
	print("\nMovable directions: North, West")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			keyR2()
		elif player == "e" :
			print("You walk east into a wall.")
		elif player == "s":
			print("There is a wall that way, no use going there.")
		elif player == "w":
			hallWay2R2()
		elif player == "u":
			print("The try to use something but nothing works.")
			print("Did you mean to acces the map 'm'")
		elif player == "g":
			print("There is nothing to grab")
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------
		| * | M |
		| * | + |
		| * * X |
		--+------
				""",mapR2)
		else:
			print("Invald Input.")

def keyR2():
	print("\n"*2)
	print("You walk through the door and see a key in the middle of the room.")
	print("You see a mirror on the wall at the oppisite side of the room.")
	print("\nMovable directions: South")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			print("The mirror is there, wonder what it is?")
		elif player == "e" :
			print("You walk east into a wall.")
		elif player == "s":
			doorR2()
		elif player == "w":
			print("Just a wall.")
		elif player == "u":
			if "glass shard" not in inventory:
				if 'key' in inventory:
					print(f"You hit the key on the mirror and it shatters.")
					print("You grab a peice of the broken mirror.")
					inventory.append("glass shard")
			else:
				print("Maybe theres something to break that mirror.")
		elif player == "g":
			if 'key' not in inventory:
				print("You grab the key. Its very heavy.")
				print("Maybe you could break something with it.")
				inventory.append('key')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------
		| * | X |
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
import random
rooms = 0
started = False
inventory = []
playerName = f"contendor#{random.randrange(1001,9999)}"

welcome()


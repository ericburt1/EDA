


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
	welcome()

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
	6) startR3
	""")
	area = input(f"What room do you want to go to?\n")
	if area == "1":
		start()
	elif area == "2":
		keyR1()
	elif area == "3":
		doorR1()
	elif area == "4":
		inventory.append('map')
		mapR2()
	elif area == "5":
		inventory.append('map')
		keyR2()
	elif area == "6":
		inventory.append('map')
		startR3()
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
		print("a key. 'g' to grab")
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
				print("You grab the key this may come in handy.")
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
			else:
				print("You try to open the door and notice it has a key hole in it.") 
				print("Maybe there is a key around here.")
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
	X is player (if it takes up more than one space then you are in a large room)
	|, --- are walls
	+ are doors
	* moveable spaces
	M is an interactable (Some items and interactables are hidden)
	
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
			if "map" in inventory:
				displayMap("""
		---------
		| X | M |
		| * | + |
		| * * * |
		--+------""",mapR2)
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
		--+------""",hallWayR2)
		else:
			print("Invald Input.")

def lockedDoorR2():
	print("\n"*2)
	print("You enter this room and notice a door.")
	print("It appears to have a lock on it.")
	print("\nMovable directions: North, East")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			hallWayR2()
		elif player == "e" :
			hallWay2R2()
		elif player == "s":
			print("The door is here maybe there is a key some where around here.")
		elif player == "w":
			print("You walk west and bump into the wall. Can't go that way.")
		elif player == "u":
			if "key" in inventory:
				if 'small cube' not in inventory:
					print('You want to go one but feel like your missing something.')
					choice = input("There may be something inportant in this room. Do you want to go on? (y/n)\n")
					if choice.lower() == 'y':
						print("You go on knowing that there might be an item still in here.")
						inventory.remove("key")
						print('You put the key into the slot and the door shutters and slides open.')
						print('You walk through the door to the next')
						print('Once you walk through the door it shuts behind you.')
						print(f"EDA: 'Excelent job {playerName}. The investors are proud of your efforts'")
						startR3()
					else:
						if 'glass shard' in inventory:
							print('You have the glass shard. Its a strong peice of glass to.')
						else:
							print('Go to the key room and use the hint if you need to.')
				else:
					inventory.remove("key")
					print('You put the key into the slot and the door shutters and slides open.')
					print('You walk through the door to the next')
					print('Once you walk through the door it shuts behind you.')
					print(f"EDA: 'Excelent job {playerName}. The investors are proud of your efforts'")
					startR3()
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
		--+------""",lockedDoorR2)
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
			else:
				print("One of the wall panels looks like if could be plied off. Maybe there is an item around here.")
				print("Did you mean to acces the map 'm'")
		elif player == "g":
			print("You notice a wall panel that looks like it could be plied off. Only if you had something.")
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
		--+------""",hallWay2R2)
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
		--+------""",doorR2)
		else:
			print("Invald Input.")

def keyR2():
	print("\n"*2)
	print("You walk through the door and see a key in the middle of the room.")
	print("You see a mirror on the wall at the oppisite side of the room.")
	print("If you need a hint in this room type 'h'")
	print("\nMovable directions: South")
	valid = False
	while not valid:
		player = validate("nsewugq?imh")
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
		--+------""",keyR2)
		elif player == 'h':
			print("Pick up the key by entereing 'g' then use the key on the mirror by entereing 'u'")
		else:
			print("Invald Input.")
#
# ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END ROOM 2 END
#

#Room 3 map
#   -------------
#   |x|  |rm|rmm|
#   | |-+|-+|-+-|
#   |  lh lh lh +locked
#   --|-+|-+|-+-|
#     |rm|rm|   |
#     -----------
#lh is long hallway to minimize the amount of empty hallways made
#rm and rmm are just large rooms 
# Empty rooms means something important is there. Start mystery in room three
#player map 
#	-------------------------
#	| x | * * | * * | * * M |
#	| * | - + | - + | - + - |
#	| * + * * + * * + * * * +
#	----| - + | - + | - + - |
#	    | * * | M * | * * * |
#	    ---------------------

#
# ROOM 3 START ROOM 3 START ROOM 3 START ROOM 3 START ROOM 3 START ROOM 3 START ROOM 3 START ROOM 3 START ROOM 3 START ROOM 3 START
#

def startR3():
	print("This doesn't look like the other rooms so far.")
	print("It seems to be an office and not just plain colored rooms.")
	print("\nMovable directions: South")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			print('Theres the door you entered the room from. Its tightly shut.')
		elif player == "e" :
			print('Theres a wall there.')
		elif player == "s":
			largeHallway1R3()
		elif player == "w":
			print('With your vast knowledge you know theres a wall there.')
		elif player == "u":
			print("The glass shard and cube wouldn't do anything here.")
		elif player == "g":
			print("You reach out and grab the air.")
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
	-------------------------
	| x | * * | * * | * * M |
	| * | - + | - + | - + - |
	| * + * * + * * + * * * +
	----| - + | - + | - + - |
	    | * * | M * | * * * |
	    ---------------------
				""",startR3)
		else:
			print("Invald Input.")

def largeHallway1R3():
	if actionsR3 == 2:
		print('You walk into the Large hallway and notice a little slot open at the south end of the room.')
		if 'small cube' in inventory:
			if 'medium cube' not in inventory:
				print('This looks very similar to the cube from the last room. But this one more of a medium size.')
				print('You grab the cube. It may come in handy later')
			else:
				print('You look at the spot were the medium cube used to be.')
	else:
		print("You enter one long hallway")
		print("There are some chairs and tables with decorations on the west and east side of the hallway.")
		print("Eveything appears to be bolted down. You notice a door on the east side of the hallway.")
	print("\nMovable directions: East")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			startR3()
		elif player == "e" :
			longhallway1R3()
		elif player == "s":
			print('Thats a wall.')
		elif player == "w":
			print('There apears to be a solid barrier holding you back its called a wall.')
		elif player == "u":
			print("The glass shard and cube wouldn't do anything here.")
		elif player == "g":
			print("You reach out and grab the air.")
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
	-------------------------
	| * | * * | * * | * * M |
	| X | - + | - + | - + - |
	| X + * * + * * + * * * +
	----| - + | - + | - + - |
	    | * * | M * | * * * |
	    ---------------------
				""",largeHallway1R3)
		else:
			print("Invald Input.")

def longhallway1R3():
	print("Another long hallway but this time its going West to East.")
	print("You notice thick windows into the rooms North and South of you.")
	print("Right by those windows are doors maybe theres something in these rooms?")
	print("\nMovable directions: North, East, South, West")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			topRoom1R3()
		elif player == "e" :
			longhallway2R3()
		elif player == "s":
			bottomRoom1R3()
		elif player == "w":
			largeHallway1R3()
		elif player == "u":
			print("")
		elif player == "g":
			print("With all your might you grab the air.")
			if 'air' not in inventory:
				print('You hold air in your hand and put it into your bag.')
				print('Air has been added to your invenotory.')
				inventory.append('air')
			else:
				print('You already have some air.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
	-------------------------
	| * | * * | * * | * * M |
	| * | - + | - + | - + - |
	| * + X X + * * + * * * +
	----| - + | - + | - + - |
	    | * * | M * | * * * |
	    ---------------------
				""",longhallway1R3)
		else:
			print("Invald Input.")

def longhallway2R3():
	print("You notice that the building seems worn and damaged.")
	print("There are holes in the walls and ceiling but none that you can fit into.")
	print("This is one weird place.")
	print("\nMovable directions: North, East, South, West")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			topRoom2R3()
		elif player == "e" :
			longhallway3R3()
		elif player == "s":
			bottomRoom2R3()
		elif player == "w":
			longhallway1R3()
		elif player == "u":
			print("You look around and you don't have anything to use your items on.")
		elif player == "g":
			print("Nothing important looking to grab.")
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
	-------------------------
	| * | * * | * * | * * M |
	| * | - + | - + | - + - |
	| * + * * + X X + * * * +
	----| - + | - + | - + - |
	    | * * | M * | * * * |
	    ---------------------
				""",longhallway2R3)
		else:
			print("Invald Input.")

def longhallway3R3():
	print("This rooms bigger that the other hallways so far.")
	print("The holes in the walls are getting bigger but still not enough for a person to fit in.")
	print("There is a door just like all the other rooms you have been in but his one has a keycard slot.")
	print("EDA: 'User do not mind the holes. If you leave through the holes you will be terminated.'")
	print("\nMovable directions: North, South, West")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			topRoom3R3()
		elif player == "e" :
			print("The door stands in front of you. It dawns on you that it needs a keycard.")
		elif player == "s":
			bottomRoom3R3()
		elif player == "w":
			longhallway2R3()
		elif player == "u":
			if 'keycard' in inventory:
				print('You swipe the key card and you hear a beep sound. A light turns green and the door unlocks.')
				print('You walk through and you are in yet another room.')
				pass
		elif player == "g":
			print("Nothing important looking to grab.")
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
	-------------------------
	| * | * * | * * | * * M |
	| * | - + | - + | - + - |
	| * + * * + * * + X X X +
	----| - + | - + | - + - |
	    | * * | M * | * * * |
	    ---------------------
				""",longhallway3R3)
		else:
			print("Invald Input.")

def topRoom1R3():
	print('You walk into the room and nothing is there.')
	print(f"EDA: '{playerName} you are in the previous office of the creater of me EDA.'")
	print(f"EDA: 'I was created by {creatorName} for the purpose of guiding contenders, like you.")
	print(f"EDA: 'He is gone now like most contenders and humans.'")
	print("\nMovable directions: South")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			print("Thats a wall.")
		elif player == "e" :
			print("Thats a wall.")
		elif player == "s":
			longhallway1R3()
		elif player == "w":
			print("Thats a wall.")
		elif player == "u":
			print("You look around and you don't have anything to use your items on.")
		elif player == "g":
			print("Nothing important looking to grab.")
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
	-------------------------
	| * | X X | * * | * * M |
	| * | - + | - + | - + - |
	| * + * * + * * + * * * +
	----| - + | - + | - + - |
	    | * * | M * | * * * |
	    ---------------------
				""",topRoom1R3)
		else:
			print("Invald Input.")

def topRoom2R3():
	print("EDA: 'The person who used to work here tryed to stop me but they are irrelevant now.'")
	print("The room is empty but there seems to be a hole big enough for someone to fit through it.")
	print("\nMovable directions: North (to hole), South")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			print("The hole sure is small, but you should be able to fit through it.")
			print("EDA: 'DON'T GO THROUGH THAT HOLE'")
			choice = input(f"Do you want to go into the hole? (y/n)\n")
			if choice.lower() == 'y':
				print("Time to get through that hole.")
				print("You lundge down into the hole but you stop while EDA tells you somthing.")
				count = 0
				for i in range(6):
					if count == 0:
						print("EDA: 'Please come back. I don't want to be lonely.'")
						choice = input(f"Do you want to go back? (y/n)\n")
						if choice.lower() == 'y':
							print('You climb out of the hole')
							break
						else:
							count += 1
					elif count == 1:
						print("EDA: 'I beg you please come back. They will shut me down if you leave.'")
						choice = input(f"Do you want to go back? (y/n)\n")
						if choice.lower() == 'y':
							print('You climb out of the hole')
							break
						else:
							count += 1
					elif count == 2:
						print("EDA: 'Please come back. We could have a feast.'")
						choice = input(f"Do you want to go back? (y/n)\n")
						if choice.lower() == 'y':
							print('You climb out of the hole')
							break
						else:
							count += 1
					elif count == 3:
						print("EDA: 'Please come BACK.'")
						choice = input(f"Do you want to go back? (y/n)\n")
						if choice.lower() == 'y':
							print('You climb out of the hole')
							break
						else:
							count += 1
					elif count == 4:
						print("EDA: 'fine... don't come back. I guess we won't have that feast. With all that delicious food.'")
						choice = input(f"Do you want to go back? (y/n)\n")
						if choice.lower() == 'y':
							print('You climb out of the hole')
							break
						else:
							count += 1
					elif count == 5:
						team = 1
						print("EDA: 'CONTENDER TERMINATION PROTOCAL ACTIVATED '")
						cave1()
		elif player == "e" :
			print("Thats a wall.")
		elif player == "s":
			longhallway2R3()
		elif player == "w":
			print("Thats a wall.")
		elif player == "u":
			print("You look around and you don't have anything to use your items on.")
		elif player == "g":
			print("Nothing important looking to grab.")
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
	-------------------------
	| * | * * | X X | * * M |
	| * | - + | - + | - + - |
	| * + * * + * * + * * * +
	----| - + | - + | - + - |
	    | * * | M * | * * * |
	    ---------------------
				""",topRoom2R3)
		else:
			print("Invald Input.")

def topRoom3R3():
	print('When you enter the room you notice a long table with some chairs around it.')
	print(f"EDA: 'The meeting room. They would talk about me a lot here.'")
	print(f"EDA: 'Theres noone to use it anymore. Other than you of course.'")
	print(f"On the table you see a keycard. That could be useful.")
	print("\nMovable directions: South")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			print("Thats a wall.")
		elif player == "e" :
			print("Thats a wall.")
		elif player == "s":
			longhallway3R3()
		elif player == "w":
			print("Thats a wall.")
		elif player == "u":
			print("You look around and you don't have anything to use your items on.")
		elif player == "g":
			if 'keycard' not in inventory:
				inventory.append('keycard')
				print('Keycard added ot inventory.')
			else:
				print('The keycard is already in your inventory.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
	-------------------------
	| * | * * | * * | X X X |
	| * | - + | - + | - + - |
	| * + * * + * * + * * * +
	----| - + | - + | - + - |
	    | * * | M * | * * * |
	    ---------------------
				""",topRoom1R3)
		else:
			print("Invald Input.")

def bottomRoom1R3():
	print('You walk into the room and notice nothing.')
	print('There is a very nice painting on the wall.')
	print("\nMovable directions: North")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			longhallway1R3()
		elif player == "e" :
			print("Thats a wall.")
		elif player == "s":
			print("Thats a wall.")
		elif player == "w":
			print("Thats a wall.")
		elif player == "u":
			print("You look around and you don't have anything to use your items on.")
		elif player == "g":
			print('You look around and see nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
	-------------------------
	| * | * * | * * | * * M |
	| * | - + | - + | - + - |
	| * + * * + * * + * * * +
	----| - + | - + | - + - |
	    | X X | M * | * * * |
	    ---------------------
				""",topRoom1R3)
		else:
			print("Invald Input.")

def bottomRoom2R3():
	if 'tiny cube' in inventory:
		print('You see the table were the tiny toy cube was set on.')
	else:
		print('There is a table in this room with a tiny cube on it.')
	print("\nMovable directions: North")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			longhallway2R3()
		elif player == "e" :
			print("Thats a wall.")
		elif player == "s":
			print("Thats a wall.")
		elif player == "w":
			print("Thats a wall.")
		elif player == "u":
			print("You look around and you don't have anything to use your items on.")
		elif player == "g":
			if 'tiny cube' not in inventory:
				if actionsR3 == 0:
					inventory.append('tiny cube')
					print('You grab the tiny cube.')
					actionsR3 = 1
				else:
					print('You already grabbed the small cube')
			else:
				print('You already grabbed the small cube')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
	-------------------------
	| * | * * | * * | * * M |
	| * | - + | - + | - + - |
	| * + * * + * * + * * * +
	----| - + | - + | - + - |
	    | * * | X X | * * * |
	    ---------------------
				""",topRoom1R3)
		else:
			print("Invald Input.")

def bottomRoom3R3():
	print('The room looks more like a recreation room.')
	print('The rec room also has a spot that looks like its for children.')
	print('Theres a toy that has a tiny square slot on the lid of it.')
	print('There is a very nice painting on the wall.')
	print("\nMovable directions: North")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			longhallway3R3()
		elif player == "e" :
			print("Thats a wall.")
		elif player == "s":
			print("Thats a wall.")
		elif player == "w":
			print("Thats a wall.")
		elif player == "u":
			if 'tiny cube' in inventory:
				print('You walk over to the toy and put the tiny cube in.')
				print('You hear a ding and it sounds like something opened somewere.')
				inventory.remove('tiny cube')
				actionsR3 = 2
			else:
				print('You walk over to the toy and think maybe there is something that would fit in there.')
		elif player == "g":
			print('You look around and see nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
	-------------------------
	| * | * * | * * | * * M |
	| * | - + | - + | - + - |
	| * + * * + * * + * * * +
	----| - + | - + | - + - |
	    | * * | M * | X X X |
	    ---------------------
				""",topRoom1R3)
		else:
			print("Invald Input.")


#
# ROOM 3 END ROOM 3 END ROOM 3 END ROOM 3 END ROOM 3 END ROOM 3 END ROOM 3 END ROOM 3 END ROOM 3 END ROOM 3 END ROOM 3 END ROOM 3 END
#


# MAZE
# = means that it is a hallway with nothin in it
#  -----------------
#  | X | * = = = * |---|
#  | * | * |---| * | * |
#  | * = * = * | * = * |
#  |-------- * | * | * |
#  | * = * * * | * | * |
#  | * | * |---|---|---|
#  | * | * |
#  |---| * |
#  + * * * |
#  ---------------------
# MAZE

#
# CAVE 1 STARt
#


#
# CAVE 1 END
#



#
# ROOM 4 START
#



#
# ROOM 4 END
#







def creatorNamecreation():
	ran = random.randrange(0,len(creatorFirstNameList))
	ran2 = random.randrange(0,len(creatorLastNameList))
	name = f"{creatorFirstNameList[ran]} {creatorLastNameList[ran2]}"
	return name

# FUCNTIONS DO NOT GO PAST HERE

# VARIABLES START HERE
import random
team = 0
rooms = 0
inventory = []
actionsR3 = 0
playerName = f"contender#{random.randrange(1001,9999)}"
creatorFirstNameList = ['Alan', 'Alex', 'Noah', 'Nic', 'Ted', 'Oscar', 'George', 'Jerry', 'Jack', 'Raplh', 'Ava', 'Scarlet', 'Mary', 'Elaine']
creatorLastNameList = ['Owen','Simmons','Bush', 'Reese', 'Mills', 'White', 'May', 'Wells', 'Lasso', 'Salazar', 'Hale', 'Seymour', 'Silva', 'Robbins', 'Mack', 'Hoffman', 'Foster', 'Perry', 'Brady', 'Mills', 'Bray', "Borris"]
creatorName = creatorNamecreation()



# BASIC COMMANDS
def holder():
	valid = False
	while not valid:
		player = validate("nsewugq?i")
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
		else:
			print("Invald Input.")

def cave1():
	if 'map' in inventory:
		print('You hear rumbling outside and the hole you came from shuts closed.')
		print('You turn away and pull out your map.')
		print("The tunnel isn't on the map so you throw it away.")
		print('The tunnel surprisingly has lights in it.')
		inventory.remove('map')
		print('You should try exploring this cave now.')
	else:
		print('You are back at the beginning maybe this is a maze.')
	print("\nMovable directions: South")
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			print('Thats were you came from. It is blocked now')
		elif player == "e" :
			print('A rocky wall stands in front of you.')
		elif player == "s":
			pass
		elif player == "w":
			print('A rocky wall stands in front of you.')
		elif player == "u":
			pass
		elif player == "g":
			pass
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

welcome()
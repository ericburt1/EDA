
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
	saveToFile(room)
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
	Save (To save leave game)
		""")
	valid = False
	while valid == False:
		leave = input("Back to game (y)\n").lower()
		if leave[0] == "y":
			area()


def welcome():
	global output 
	output = input(f"""
	Welcome to EDA.

	What do you want to do?
	1) Start Game
	2) Controls
	3) Load
	4) Quit
			\n""")
	if str(output) in ("1", "start", "start game", "s"):
		start()
	elif str(output) in ("2", "controls", "c"):
		helpdisplay(welcome)
	elif str(output) in ("3", "load", "l"):
		loadFromFile()
	elif str(output) in ("4", "quit", "q"):
		quit()
	elif str(output) == "890":
		develop_testing()
	elif str(output) == "5":
		start()
	

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
		if response != '':
			if response[0] == "q":
				gamelose("You left the game :(")
			elif response[0] not in values:
				return
			elif response[0] in values:
				return response[0]
		else:
			return



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





#Room 1 Rooms start, keyR1, doorR1, fillerR1

#
# ROOM 1 START ROOM 1 START ROOM 1 START ROOM 1 START ROOM 1 START ROOM 1 START ROOM 1 START ROOM 1 START ROOM 1 START
#


def start():
	print("\n"*2)
	debugRun('start\n')
	print(f"Welcome to EDA {playerName}. If you need a reminder of controls type '?'")
	print("You are in the corner of a white room.")
	print("You notice a door south of you.")
	print("\nMoveable directions: East, South.")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			randomWallmessage()
		elif player == "e":
			keyR1()
		elif player == "s":
			doorR1()
		elif player == "w":
			randomWallmessage()
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
	debugRun('keyR1\n')
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
			randomWallmessage()
		elif player == "e" :
			randomWallmessage()
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
	debugRun('doorR1\n')
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
			randomWallmessage()
		elif player == "u":
			if "key" in inventory:
				print("You hear a click in the door. The key is stuck in the door.")
				print("The door slides open.")
				for i in range(len(inventory)):
					part = inventory[i]
					if part == "key":
						inventory.remove(inventory[i])
						info.rooms = 1
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
	debugRun('fillerR1\n')
	print("This appears to be a kitchen.")
	print("The kitchen is very clean. No food appears to be there.")
	print("\nMovable directions: North, West.")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			keyR1()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			randomWallmessage()
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

#Room 2 rooms mapR2, hallWayR2, lockedDoorR2, hallWay2R2, doorR2, keyR2

#
# ROOM 2 START ROOM 2 START ROOM 2 START ROOM 2 START ROOM 2 START ROOM 2 START ROOM 2 START ROOM 2 START ROOM 2 START
#

def mapR2():
	print("\n"*2)
	debugRun('mapR2\n')
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
			randomWallmessage()
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
	debugRun('hallWayR2\n')
	print("You walk into a hallway that appears to have nothing in it.")
	print("\nMovable directions: North, South")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			mapR2()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			lockedDoorR2()
		elif player == "w":
			randomWallmessage()
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
	debugRun('lockedDoorR2\n')
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
			randomWallmessage()
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
	debugRun('hallWay2R2\n')
	print("You are in a damp and what looks like ruined hallway.")
	print("Ceiling panels look loose. You might want to get into a different room.")
	print("One of the wall panels looks like it could be plied off. Only if you had something to ply it off with.")
	print("\nMovable directions: East, West")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			doorR2()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			lockedDoorR2()
		elif player == "u":
			if 'small cube' not in inventory:
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
	debugRun('doorR2\n')
	print("You enter a room that has a door up North.")
	print("Otherwise nothing else in this room. What is this place.")
	print("\nMovable directions: North, West")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			keyR2()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			randomWallmessage()
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
	debugRun('keyR2\n')
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
			randomWallmessage()
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

#Room 3 Rooms startR3, largeHallway1R3, longhallway1R3, longhallway2R3, longhallway3R3, topRoom1R3, topRoom2R3, topRoom3R3, bottomRoom1R3, bottomRoom2R3, bottomRoom3R3

def startR3():
	print("\n"*2)
	debugRun('startR3\n')
	print("This doesn't look like the other rooms so far.")
	print("It seems to be an office and not just plain colored rooms.")
	print("\nMovable directions: South")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			print('Theres the door you entered the room from. Its tightly shut.')
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			largeHallway1R3()
		elif player == "w":
			randomWallmessage()
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
	print("\n"*2)
	debugRun('largeHallwat1R3\n')
	if info.actionsR3 == 2:
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
			randomWallmessage()
		elif player == "w":
			randomWallmessage()
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
	print("\n"*2)
	debugRun('longhallway1R3\n')
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
			if 'Air' not in inventory:
				print('You hold air in your hand and put it into your bag.')
				print('Air has been added to your invenotory.')
				inventory.append('Air')
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
	print("\n"*2)
	debugRun('longhallway2R3\n')
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
	print("\n"*2)
	debugRun('longhallway3R3\n')
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
				print('You hear a cracking below you and you fall through the ground into a new room.')
				print('EDA: Good job user you passed Room 3. See if you can get passed the final room.')
				middleRoom()
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
	print("\n"*2)
	debugRun('topRoom1R3\n')
	print('You walk into the room and nothing is there.')
	print(f"EDA: '{playerName} you are in the previous office of the creater of me EDA.'")
	print(f"EDA: 'I was created by {creatorName} for the purpose of guiding contenders, like you.")
	print(f"EDA: 'He is gone now like most contenders and humans.'")
	print("\nMovable directions: South")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			longhallway1R3()
		elif player == "w":
			randomWallmessage()
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
	print("\n"*2)
	debugRun('topRoom2R3\n')
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
						info.team = 1
						print("EDA: 'CONTENDER TERMINATION PROTOCAL ACTIVATED '")
						cave1()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			longhallway2R3()
		elif player == "w":
			randomWallmessage()
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
	print("\n"*2)
	debugRun('topRoom3R3\n')
	print('When you enter the room you notice a long table with some chairs around it.')
	print(f"EDA: 'The meeting room. They would talk about me a lot here.'")
	print(f"EDA: 'Theres noone to use it anymore. Other than you of course.'")
	print(f"On the table you see a keycard. That could be useful.")
	print("\nMovable directions: South")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			longhallway3R3()
		elif player == "w":
			randomWallmessage()
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
	print("\n"*2)
	debugRun('bottomRoom1R3\n')
	print('You walk into the room and notice nothing.')
	print('There is a very nice painting on the wall.')
	print("\nMovable directions: North")
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			longhallway1R3()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			randomWallmessage()
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
	print("\n"*2)
	debugRun('bottomRoom2R3\n')
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
			randomWallmessage()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			print("You look around and you don't have anything to use your items on.")
		elif player == "g":
			if 'tiny cube' not in inventory:
				if info.actionsR3 == 0:
					inventory.append('tiny cube')
					print('You grab the tiny cube.')
					info.actionsR3 = 1
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
	print("\n"*2)
	debugRun('bottomRoom3R3\n')
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
			randomWallmessage()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			if 'tiny cube' in inventory:
				print('You walk over to the toy and put the tiny cube in.')
				print('You hear a ding and it sounds like something opened somewere.')
				inventory.remove('tiny cube')
				info.actionsR3 = 2
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
#  | c1| 2n= = = 3n|---|
#  | c2| 1n|---| 4n| 8n|
#  | c3= c4= 1e| 5n= 9n|
#  |-------- 2e| 6n|10n|
#  | 1s=5e 4e3e| 7n|11n|
#  | 2s| 6e|---|---|---|
#  | 3s| 7e|
#  |---| 8e|
#  +11 10 9e|
#  ---------------------
# MAZE

#
# CAVE 1 START
#

#Cave Room Rooms holder, cave1, cave2, cave3, cave4, cave5, cave1n, cave2n, cave3n, cave4n, cave5n, cave6n, cave7n, cave8n, cave9n, cave10n, cave11nGenerator, small_paper
#Cave Room Rooms continued cave1e, cave2e, cave3e, cave4e, cave5e, cave6e, cave7e, cave8e, cave9e, cave10e, cave11e, cave1s, cave3s, cave2s
# BASIC COMMANDS
def holder():
	print("\n"*2)
	debugRun('holder\n')
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
	print("\n"*2)
	debugRun('cave1\n')
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
			cave2()
		elif player == "w":
			print('A rocky wall stands in front of you.')
		elif player == "u":
			print('Nothing looks interactable.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave2():
	print("\n"*2)
	debugRun('cave2\n')
	print('You walk into another cave.')
	print('On the wall you notice a partial map in the wall.')
	print('''-----
| X |
| * |
| * =
------''')
	print('Movable directions: North, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave1()
		elif player == "e" :
			print('A rocky wall stands in front of you.')
		elif player == "s":
			cave3()
		elif player == "w":
			print('A rocky wall stands in front of you.')
		elif player == "u":
			print("Those two things don't go together.")
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave3():
	print("\n"*2)
	debugRun('cave3\n')
	print('You walk into another cave.')
	print('Looks like there is a turn in this room.')
	print('Movable directions: North, East')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave2()
		elif player == "e" :
			cave4()
		elif player == "s":
			print('A rocky wall stands in front of you.')
		elif player == "w":
			print('A rocky wall stands in front of you.')
		elif player == "u":
			print("Those two things don't go together.")
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave4():
	print("\n"*2)
	debugRun('cave4\n')
	print('You enter into another cave.')
	print('Another etching in the wall.')
	print('''-----------------
| * | 
| * | * |
| * = X = * |
---------''')
	print('Movable directions: North, East')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave1n() # this is from x going north that pathway
		elif player == "e" :
			cave1e() # this is from x going east that pathway
		elif player == "s":
			print('A rocky wall stands in front of you.')
		elif player == "w":
			print('A rocky wall stands in front of you.')
		elif player == "u":
			print("Those two things don't go together.")
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave1n():
	print("\n"*2)
	debugRun('cave1n\n')
	print('You enter into another cave.')
	print('This must be a maze.')
	print('This time there is not etching in the wall.')
	#print('''---------
#| * = 
#| X |
#= * = * |
#---------''')
	print('Movable directions: North, East')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave2n()
		elif player == "e" :
			print('A rocky wall stands in front of you.')
		elif player == "s":
			cave4()
		elif player == "w":
			print('A rocky wall stands in front of you.')
		elif player == "u":
			print("You try to use something it does not work.")
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave2n():
	print("\n"*2)
	debugRun('cave2n\n')
	if 'small paper' not in inventory:
		small_paper()
	else:
		print('You enter a small cave. There is a tunnel going East.')
		print('Movable directions: East, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			print('A rocky wall stops you from going any further.')
		elif player == "e" :
			cave5n()
		elif player == "s":
			cave1n()
		elif player == "w":
			print('A rocky wall stands in front of you.')
		elif player == "u":
			print("You try to use something it does not work.")
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave3n():
	print("\n"*2)
	debugRun('cave3n\n')
	print('You enter a small rocky room. A tunnel is going West.')
	print('Movable directions: South, West')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			print('A rocky wall stops you from going any further.')
		elif player == "e" :
			print('Something is in the way')
		elif player == "s":
			cave4n()
		elif player == "w":
			cave2n()
		elif player == "u":
			print("You try to use something it does not work.")
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave4n():
	print("\n"*2)
	debugRun('cave4n\n')
	print('You walk into the cave but now the ground is a metal grait.')
	print('You are walking on a pathway suspened over a cavern.')
	print('Movable directions: North, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave3n()
		elif player == "e" :
			print('You start walking and stop realizing you would fall into the cavern.')
		elif player == "s":
			cave5n()
		elif player == "w":
			print('You start walking and stop realizing you would fall into the cavern.')
		elif player == "u":
			print("You try to use something it does not work.")
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave5n():
	print("\n"*2)
	debugRun('cave5n\n')
	print('You enter a cave that has a crossing.')
	print('On the wall you notice some markings.')
	print('''| * | * |
| X = * |
| * | * |
	''')
	print('Movable directions: North, East, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave4n()
		elif player == "e" :
			cave9n()
		elif player == "s":
			cave6n()
		elif player == "w":
			print('A rocky wall stops you from going any further.')
		elif player == "u":
			print("You try to use something it does not work.")
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave6n():
	print("\n"*2)
	debugRun('cave6n\n')
	print('You look down into the cravern and see nothing just pure black.')
	print('Movable directions: North, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave5n()
		elif player == "e" :
			print('You can\'t go that way')
		elif player == "s":
			cave7n()
		elif player == "w":
			print('A rocky wall stops you from going any further.')
		elif player == "u":
			print("You try to use something it does not work.")
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave7n():
	print("\n"*2)
	debugRun('cave7n\n')
	print('You look on the wall and notice that there are some scratchings of words.')
	print('You can\' seem to tell what it says.')
	print('But it does look like you reached a dead end. No generator here.')
	print('Movable directions: North')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave6n()
		elif player == "e":
			print('A rocky wall stops you from going any further.')
		elif player == "s":
			print('A rocky wall stops you from going any further.')
		elif player == "w":
			print('A rocky wall stops you from going any further.')
		elif player == "u":
			print("You try to use something it does not work.")
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave8n():
	print("\n"*2)
	debugRun('cave8n\n')
	print('')
	print('Movable directions: North, East, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave4n()
		elif player == "e" :
			cave9n()
		elif player == "s":
			cave6n()
		elif player == "w":
			print('A rocky wall stops you from going any further.')
		elif player == "u":
			print("You try to use something it does not work.")
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave9n():
	print("\n"*2)
	debugRun('cave9n\n')
	print('You enter a cave that has a crossing.')
	print('On the wall you notice some markings.')
	print('''| * | * |
| * = X |
| * | * |
	''')
	print('Movable directions: North, South, West')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave8n()
		elif player == "e" :
			print('You are not able to go east.')
		elif player == "s":
			cave10n()
		elif player == "w":
			cave5n()
		elif player == "u":
			print("You try to use something it does not work.")
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave10n():
	print("\n"*2)
	debugRun('cave10n\n')
	print('You see a drawing of an arrow on a wall. It is pointing south.')
	print('There are words on the arrow. It seems to be saying Generator.')
	print('Movable directions: North, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave9n()
		elif player == "e" :
			print('You are not able to go east.')
		elif player == "s":
			cave11nGenerator()
		elif player == "w":
			print('You are not able to go west.')
		elif player == "u":
			print('No use.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave11nGenerator():
	print("\n"*2)
	debugRun('cave11nGenerator\n')
	print('You look around and see an unpowered generator.')
	print('Looks like you need to start it. Type \'u\' to activate generator.')
	print('Movable directions: North')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave10n()
		elif player == "e" :
			print('You are not able to go east.')
		elif player == "s":
			print('You can\'t go this way.')
		elif player == "w":
			print('You are not able to go west.')
		elif player == "u":
			gensOn = 0
			if info.gen1on != False:
				print('The generator is already on.\n')
			elif info.gen1on != True:
				info.gen1on = True
				print('You here a sput and the generator sparks to life.')
				if info.gen1on == True:
					gensOn += 1
				if info.gen2on == True:
					gensOn += 1
				if info.gen3on == True:
					gensOn += 1
				print(f"Generators active: {gensOn}")
				print(f"Generators left: {3 - gensOn}")


		elif player == "g":
			pass
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")
#
# CAVE 1 END
#

def small_paper():
	print('You find a small piece of paper on the ground.')
	print('It says "For one to leave the maze one must activate all three generators."')
	print('Time to start looking for some generators.')
	inventory.append('small paper')
	return

def cave1e():
	print("\n"*2)
	debugRun('cave1e\n')
	print('You enter another cave.')
	print('This one looks a little smaller than the others')
	print('Movable directions: South, East')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			cave2e()
		elif player == "w":
			cave4()
		elif player == "u":
			print('No use.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave2e():
	print("\n"*2)
	if 'small paper' not in inventory:
		small_paper()
	debugRun('cave2e\n')
	print('You enter another cave.')
	print('There\'s some bright lights in this room.')
	print('Movable directions: North, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave1e()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			cave3e()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			if 'Air' in inventory:
				print('You look in you bag and pull out the air your grabbed earlier.')
				print('You use the air on the bright lights and out of the ceiling falls a flame thrower.')
				inventory.append('Flame Thrower')
				inventory.remove('Air')
			elif 'Flame Thrower' in inventory:
				print('This is the room were you got the Flame Thrower.')
			else:
				print('No use.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave3e():
	print("\n"*2)
	debugRun('cave3e\n')
	print('You enter another cave.')
	print('This cave seems to be a bend.')
	print('Movable directions: North, West')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave2e()
		elif player == "e" :
			cave4e()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			print('Those two things don\'t go together.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave4e():
	print("\n"*2)
	debugRun('cave4e\n')
	print('You enter another cave.')
	print('A narrow long hallway.')
	print('Movable directions: East, West')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			cave3e()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			cave5e()
		elif player == "u":
			print('Those two things don\'t go together.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave5e():
	print("\n"*2)
	debugRun('cave5e\n')
	print('You enter another cave.')
	print('You aproach a crossing, and some markings on the wall.')
	print('''|-------- * |
| * = X * * |
| * | * |----''')
	print('Movable directions: East, South, West')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			cave4e()
		elif player == "s":
			cave6e()
		elif player == "w":
			cave1s()
		elif player == "u":
			print('Those two things don\'t go together.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave6e():
	print("\n"*2)
	debugRun('cave6e\n')
	print('You enter another cave.')
	print('Doesn\'t seem like there is anything of use.')
	print('Movable directions: North, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave5e()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			cave7e()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			print('Those two things don\'t go together.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave7e():
	print("\n"*2)
	debugRun('cave7e\n')
	print('You enter another cave.')
	print('You see an arrow on the wall pointing south. It says generator right under it.')
	print('Movable directions: North, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave6e()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			cave8e()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			print('Doesn\'t seem useful in this room.')
		elif player == "g":
			print('Nothing in this room is worthy of taking.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave8e():
	print("\n"*2)
	debugRun('cave8e\n')
	print('You enter another cave.')
	print('You see an arrow on the wall pointing south. It says generator right under it.')
	print('Movable directions: North, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave6e()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			cave9e()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			print('Doesn\'t seem useful in this room.')
		elif player == "g":
			print('Nothing in this room is worthy of taking.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave9e():
	print("\n"*2)
	debugRun('cave9e\n')
	if info.gen2on != True:
		print('You enter a cave with a generator in it.')
		print('You need to activate it.')
	else:
		print('This is were the second generator was.')
	print('Movable directions: North, West')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave8e()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			cave10e()
		elif player == "u":
			gensOn = 0
			if info.gen2on != False:
				print('The generator is already on.\n')
			elif info.gen2on != True:
				info.gen2on = True
				print('You here a sput and the generator sparks to life.')
				if info.gen1on == True:
					gensOn += 1
				if info.gen2on == True:
					gensOn += 1
				if info.gen3on == True:
					gensOn += 1
				print(f"Generators active: {gensOn}")
				print(f"Generators left: {3 - gensOn}")

		elif player == "g":
			print('Nothing in this room is worthy of taking.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")


def cave10e():
	print("\n"*2)
	debugRun('cave10e\n')
	print('You enter another cave.')
	print('You see light coming from the west.')
	print('Movable directions: East, West')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			cave9e()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			cave11e()
		elif player == "u":
			print('Doesn\'t seem useful in this room.')
		elif player == "g":
			print('Nothing in this room is worthy of taking.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave11e():
	print("\n"*2)
	debugRun('cave11e\n')
	print('You enter another cave.')
	print('You enter a room with a door to your east.')
	print('This must be the exit.')
	print('There is a button by the door.')
	script = f'There are three lights above the door.\n'

	if info.gen1on == True:
		script += f'The light on the left is activated.\n'
	else:
		script += f'The light on the left is off.\n'
	if info.gen2on == True:
		script += f'The light in the middle is activated.\n'
	else:
		script += f'The light in the middle is off.\n'
	if info.gen3on == True:
		script += f'The light on the right is activated.\n'
	else:
		script += f'The light on the right is off.\n'
	print(script)
	print('Movable directions: East')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			cave10e()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			if info.gen1on == True and info.gen2on == True and info.gen3on == True:
				print('You press the button by the door and you here a ding.')
				print('The doors slide open to reveal the inside of an elevator.')
				print('You walk into the elevator.')
				caveElevator()
			else:
				print('It seems that the button needs all of the lights to be on.')
		elif player == "g":
			print('Nothing in this room is worthy of taking.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave1s():
	print("\n"*2)
	debugRun('cave1s\n')
	print('You enter another cave.')
	print('You here a weird sputtering coming from the south.')
	print('Movable directions: East, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			cave5e()
		elif player == "s":
			cave2s()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			print('Doesn\'t seem useful in this room.')
		elif player == "g":
			print('Nothing in this room is worthy of taking.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave2s():
	print("\n"*2)
	debugRun('cave2s\n')
	print('The sputtering sound is getting in louder.')
	print('It seems like the sound is farther down south')
	print('Movable directions: North, South')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave1s()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			cave3s()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			print('Doesn\'t seem useful in this room.')
		elif player == "g":
			print('Nothing in this room is worthy of taking.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def cave3s():
	print("\n"*2)
	debugRun('cave2s\n')
	if info.gen3on == True:
		print('This is were you activated the 3rd generator.')
	else:
		print('You walk into an actual room it looks like the ones you started in.')
		print('The generator seems to be struggling to start.')
		print('Maybe if you try starting it again.')
	print('Movable directions: North')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			cave2s()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			gensOn = 0
			if info.gen3on != False:
				print('The generator is already on.\n')
			elif info.gen3on != True:
				info.gen3on = True
				print('You turn the generator off and try to turn it on.')
				print('You here a sput and the generator sparks to life.')
				print('It seems to be running smoothly now.')
				print('You turn to walk away and a tiny cube launches from the generator hitting you.')
				print('You turn around and take the cube.')
				if info.gen1on == True:
					gensOn += 1
				if info.gen2on == True:
					gensOn += 1
				if info.gen3on == True:
					gensOn += 1
				print(f"Generators active: {gensOn}")
				print(f"Generators left: {3 - gensOn}")
		elif player == "g":
			print('Nothing in this room is worthy of taking.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

# CAVE elevator  CAVE elevator  CAVE elevator  CAVE elevator  CAVE elevator  CAVE elevator  CAVE elevator  CAVE elevator  CAVE elevator 

def caveElevator():
	print("\n"*2)
	debugRun('caveElevator\n')
	print('The doors close behind you as you enter.')
	print('You notice that there is only one button in the elevator.')
	print('Its down.')
	valid = False
	while not valid:
		player = validate("nsewugq?i")
		if player == "n":
			print('You walk into the wall of the elevator.')
		elif player == "e" :
			print('You walk into the wall of the elevator.')
		elif player == "s":
			print('You walk into the wall of the elevator.')
		elif player == "w":
			print('You walk into the wall of the elevator.')
		elif player == "u":
			caveElevatorMoving()
		elif player == "g":
			print('Nothing in this room is worthy of taking.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		else:
			print("Invald Input.")

def caveElevatorMoving():
	print("\n"*2)
	debugRun('caveElevatorMoving\n')
	print('You pressed the button to go down.')
	print('The elevator jolts. It starts its adventure down.')
	print('Its down.')
	print('Press \'w\' to wait.')
	timewaited = 0
	valid = False
	while not valid:
		pass


# CAVE elevator  CAVE elevator  CAVE elevator  CAVE elevator  CAVE elevator  CAVE elevator  CAVE elevator  CAVE elevator  CAVE elevator 



#Cave Room Rooms continued cave1e, cave2e, cave3e, cave4e, cave5e, cave6e, cave7e, cave8e, cave9e, cave10e, cave11e, cave1s, cave3s, cave2s

#Generators are going to be 11n 3s and 9e or 3e

# MAZE
# = means that it is a hallway with nothin in it
#  -----------------
#  | c1| 2n= = = 3n|---|
#  | c2| 1n|---| 4n| 8n|
#  | c3= c4= 1e| 5n= 9n|
#  |-------- 2e| 6n|10n|
#  | 1s=5e 4e3e| 7n|11n|
#  | 2s| 6e|---|---|---|
#  | 3s| 7e|
#  |---| 8e|
#  +11 10 9e|
#  ---------------------
# MAZE


#
# ROOM 4 START
#

# Map of room

#---------   ---------
#| * | * |   | * | * |
#| + - + ----- + - + -
#| * * * + * + * * * |
#--------- + ---------

def holder():
	print("\n"*2)
	debugRun('holder\n')
	print('Movable directions: North, South')
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
		---------   ---------
		| * | * |   | * | * |
		| + - + ----- + - + -
		| * * * + X + * * * |
		--------- + ---------
				""",holder)
		else:
			print("Invald Input.")

def middleRoom():
	print("\n"*2)
	debugRun('middleRoom\n')
	print('You are standing on the rubble from when you fell through the floor.')
	print('North of you is a window looking out into a city.')
	print('Movable directions: East, West')
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			rightHallway1()
		elif player == "s":
			print('It says you need to switch 4 levers for the door to open.')
		elif player == "w":
			leftHallway1()
		elif player == "u":
			if info.__leverl1 == True and info.__leverl2 == True and info.__leverr1 == True and info.__leverr2 == True:
				print('You activated all of the levers.')
				print('When you open the door there is an elevator, you walk in it.')
			else:
				print('One or more of the levers is not activated.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------   ---------
		| * | * |   | * | * |
		| + - + ----- + - + -
		| * * * + X + * * * |
		--------- + ---------
				""",middleRoom)
		else:
			print("Invald Input.")

def leftHallway1():
	print("\n"*2)
	debugRun('leftHallway1\n')
	print('You seem to be in a very nice office building.')
	print('A door is to your north.')
	print('Movable directions: North, East, West')
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			leftRoom1()
		elif player == "e" :
			middleRoom()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			leftHallway2()
		elif player == "u":
			print('No use.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------   ---------
		| * | * |   | * | * |
		| + - + ----- + - + -
		| * * X + * + * * * |
		--------- + ---------
				""",leftHallway1)
		else:
			print("Invald Input.")

def leftHallway2():
	print("\n"*2)
	debugRun('leftHallway2\n')
	print('On the wall there is a empty frame. It looks like something was riped from it.')
	print('Movable directions: East, West')
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			leftHallway1()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			leftHallway3()
		elif player == "u":
			print('No use.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------   ---------
		| * | * |   | * | * |
		| + - + ----- + - + -
		| * X * + * + * * * |
		--------- + ---------
				""",leftHallway2)
		else:
			print("Invald Input.")

def leftHallway3():
	print("\n"*2)
	debugRun('leftHallway3\n')
	print('A door is to your north.')
	print('Movable directions: North, East')
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			leftRoom1()
		elif player == "e" :
			leftHallway2()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			print('No use.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------   ---------
		| * | * |   | * | * |
		| + - + ----- + - + -
		| X * * + * + * * * |
		--------- + ---------
				""",leftHallway3)
		else:
			print("Invald Input.")

def leftRoom1():
	print("\n"*2)
	debugRun('leftRoom1\n')
	if info.__leverl1 == False:
		print(f"There is a lever in the middle of the room. There is a red light by it.")
	elif info.__leverl1 == True:
		print('You already pulled the lever in this room. There is a green light by the switch.')
	print('Movable directions: North, East')
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			leftHallway1()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			if info.__leverl1 != True:
				info.__leverl1 = True
				print('You pull the lever and the red light switchs to green.')
			else:
				print('You already pulled the lever.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------   ---------
		| * | X |   | * | * |
		| + - + ----- + - + -
		| * * * + * + * * * |
		--------- + ---------
				""",leftRoom1)
		else:
			print("Invald Input.")

def leftRoom2():
	print("\n"*2)
	debugRun('leftRoom2\n')
	print('There are some windows that look out to the city. That\'s wierd not a single other buildings have lights on.')
	if info.__leverl2 == False:
		print(f"There is a lever in the middle of the room. There is a red light by it.")
	elif info.__leverl2 == True:
		print('You already pulled the lever in this room. There is a green light by the switch.')
	print('Movable directions: North, East')
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			leftHallway3()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			if info.__leverl2 != True:
				info.__leverl2 = True
				print('You pull the lever and the red light switchs to green.')
			else:
				print('You already pulled the lever.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------   ---------
		| X | * |   | * | * |
		| + - + ----- + - + -
		| * * * + * + * * * |
		--------- + ---------
				""",leftRoom2)
		else:
			print("Invald Input.")

def rightRoom1():
	print("\n"*2)
	debugRun('rightRoom1\n')
	print('There are some windows on the wall.')
	print('There are cars on the road but not a single one is moving.')
	if info.__leverr1 == False:
		print(f"There is a lever in the middle of the room. There is a red light by it.")
	elif info.__leverr1 == True:
		print('You already pulled the lever in this room. There is a green light by the switch.')
	print('Movable directions: North, East')
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			rightHallway1()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			if info.__leverr1 != True:
				info.__leverr1 = True
				print('You pull the lever and the red light switchs to green.')
			else:
				print('You already pulled the lever.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------   ---------
		| * | * |   | X | * |
		| + - + ----- + - + -
		| * * * + * + * * * |
		--------- + ---------
				""",rightRoom1)
		else:
			print("Invald Input.")

def rightRoom2():
	print("\n"*2)
	debugRun('rightRoom2\n')
	print('One of the windows is broken. You should stay clear of it.')
	if info.__leverr2 == False:
		print(f"There is a lever in the middle of the room. There is a red light by it.")
	elif info.__leverr2 == True:
		print('You already pulled the lever in this room. There is a green light by the switch.')
	print('Movable directions: North, East')
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			rightHallway3()
		elif player == "w":
			randomWallmessage()
		elif player == "u":
			if info.__leverr2 != True:
				info.__leverr2 = True
				print('You pull the lever and the red light switchs to green.')
			else:
				print('You already pulled the lever.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------   ---------
		| * | * |   | * | X |
		| + - + ----- + - + -
		| * * * + * + * * * |
		--------- + ---------
				""",rightRoom2)
		else:
			print("Invald Input.")

def rightHallway1():
	print("\n"*2)
	debugRun('rightHallway1\n')
	print('A door is to your north.')
	print('The carpet here is riped to shreds.')
	print('Movable directions: North, East, West')
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			rightRoom1()
		elif player == "e" :
			rightHallway2()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			middleRoom()
		elif player == "u":
			print('No use.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------   ---------
		| * | * |   | * | * |
		| + - + ----- + - + -
		| * * * + * + X * * |
		--------- + ---------
				""",rightHallway1)

def rightHallway2():
	print("\n"*2)
	debugRun('rightHallway2\n')
	print('This room seems to be really ripped upped.')
	print('Movable directions: East, West')
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			randomWallmessage()
		elif player == "e" :
			rightHallway3()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			rightHallway2()
		elif player == "u":
			print('No use.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------   ---------
		| * | * |   | * | * |
		| + - + ----- + - + -
		| * * * + * + * X * |
		--------- + ---------
				""",rightHallway2)

def rightHallway3():
	print("\n"*2)
	debugRun('rightHallway3\n')
	print('A door is to your north.')
	print('The East wall is missing and you can see the city below.')
	print('Movable directions: North, West')
	valid = False
	while not valid:
		player = validate("nsewugq?im")
		if player == "n":
			rightRoom2()
		elif player == "e" :
			randomWallmessage()
		elif player == "s":
			randomWallmessage()
		elif player == "w":
			middleRoom()
		elif player == "u":
			print('No use.')
		elif player == "g":
			print('There is nothing to grab.')
		elif player == "?":
			helpdisplay()
		elif player == "i":
			displayInventory()
		elif player == "m":
			if "map" in inventory:
				displayMap("""
		---------   ---------
		| * | * |   | * | * |
		| + - + ----- + - + -
		| * * * + * + * * X |
		--------- + ---------
				""",rightHallway3)


#
# ROOM 4 END
#







def creatorNameCreating():
	ran = random.randrange(0,len(creatorFirstNameList))
	ran2 = random.randrange(0,len(creatorLastNameList))
	creatorName = f"{creatorFirstNameList[ran]} {creatorLastNameList[ran2]}"
	return creatorName

# FUCNTIONS DO NOT GO PAST HERE

class informationToSave(object):

	def __init__(self):
		self.__team = 0
		self.__rooms = 0
		self.__actionsR3 = 0
		self.__gen1on = False
		self.__gen2on = False
		self.__gen3on = False
		self.__leverl1 = False
		self.__leverl2 = False
		self.__leverr1 = False
		self.__leverr2 = False


	def __str__(self):
		printer = f'This is some saved data:'
		printer += f'Your team is {self.__team}\n'
		printer += f'Your rooms is {self.__rooms}\n'
		printer += f'Your actionsR3 is {self.__actionsR3}\n'
		printer += f'Generator 1 is {self.__gen1on}\n'
		printer += f'Generator 2 is {self.__gen2on}\n'
		printer += f'Generator 3 is {self.__gen3on}\n'
		printer += f'Lever L1 pulled {self.__leverl1}\n'
		printer += f'Lever L2 pulled {self.__leverl2}\n'
		printer += f'Lever R1 pulled {self.__leverr1}\n'
		printer += f'Lever R2 pulled {self.__leverr2}\n'
		return printer

	@property
	def team(self):
		return self.__team
	
	@property
	def gen1on(self):
		return self.__gen1on
	
	@property
	def gen2on(self):
		return self.__gen2on
	
	@property
	def gen3on(self):
		return self.__gen3on

	@property
	def rooms(self):
		return self.__rooms
	
	@property
	def actionsR3(self):
		return self.__actionsR3
	
	@team.setter
	def team(self, newTeam):
		if newTeam == 1:
			self.__team = newTeam

	@rooms.setter
	def rooms(self, newRooms):
		if newRooms == 1:
			self.__rooms = newRooms

	@actionsR3.setter
	def actionsR3(self, actions):
		self.__actionsR3 = actions

	@gen1on.setter
	def gen1on(self, on):
		if self.__gen1on != on:
			self.__gen1on = on

	@gen2on.setter
	def gen2on(self, on):
		if self.__gen2on != on:
			self.__gen2on = on

	@gen3on.setter
	def gen3on(self, on):
		if self.__gen3on != on:
			self.__gen3on = on

# VARIABLES START HERE
import random, pickle

inventory = []
output = 0
room = 'start\n'

creatorFirstNameList = ['Alan', 'Alex', 'Noah', 'Nic', 'Ted', 'Oscar', 'George', 'Jerry', 'Jack', 'Raplh', 'Ava', 'Scarlet', 'Mary', 'Elaine']
creatorLastNameList = ['Owen','Simmons','Bush', 'Reese', 'Mills', 'White', 'May', 'Wells', 'Lasso', 'Salazar', 'Hale', 'Seymour', 'Silva', 'Robbins', 'Mack', 'Hoffman', 'Foster', 'Perry', 'Brady', 'Mills', 'Bray', "Borris"]
wallMessages = ['You walk into a wall.', 'A wall stops you from going any further.', 'With your vast knowledge you know theres a wall there.', "You try walking through the wall. It doesn't work very well.", "As you walk that way you notice you aren't moving.", "You walk over and bump into the wall. Can't go that way.", "There is a wall that way, no use going there.", "There's a wall there.", "That's a wall.", "There appears to be a solid barrier holding you back its called a wall."]
creatorName = creatorNameCreating()
playerName = f"contender#{random.randrange(1001,9999)}"

def debugRun(area):
	global room 
	room = area
	if output == 5:
		print(area)
		return
	else:
		return
	
def randomWallmessage():
	randomNum = random.randrange(0,len(wallMessages))
	print(wallMessages[randomNum])
	return

def saveToFile(room):
	with open('game.dat','wb') as f:
		pickle.dump(inventory,f)
		pickle.dump(room,f)
		pickle.dump(playerName,f)
		pickle.dump(creatorName,f)
		pickle.dump(info,f)
	print("Game saved!")

def loadFromFile():
	global room, inventory, playerName, creatorName, info, gensActivated
	try:
		with open("game.dat",'rb') as f:
			inventory = pickle.load(f)
			room = pickle.load(f)
			playerName = pickle.load(f)
			creatorName = pickle.load(f)
			info = pickle.load(f)
			if [] in inventory:
				inventory.remove([])
		print("Game loaded!")
		function_dict[room]()
	except FileNotFoundError:
		print("Game file not found!")

#Put all rooms names in here. Like start. 
#Room 1 Rooms start, keyR1, doorR1, fillerR1
#Room 2 rooms mapR2, hallWayR2, lockedDoorR2, hallWay2R2, doorR2, keyR2
#Room 3 Rooms startR3, largeHallway1R3, longhallway1R3, longhallway2R3, longhallway3R3, topRoom1R3, topRoom2R3, topRoom3R3, bottomRoom1R3, bottomRoom2R3, bottomRoom3R3
#Cave Room Rooms holder, cave1, cave2, cave3, cave4, cave5, cave1n, cave2n, cave3n, cave4n, cave5n, cave6n, cave7n, cave8n, cave9n, cave10n, cave11nGenerator, small_paper
                                                                                                                                                                                                                                                                                                                   #Cave Room Rooms continued cave1e, cave2e, cave3e, cave4e, cave5e, cave6e, cave7e, cave8e, cave9e, cave10e, cave11e, cave1s, cave3s, cave2s

function_dict = {'start\n':start, 'keyR1\n':keyR1, 'doorR1\n':doorR1, 'fillerR1\n':fillerR1, 
		 		'mapR2\n':mapR2, 'hallWayR2\n':hallWayR2, 'lockedDoorR2\n':lockedDoorR2, 'hallWay2R2\n':hallWay2R2, 'doorR2\n':doorR2, 'keyR2\n':keyR2,
				'startR3\n':startR3, 'largeHallway1R3\n':largeHallway1R3, 'longhallway1R3\n':longhallway1R3, 'longhallway2R3\n':longhallway2R3, 'longhallway3R3\n':longhallway3R3, 'topRoom1R3\n':topRoom1R3, 'topRoom2R3\n':topRoom2R3, 'topRoom3R3\n':topRoom3R3, 'bottomRoom1R3\n':bottomRoom1R3, 'bottomRoom2R3\n':bottomRoom2R3, 'bottomRoom3R3\n':bottomRoom3R3,
				'cave1\n':cave1, 'cave2\n':cave2, 'cave3\n':cave3, 'cave4\n':cave4, 'cave5\n':mapR2, 'cave1n\n':cave1n, 'cave2n\n':cave2n, 'cave3n\n':cave3n, 'cave4n\n':cave4n, 'cave5n\n':cave5n, 'cave6n\n':cave6n, 'cave7n\n':cave7n, 'cave8n\n':cave8n, 'cave9n\n':cave9n, 'cave10n\n':cave10n, 'cave11nGenerator\n':cave11nGenerator, 'small_paper\n':small_paper, 'cave1e\n':cave1e, 'cave2e\n':cave2e, 'cave3e\n':cave3e, 'cave4e\n':cave4e, 'cave5e\n':cave5e, 'cave6e\n':cave6e, 'cave7e\n':cave7e, 'cave8e\n':cave8e, 'cave9e\n':cave9e, 'cave10e\n':cave10e, 'cave11e\n':cave11e, 'cave1s\n':cave1s, 'cave2s\n':cave2s, 'cave3s\n':cave3s, 
				'caveElevator\n' : caveElevator, 'caveElevatorMoving\n': caveElevatorMoving,
				'middleRoom': middleRoom, 'leftHallway1\n': leftHallway1, 'leftHallway2\n': leftHallway2, 'leftHallway3\n': leftHallway3, 'leftRoom1\n': leftRoom1, 'leftRoom2\n': leftRoom2, 'rigthHallway1\n': rightHallway1, 'rigthHallway2\n': rightHallway2, 'rigthHallway3\n': rightHallway3, 'rightRoom1\n': rightRoom1, 'rightRoom2\n': rightRoom2,
				}
info = informationToSave()

welcome()




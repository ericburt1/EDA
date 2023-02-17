
inventory = []


def holder():
	player = validate("nsewugq?h")
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
		pass
	elif player == "i":
		displayInventory()
	else:
		print("That is not possible.")

		
#Room one layout each set of parenthasis is an area with its functon ame 
#(start)(keyR1)
#(c1r2) (c1r2)
#(doorR1)

def gamelose(cause):
	print("\n"*5)
	print(cause)
	print("Game over!")
	quit()

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
	Inventory (i)
	Help (?)
		""")
	leave = input("Back to game (y)")
	valid = False
	while valid == False:
		leave = input("Back to game (y)").lower()
		if leave[0] == "y":
			area()



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
		if response[0] == "i":
			displayInventory()
			return
		elif response[0] == "q":
			gamelose("You left the game :(")
		elif response[0] in values:
			return response

def start():
	valid = False
	while not valid:
		print("\n"*2)
		print("Welcome to EDA USER. If you need a reminder of controls type '?'")
		print("You are in the corner of a white room.")
		print("You notice a door south of you.")
		print("\nMoveable directions: East, South.")
		player = validate("nsewugq?i")
		started = True
		if player == "n":
			print("You walk north into a wall.")
		elif player == "e":
			print("You move east.")
			keyR1()
		elif player == "s":
			print("You move south.")
		elif player == "w":
			print("You walk west into a wall.")
		elif player == "u":
			print("You go ignore what is happeneding around you and go back to sleep")
			gamelose("You went to sleep and woke up in your house.")
		elif player == "g":
			print("You look around and don't see anything to pick up.")
		elif player == "?":
			helpdisplay(start)
		elif player == "q":
			gamelose("You left the game :(")
		elif player == "i":
			displayInventory()
		else:
			print("Invalid Input.")


def keyR1():
	print("You look around and see an empty area other than ...")
	print("a key this may come in handy.")
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
			if "key" in inventory:
				print("You already picked up the key!!")
			else:
				inventory.append("key")
		elif player == "?":
			pass
		else:
			print("Invald Input.")

def displayInventory():
	print("Inventory:\n")
	for i in range(len(inventory)):
		part = inventory[i]
		print(f"{i+1}: {part}")
	print()
	return

# FUCNTIONS DO NOT GO PAST HERE


# VARIABLES START HERE
started = False


welcome()
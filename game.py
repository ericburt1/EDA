# 0's are where player gets no movement. 3 is the player. 1 is moveable spots
rooms = [0,0,0,0,0,0,0,0,0,0,0,
		 0,3,0,0,0,0,0,0,0,0,0,
		 0,1,0,0,0,0,0,0,0,0,0,
		 0,1,1,1,1,1,1,1,1,0,0,
		 0,1,1,1,1,1,1,1,1,0,0,
		 0,1,1,1,1,1,1,1,1,0,0,
		 0,1,1,1,1,1,1,1,1,0,0,
		 0,0,0,0,0,0,0,0,0,0,0]
playerInput = int(input(f"""
	Welcome to EDA.

	What do you want to do?
	1) Start Game
	q) Quit
		\n"""))

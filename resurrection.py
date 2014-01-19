#imports

#maps

memories_map = [
	(
"""You step out with Death from the warm office into a place that smells distinctly like dust and dry paper, utterly devoid of sound. Until Death says 'This corridor is an offshoot of the Maze of Memories. The memories of the dead exist here - in theory this place contains the memories we need.'""", "First Corridor of maze"), #0
	(
"""Death leads the way down the corridor to a dead end. 'Let me just...' and with one sweep of an arm, a word appears on the wall. """, "FirstPuzzle"), #1
]


#word puzzles


#main gameloop

while True:
	command = raw_input("> ")

	if command == "exit" or command == "quit":
		break
	

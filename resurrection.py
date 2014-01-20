#imports

#maps

memories_map = [
	(
"""You step out with Death from the warm office into a place that smells distinctly like dust and dry paper, utterly devoid of sound. Until Death says 'This corridor is an offshoot of the Maze of Memories. The memories of the dead exist here - in theory this place contains the memories we need.'""", "First Corridor of maze"), #0
	(
"""Death leads the way down the corridor to a dead end. 'Let me just...' and with one sweep of an arm, a word appears on the wall. 'shcaneg vreen arw. It's a prhase that got jumbled up. If we can solve it, the wall will open. Get to it, assistant. We don't have eternity. Well, we do, but I have better places to spend it in rather than here.' Death mutters impatiently.""", "Corridor Part 1"), #1
	(
"""The next section of corridor is revealed, the dust beyond unsettled by the collapse of the wall.""", "Corridor Part 2"), #2
	(
"""Again, you happen upon a dead end. Another sweep of an arm, and another jumbled word appears on the wall. 'ro lhle naheev. Another jumbled word. You know what to do, assistant. """, "Corridor Part 3"), #3
	(
"""""", "") #4
]


#word puzzles


#main gameloop

print """		Welcome to Resurrection.

The player takes on the role of one of Death's assistants. Since the introduction of 'extra lives', Death has had to take on help in order to recover those that need to be sent back to the living.

This is your first day on the job - and you have to go find the three parts that make up this one person who has an extra chance. To resurrect someone, you need to find their memories, their flesh and their passion for life. You won't be alone - Death will be right along with you, ensuring you get the job done, and done well."""

while True:
	command = raw_input("> ")

	if command == "help":
		print """help: brings up list of commands
exit, quit: quit the game.
up: move up
down: move down
right: move right
left: move left
"""

	if command == "exit" or command == "quit":
		break
	

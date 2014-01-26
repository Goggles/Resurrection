#imports

#maps

main_map = [
	(
"""You step out with Death from the warm office into a place that smells distinctly like dust and dry paper, utterly devoid of sound. Until Death says 'This corridor is an offshoot of the Maze of Memories. The memories of the dead exist here - in theory this place contains the memories we need.'""", "0"), #0
	(
"""Death leads the way down the corridor to a dead end. 'Let me just...' and with one sweep of an arm, a word appears on the wall. 'shcaneg vreen arw. It's a prhase that got jumbled up. If we can solve it, the wall will open. Get to it, assistant. We don't have eternity. Well, we do, but I have better places to spend it in rather than here.' Death mutters impatiently.""", "1"), #1
	(
"""The next section of corridor is revealed, the dust beyond unsettled by the collapse of the wall.""", "2"), #2
	(
"""Again, you happen upon a dead end. Another sweep of an arm, and another jumbled word appears on the wall. 'ro lhle naheev. Another jumbled word. You know what to do, assistant. """, "3"), #3
	(
"""This wall also crumbles away to nothingness, this time revealing a small book just inside. 'These would be the memories we seek.' Death picks up the book and stashes it away somewhere in their robes. 'To the next destination - the Labyrith of Flesh.' A portal opens, and you follow Death through it to the next area.""", "4"), #4
	(
"""Out of the portal you and Death step, straight into a place that seems to made up of quivering masses of flesh. 'Distasteful, isn't it? The first Death took the idea of a realm for the flesh of the dead a little too literally. Watch your step, the whole place is alive.' With that said, Death walks on forward to what looks like a massive artery - big enough for a bus to go through with room to spare.""", "5"), #5
	(
"""You both stop before a membrane blocking the corridor. A mess of characters are carved into the thin barrier. 'taalfyti. Yet another anagram. Let us hope it is the last...'""", "6"), #6
	(
"""The membrane explodes, splattering blood and pieces of itself onto both yourself and Death. '...I forgot that happens. Come along, the body we seek will be in here. Attempting to wipe the remains of the wall from your person, you follow Death down the staircase formed of tight muscle. At the foot of the staircase is a small altar that looks suspiciously like a hollowed out uterus. 'The original Death also took certain ideas too far...' your boss mutters under his breath. 'Take the bag you'll find in that...thing. Try not to think too much about what you're doing, I don't want you to suddenly puke and the realm we're in to take offence.' You put your arm into the altar and feel around for a small bag. 'Got it? Good. To the Realm of Spirit and Passion.' With that, you and Death warp away to the next destination.""", "7"), #7
	(
"""Suddenly, you and Death are standing in a long corridor. The floor is covered in a thin layer of mist. The mist keeps changing colour - from white to a deep red, to a light blue and back again. Death motions for you to follow them down the corridor until he pauses. Some of the mist rises and forms into the shape of a heart - which starts moving around in a jerky fashion. Faintly, you hear a voice saying 'ghhi' repeatedly. 'Say the actual word! It's another puzzle! Say the true word and it will be stunned!' Death is now holding a butterfly net in one hand, intently watching the fast-moving mist-heart.""", "8"), #8
	(
"""The mist-heart freezes as you utter the right word. Death captures it quickly with the butterfly net. 'One down. Let us find the others.' You both continue down the corridor, waiting for another mist-heart to appear.""", "9"), #9
	(
"""'wlo. wlo. wlo.' The voice echos around you both, as another mist-heart is formed. 'Stun it, assistant!' Death readies the butterfly net again.""", "10"), #10
	(
"""The net swiftly contains this mist-heart as well. 'This is extremely simple...'""", "11"),

]


#main gameloop

print """		Welcome to Resurrection.

The player takes on the role of one of Death's assistants. Since the introduction of 'extra lives', Death has had to take on help in order to recover those that need to be sent back to the living.

This is your first day on the job - and you have to go find the three parts that make up this one person who has an extra chance. To resurrect someone, you need to find their memories, their flesh and their passion for life. You won't be alone - Death will be right along with you, ensuring you get the job done, and done well."""

while True:
	command = raw_input("> ")

	if command == "help":
		print """help: brings up list of commands
exit, quit: quit the game.
"""

	if command == "exit" or command == "quit":
		break
	

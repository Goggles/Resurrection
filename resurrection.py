#imports

#maps

main_map = [

"""You step out with Death from the warm office into a place that smells distinctly like dust and dry paper, utterly devoid of sound.

Until Death says 'This corridor is an offshoot of the Maze of Memories. The memories of the dead exist here - in theory, here contains the memories we need.'
""", #0
	
"""Death leads the way down the corridor to a dead end. 'Let me just...' and with one sweep of an arm, a word appears on the wall.

'Shcaneg vreen arw. It's a prhase that got jumbled up. If we can solve it, the wall will open. Get to it, assistant. We don't have eternity. Well, we do, but I have better places to spend it in rather than here.' Death mutters impatiently.
""", #1
	
"""The next section of corridor is revealed, the dust beyond unsettled by the collapse of the wall.
""", #2
	
"""Again, you happen upon a dead end. Another sweep of an arm, and another jumbled word appears on the wall. 'ro lhle naheev. Another jumbled word. You know what to do, assistant.'
""", #3
	
"""This wall also crumbles away to nothingness, revealing a small book just inside. 'These would be the memories we seek.' Death picks up the book and stashes it away somewhere in their robes.

'To the next destination - the Labyrith of Flesh.' A portal opens, and you follow Death through it to the next area.
""", #4
	
"""Out of the portal you and Death step, straight into a place that seems to made up of quivering masses of flesh.

'Distasteful, isn't it? The first Death took the idea of a realm for the flesh of the dead a little too literally. Watch your step, the whole place is alive.' With that said, Death walks on forward to what looks like a massive artery - big enough for a bus to go through with room to spare.
""", #5
	
"""You both stop before a membrane blocking the corridor. A mess of characters are carved into the thin barrier. 'taalfyti. Yet another anagram. Let us hope it is the last...'
""", #6
	
"""The membrane explodes, splattering blood and pieces of itself onto both yourself and Death. '...I forgot that happens. Come along, the body we seek will be in here.'

Attempting to wipe the remains of the wall from your person, you follow Death down the staircase formed of tight muscle. At the foot of the staircase is a small altar that looks suspiciously like a hollowed out uterus. 'The original Death also took certain ideas too far...' your boss mutters under his breath.

'Take the bag you'll find in that...thing. Try not to think too much about what you're doing, I don't want you to suddenly puke and the realm we're in to take offence.' You put your arm into the altar and feel around for a small bag. 'Got it? Good. To the Realm of Spirit and Passion.' With that, you and Death warp away to the next destination.
""", #7
	
"""Suddenly, you and Death are standing in a long corridor. The floor is covered in a thin layer of mist. The mist keeps changing colour - from white to a deep red, to a light blue and back again. Death motions for you to follow them down the corridor until he pauses.

Some of the mist rises and forms into the shape of a heart - which starts moving around in a jerky fashion. Faintly, you hear a voice saying 'ghhi' repeatedly. 'Say the actual word! It's another puzzle! Say the true word and it will be stunned!' Death is now holding a butterfly net in one hand, intently watching the fast-moving mist-heart.
""", #8
	
"""The mist-heart freezes as you utter the right word. Death captures it quickly with the butterfly net. 'One down. Let us find the others.' You both continue down the corridor, waiting for another mist-heart to appear.
""", #9
	
"""'wlo. wlo. wlo.' The voice echos around you both, as another mist-heart is formed. 'Stun it, assistant!' Death readies the butterfly net again.
""", #10
	
"""The net swiftly contains this mist-heart as well. 'This is extremely simple...'
""", #11
	
"""'Is that it? There's usually more to a person's spirit...' Death mutters. You both warily walk down the mist-ridden corridor, until you happen upon a figure made up of mist.

It stumbles towards you both, arms outstretched, moaning 'idlmde. idlmde. idlmde!' Death steps forward, brandishing the iconic scythe. 'Work out the true word. Quickly now!'
""", #12
	
"""As you utter the true word, the figure's right arm breaks away and forms into a mist-heart. Death sweeps forward and catches it, dodging a lunging attack from the mist-figure. 'klbco...klbco...' the mist-monster intones.
""", #13
	
"""The left arm of the mist-figure breaks off and forms into a mist-heart - like the previous limb. The figure howls in pain - 'ujpm, ujpm, ujpm!' 'Say the true word, then we get the final piece!' Death yells while capturing the mist-heart.
""", #14
	
"""It freezes, then reforms into a giant mist-heart. Death grabs it and stashes it away somewhere in his vast robes. 'We have everything. We can now resurrect this person and send them back.' And with that, Death warps both of you away.
""", #15
	
"""You both stumble into the Resurrection Chamber and lock the door behind you. Death releases the mist-hearts while you open the book of memories and the bag of flesh.

Death mutters some incantation, and all the items meld together to create a person - a muscular man with spiky hair, tattoos and wearing only a pair of trousers and small amounts of armour. 'Well, let's send him on his way...'. With a flick of the wrist, Death warped the young man away.

'Wonder how he'll get on.' A crystal ball, stood near the door, showed an arena - where the young man they just revived started fighting a girl in a chinese-style dress. After a few blows, the man was on the floor, bleeding profusely. 'Thankfully that was his last life. Didn't want to go through the hassle of fetching him again...'

			~The End~
""" #16

]


#main gameloop

print """		Welcome to Resurrection.

The player takes on the role of one of Death's assistants. Since the introduction of 'extra lives', Death has had to take on help in order to recover those that need to be sent back to the living.

This is your first day on the job - and you have to go find the three parts that make up this one person who has an extra chance. To resurrect someone, you need to find their memories, their flesh and their passion for life. You won't be alone - Death will be right along with you, ensuring you get the job done, and done well.
"""

#print main_map[0]
count = 0

while True:
	print main_map[count]
	command = raw_input("> ")

	if command == "help":
		print """help: brings up list of commands
exit, quit: quit the game.
"""

	if command == "exit" or command == "quit":
		break


	if count == 1:
		if command == "war never changes":
			count += 1
		else:
			print "Nothing happens.\n"
	elif count == 3:
		if command == "heaven or hell":
			count += 1
		else:
			print "Nothing happens.\n"
	elif count == 6:
		if command == "fatality":
			count += 1
		else:
			print "Nothing happens.\n"
	elif count == 8:
		if command == "high":
			count += 1
		else:
			print "Nothing happens.\n"
	elif count == 10:
		if command == "low":
			count += 1
		else:
			print "Nothing happens.\n"
	elif count == 12:
		if command == "middle":
			count += 1
		else: 
			print "Nothing happens.\n"
	elif count == 13:
		if command == "block":
			count += 1
		else:
			print "Nothing happens.\n"
	elif count == 14:
		if command == "jump":
			count += 1
		else:
			print "Nothing happens.\n" 
	elif count == 16:
		break
	else:
		count += 1

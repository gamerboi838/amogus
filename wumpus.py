import random
world =         [[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]]
row = random.randint(0, 4)
col = random.randint(0, 4)
world[row][col] = 'w'
needit = True
i=3
while i!=0:
	row = random.randint(0, 4)
	col = random.randint(0, 4)
	if world[row][col] == 0:
		world[row][col] = 'p'
		i-=1
		if(i==3):
			needit = False
needit = True
while needit:
	row = random.randint(0, 4)
	col = random.randint(0, 4)
	if world[row][col] == 0:
		world[row][col] = 'g'
		needit = False
needit = True
while needit:
	row = random.randint(0, 4)
	col = random.randint(0, 4)
	if world[row][col] == 0:
		userRow = row
		userCol = col
		needit = False
arrows = 5
alive = True
while alive:
	for item in world:
		print(item)
	print('You are at row ' + str(userRow) + ' and col ' + str(userCol) + '.')
	if world[(userRow - 1)%5][userCol] == 'w' or world[(userRow + 1)%5][userCol] == 'w' or world[userRow][(userCol - 1)%5] == 'w' or \
					world[userRow][(userCol + 1)%5] == 'w':
		print('I smell Wumpus...')
	if world[(userRow - 1)%5][userCol] == 'p' or world[(userRow + 1)%5][userCol] == 'p' or world[userRow][(userCol - 1)%5] == 'p' or \
					world[userRow][(userCol + 1)%5] == 'p':
		print('I feel a draft...  (You are near a pit)')
	if world[(userRow - 1)%5][userCol] == 'g' or world[(userRow + 1)%5][userCol] == 'g' or world[userRow][(userCol - 1)%5] == 'g' or \
					world[userRow][(userCol + 1)%5] == 'g':
		print('I see gold dust...  (You are near gold)')
	print('What do you want to do next?')
	print('You can type "n", "s", "e", or "w" to move, or "f" to fire an arrow.')
	action = input()
	if action == 'n':
		userRow = userRow - 1
	if action == 's':
		userRow = userRow + 1
	if action == 'e':
		userCol = userCol + 1
	if action == 'w':
		userCol = userCol - 1
	if userRow == -1:
		userRow = 4
	elif userRow == 5:
		userRow = 0
	if userCol == 5:
		userCol = 0
	elif userCol == -1:
		userCol = 4
	if world[userRow][userCol] == 'w':
		print('Chomp, chomp, chomp, you are dinner...')
		alive = 0
	if world[userRow][userCol] == 'p':
		print('"Aaaaaaaaaah," you scream as you fall to your death.')
		alive = 0
	if action == 'f':
		print('Which direction do you want to fire?')
		flight = input()
		arrows = arrows - 1
		print('You have ' + str(arrows) + ' arrows left.')
		if arrows == 0:
			alive = False
		if flight == 'n':
			arrowRow = userRow - 1
			arrowCol = userCol
		if flight == 'e':
			arrowRow = userRow
			arrowCol = userCol + 1
		if flight == 's':
			arrowRow = userRow + 1
			arrowCol = userCol
		if flight == 'w':
			arrowRow = userRow
			arrowCol = userCol - 1
		if arrowRow == -1:
			arrowRow = 4
		if arrowRow == 5:
			arrowRow = 0
		if arrowCol == -1:
			arrowCol = 4
		if arrowCol == 5:
			arrowCol = 0
		lookup = world[arrowRow][arrowCol]
		if lookup == 'w':
			print('You wumped the wumpus...')
			print('You win!!!!')
			alive = False
	lookup = world[userRow][userCol]
	if lookup == 'g':
		print('You found the gold...')
		print('You win!!!!')
		alive = False

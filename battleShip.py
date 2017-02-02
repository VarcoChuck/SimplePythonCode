import time
import os
import random

player = []
enemy = []
playerLive = 3
enemyLive = 3
board = 5
firstTime = True

def makeGame():
	global player
	global enemy
	for i in range(0, board):
		player.append(['0'] * board)
		enemy.append(['0'] * board)

def printPlayer():
	global player
	global enemy
	print('Battle Ship Prototype'.center(50,'*'))
	print("\n\nPLayer Live: {}\nEnemy Live: {}\n".format(playerLive, enemyLive))
	print '    1 2 3 4 5\n  -----------'
	print '1 | {} {} {} {} {}'.format(player[0][0],player[0][1],player[0][2],player[0][3],player[0][4])
	print '2 | {} {} {} {} {}'.format(player[1][0],player[1][1],player[1][2],player[1][3],player[1][4])
	print '3 | {} {} {} {} {}'.format(player[2][0],player[2][1],player[2][2],player[2][3],player[2][4])
	print '4 | {} {} {} {} {}'.format(player[3][0],player[3][1],player[3][2],player[3][3],player[3][4])
	print '5 | {} {} {} {} {}'.format(player[4][0],player[4][1],player[4][2],player[4][3],player[4][4])

def generateShip():
	global player
	global enemy
	for i in range(0,6):
		a = random.randint(0,4)
		b = random.randint(0,4)
		if i <= 2:
			player[a][b] = 'x'
		else:
			enemy[a][b] = 'x'

def WinOrLose():
	global enemyLive
	global playerLive
	if playerLive == 0:
		os.system('clear')
		print("Sorry sir you lose!")
		print("Maybe next time..")
		print("\n")
		raw_input("Press ENTER to exit")
		exit()
	elif enemyLive == 0:
		os.system('clear')
		print("Good Job sir")
		print("You won..")
		print("\n")
		raw_input("Press ENTER to exit")
		exit()

def main():
	printPlayer()
	WinOrLose()


while 1:
	os.system('clear')
	print("Hello sir")
	print("Do you want to play?")
	anwser = raw_input("Yes/No: ")
	anwser = anwser.lower()
	if anwser == 'yes':
		makeGame()
		generateShip()
		while 1:
			os.system('clear')
			main()
			print("\nPlayer turn.\n")
			row = int(raw_input('Row: '))
			col = int(raw_input('Col: '))
			if row > board or col > board:
				os.system('clear')
				print("This is not the ocean!")
				raw_input("Press ENTER to continue")
			elif enemy[row][col] == 'x':
				os.system('clear')
				print("You hit the enemy ship")
				enemyLive = enemyLive - 1
				time.sleep(2)
			else:
				os.system('clear')
				print("You mise!")
				time.sleep(1)
				print("Enemy turn!")
				a = random.randint(0, 4)
				b = random.randint(0, 4)
				if player[a][b] == 'x':
					os.system('clear')
					print("Enemy hit your ship")
					player[a][b] = 'x'
					playerLive = playerLive - 1
					time.sleep(2)
				else:
					os.system('clear')
					print('Enemy miss')
					time.sleep(2)
	elif anwser == 'no':
		os.system('clear')
		print("Ok sir, Good bye")
		raw_input("Press ENTER to exit!")
		exit()
	else:
		os.system('clear')
		print('Yes or No..')
		raw_input("Press ENTER to continue..!")
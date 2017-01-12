import time # importing time for sleep function!
import os # importing os for system function!
import random # importing random for randint function!


#variabile!
menu = True
odds = 3 # Player Live!
#Start Game!
os.system('cls')
print('Welcome to the Guest the number!')
print('The game is simple..you type a number!')
print('If the number is correct you on else..you lose!')
print("But you have only 3 odds, take care!")
print("Let's start!")
time.sleep(5) # time.sleep make user..to wait 5 second
os.system('cls')
print("Select the dificulty.")
print("1.)Easy\n2.)Medium\n3.)Hard")
anwser = raw_input("> ")
if anwser == '1':
	os.system('cls')
	print("You select the easy mode: ")
	print("You need to chose a number bettwen 0 to 10")
	numberMode = 10
	raw_input('Press ENTER to continue!')
elif anwser == '2':
	os.system('clear')
	print("You select the easy mode: ")
	print("You need to chose a number bettwen 0 to 25")
	raw_numberMode = 25
	input('Press ENTER to continue!')
elif anwser == '3':
	os.system('clear')
	print("You select the easy mode: ")
	print("You need to chose a number bettwen 0 to 50")
	raw_numberMode = 50
	input('Press ENTER to continue!')
else:
	os.system('cls')
	print("Invalid option")
	time.sleep(2)
while menu:
	os.system('cls') # Using system('cls') function to clear.. the console!
	print("Type a number bettwen 0 to {}".format(numberMode))
	player = int(raw_input('> '))
	randomNumber = random.randint(0, numberMode) # Get a random int value from 0 to numberMode!
	# Ask user..to type a number from 0 to numberMode
	if odds != 1:
		if player == randomNumber: #Verify if the player number..is correct!
			os.system('cls') #Clear console!
			print("Good job sir, you won!")
			time.sleep(2)
			print("Do you want to play again?")
			anwser = raw_input("(Y/N) > ")
			if anwser.lower() == 'y':
				odds = 3
				continue
			elif anwser.lower() == 'n':
				os.system('cls') #Clear console!
				print ("Take care! and thanks for playing!")
				print ("Good bye sir!")
				time.sleep(3) # time.sleep make user..to wait 3 second
				close() # Close the console!
			else:
				print('Y or N')
		else:
			os.system('cls') #Clear console!
			print("Sorry sir! you don't gues the number")
			print("The correct number is : {}".format(randomNumber))
			odds = odds - 1 # For evry wrong number , odds = -1
			print("You have only {} odds left!".format(odds))
			print("Take..care!")
			time.sleep(2) # time.sleep make user..to wait 2 second
	else:
		os.system('cls') #Clear console!
		print("Game Over")
		print("Maybe next time you have a better luck!")
		time.sleep(2)
		os.system('clear') #Clear console!
		print("Do you want to play again?")
		anwser = raw_input("(Y/N) > ")
		if anwser.lower() == 'y':
			odds = 3
			continue
		elif anwser.lower() == 'n':
			os.system('cls') #Clear console!
			print ("Take care! and thanks for playing!")
			print ("Good bye sir!")
			time.sleep(3) # time.sleep make user..to wait 3 second
			close() # Close the console!
		else:
			print('Y or N')


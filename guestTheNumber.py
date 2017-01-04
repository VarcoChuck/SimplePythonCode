import time # importing time for sleep function!
import os # importing os for system function!
import random # importing random for randint function!

#variabile!
menu = True
odds = 3 # Player Live!
#Start Game!
print('Welcome to the Guest the number!')
print('The game is simple..you type a number!')
print('If the number is correct you on else..you lose!')
print("But you have only 3 odds, take care!")
print("Let's start!")
time.sleep(5) # time.sleep make user..to wait 5 second
while menu:
	os.system('cls') # Using system('cls') function to clear.. the console!
	player = int(raw_input('Type a number from 0 to 10: '))
	randomNumber = random.randint(0, 10) # Get a random int value from 0 to 10!
	# Ask user..to type a number from 0 to 10
	if odds != 1:
		if player == randomNumber: #Verify if the player number..is correct!
			os.system('cls') #Clear console!
			print("Good job sir, you won!")
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
		print ("Sorry bro")
		print ("You don't have any odds left!")
		print ("Take care! and thanks for playing!")
		print ("Good bye sir!")
		time.sleep(5) # time.sleep make user..to wait 5 second
		close() # Close the console!


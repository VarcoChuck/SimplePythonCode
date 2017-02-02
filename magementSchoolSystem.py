import os
import time

class program:
	def __init__(self, FirstName,LastName,Age,Class,BirthDay,Location):
		self.FirstName = FirstName
		self.LastName = LastName
		self.Age = Age
		self.Class = Class
		self.BirthDay = BirthDay
		self.Location = Location
		
		os.system('clear')
		print("Name: {} {}".format(FirstName,LastName))
		print("Age: {}".format(Age))
		print("Class: {}".format(Class))
		print("Birthday: {}".format(BirthDay))
		print("Location: {}".format(Location))

	def putInTextFile(self):
		a = open('{}-{}.txt'.format(FirstName,LastName), 'w')
		a.write('First Name: {}\n'.format(FirstName))
		a.write('Last Name: {}\n'.format(LastName))
		a.write('Age: {}\n'.format(Age))
		a.write('Class: {}\n'.format(Class))
		a.write('Birthday: {}\n'.format(BirthDay))
		a.write('Location: {}'.format(Location))
		a.close()

while 2:
	os.system('clear')
	print("Hello Sir")
	print("1.Register student\n2.Exit")
	anwser = raw_input("> ")
	if anwser == '1':
		FirstName = raw_input("First Name: ")
		LastName = raw_input("Last name: ")
		Age = raw_input("Age: ")
		Class = raw_input("Class: ")
		BirthDay = raw_input("Birthday: ")
		Location = raw_input("Location: ")
		main = program(FirstName, LastName, Age, Class, BirthDay, Location)
		main.__init__(FirstName, LastName, Age, Class, BirthDay, Location)
		raw_input('Press ENTER to continue')
		os.system('clear')
		print("Export information to a text file?: ")
		anwser = raw_input("Yes/No: ")
		if anwser.lower() == 'yes':
			main.putInTextFile()
		elif anwser.lower() == 'no':
			os.system('clear')
			print("Good bye")
			time.sleep(2)
			exit()
		else:
			print("Yes or No")
	elif anwser == '2':
		exit()
	else:
		print ("Error")
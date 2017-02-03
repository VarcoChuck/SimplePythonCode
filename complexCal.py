from __future__ import division
from math import sqrt
from math import sin
from math import cos
import os

c = 0
def abc():
	anwser2 = raw_input("Type c to continue or q to quit: ")
	if anwser2 == 'c':
		continu()
	elif anwser2 == 'q':
		raw_input("Press ENTER to continue")
	else:
		print("c for continue or q for quit!")

def show():
	print("Hello sir!")
	print ("What do you want to do?")
	print ("1.Addition")
	print ("2.Decrease")
	print ("3.Division")
	print ("4.Multiplication")
	print ("5.Involution")
	print ("6.The remaining Divisions")
	print ("7.Exit")

def Addition(a,b):
	return a + b

def Decrease(a,b):
	return a - b

def Division(a,b):
	return a / b

def Multiplication(a,b):
	return a * b

def Involution(a,b):
	return a ** b

def TRD(a,b):
	return a % b

def choice():
	global a
	global b
	global c
	if anwser == 1:
		c = Addition(a,b);os.system('clear');print("{} + {} = {}".format(a,b,c));
	elif anwser == 2:
		c = Decrease(a,b);os.system('clear');print("{} - {} = {}".format(a,b,c));
	elif anwser == 3:
		c = Division(a,b);os.system('clear');print("{} / {} = {}".format(a,b,c));
	elif anwser == 4:
		c = Multiplication(a,b);os.system('clear');print("{} * {} = {}".format(a,b,c));
	elif anwser == 5:
		c = Involution(a,b);os.system('clear');print("{} ** {} = {}".format(a,b,c));
	elif anwser == 6:
		c = TRD(a,b);os.system('clear');print("{} % {} = {}".format(a,b,c));		os.system('clear');exit()

def continu():
	os.system('clear')
	global a
	global b
	global c
	print("{} si the curent valor of pre equation!\n\n".format(c))
	show()
	print("Select the next operation: ")
	anwser = int(raw_input('> '))
	os.system('clear')
	a = c
	print("First valor: %d" % a)
	b = int(raw_input("Second Valor: "))
	choice()
	raw_input("Press ENTER to continue!")


menu = True
while menu:
	os.system('clear')
	show()
	try:
		anwser = int(raw_input("> "))
		if anwser == 7:
			exit()
		a = int(raw_input("First number: "));b = int(raw_input("Second number: "))
		choice()
		abc()
	except ValueError:
		os.system('clear');print("Don't use letter, use only number");raw_input("Press ENTER to continue")
	except ZeroDivisionError:
		os.system('clear');print("Any number divised by 0 is 0..");raw_input("Press ENTER to continue")

		

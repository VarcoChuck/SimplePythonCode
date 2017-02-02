from __future__ import division
from math import sqrt
from math import sin
from math import cos
import os

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

def Cos(a):
	return sin(a)

def Sin(a):
	return cos(a)

def Sqrt(a):
	return sqrt(a)

menu = True
while menu:
	os.system('clear')
	print("Hello sir!")
	print("1.")
	print ("What do you want to do?")
	print ("1.Addition")
	print ("2.Decrease")
	print ("3.Division")
	print ("4.Multiplication")
	print ("5.Involution")
	print ("6.The remaining Divisions")
	print ("7.Cos")
	print ("8.Sin")
	print ("9.Square Root")
	print ("10.Exit")
	try:
		anwser = int(raw_input("> "))
		if anwser == 1:
				a = int(raw_input("First number: "));b = int(raw_input("Second number: "))
				c = Addition(a,b);os.system('clear');print("{} + {} = {}".format(a,b,c));raw_input("Press ENTER to continue")
		elif anwser == 2:
				a = int(raw_input("First number: "));b = int(raw_input("Second number: "))
				c = Decrease(a,b);os.system('clear');print("{} - {} = {}".format(a,b,c));raw_input("Press ENTER to continue")
		elif anwser == 3:
				a = int(raw_input("First number: "));b = int(raw_input("Second number: "))
				c = Division(a,b);os.system('clear');print("{} / {} = {}".format(a,b,c));raw_input("Press ENTER to continue")
		elif anwser == 4:
				a = int(raw_input("First number: "));b = int(raw_input("Second number: "))
				c = Multiplication(a,b);os.system('clear');print("{} * {} = {}".format(a,b,c));raw_input("Press ENTER to continue")
		elif anwser == 5:
				a = int(raw_input("First number: "));b = int(raw_input("Second number: "))
				c = Involution(a,b);os.system('clear');print("{} ** {} = {}".format(a,b,c));raw_input("Press ENTER to continue")
		elif anwser == 6:
				a = int(raw_input("First number: "));b = int(raw_input("Second number: "))
				c = TRD(a,b);os.system('clear');print("{} % {} = {}".format(a,b,c));raw_input("Press ENTER to continue")
		elif anwser == 7:
				a = int(raw_input("First number: "));c = Cos(a);os.system('clear');print("The cosinus of {} is {}".format(a,c));raw_input("Press ENTER to continue")
		elif anwser == 8:
				a = int(raw_input("First number: "));c = Sin(a);os.system('clear');print("The sinus of {} is {}".format(a,c));raw_input("Press ENTER to continue")
		elif anwser == 9:
				a = int(raw_input("First number: "));c = Sqrt(a);os.system('clear');print("The square root of {} is {}".format(a,c));raw_input("Press ENTER to continue")
		elif anwser == 10:
				os.system('clear');exit()
	except ValueError:
		os.system('clear');print("Don't use letter, use only number");raw_input("Press ENTER to continue")
	except ZeroDivisionError:
		os.system('clear');print("Any number divised by 0 is 0..");raw_input("Press ENTER to continue")

		

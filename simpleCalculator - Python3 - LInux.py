from os import system
from time import sleep
import math

menu = True

while menu:
	system('clear')
	print ("Hello sir!")
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
	anwser = input("> ")
	if anwser == '1':
		system('clear')
		sum01 = int(input("First valor: "))
		sum02 = int(input("Second valor: "))
		sum03 = sum01 + sum02
		system('clear')
		print ("{} + {} = {}".format(sum01,sum02,sum03))
		input("Press ENTER to exit!")
	elif anwser == '2':
		system('clear')
		sum01 = int(input("First valor: "))
		sum02 = int(input("Second valor: "))
		sum03 = sum01 - sum02
		system('clear')
		print ("{} - {} = {}".format(sum01,sum02,sum03))
		input("Press ENTER to exit!")
	elif anwser == '3':
		system('clear')
		sum01 = int(input("First valor: "))
		sum02 = int(input("Second valor: "))
		sum03 = sum01 / sum02
		system('clear')
		print ("{} / {} = {}".format(sum01,sum02,sum03))
		input("Press ENTER to exit!")
	elif anwser == '4':
		system('clear')
		sum01 = int(input("First valor: "))
		sum02 = int(input("Second valor: "))
		sum03 = sum01 * sum02
		system('clear')
		print ("{} * {} = {}".format(sum01,sum02,sum03))
		input("Press ENTER to exit!")
	elif anwser == '5':
		system('clear')
		sum01 = int(input("First valor: "))
		sum02 = int(input("Second valor: "))
		sum03 = sum01 ** sum02
		system('clear')
		print ("{} ** {} = {}".format(sum01,sum02,sum03))
		input("Press ENTER to exit!")
	elif anwser == '6':
		system('clear')
		sum01 = int(input("First valor: "))
		sum02 = int(input("Second valor: "))
		sum03 = sum01 % sum02
		system('clear')
		print ("{} % {} = Rest({})".format(sum01,sum02,sum03))
		input("Press ENTER to exit!")
	elif anwser == '7':
		system('clear')
		sin = int(input("Valor: "))
		sinValor = math.sin(sin)
		system('clear')
		print ("The sinus of valor {} is {}".format(sin,sinValor))
		input("Press ENTER to exit!")
	elif anwser == '8':
		system('clear')
		cos = int(input("Valor: "))
		cosValor = math.cos(cos)
		system('clear')
		print ("The cosine of valor {} is {}".format(cos,cosValor))
		input("Press ENTER to exit!")
	elif anwser == '9':
		system('clear')
		sqrt = int(input("Valor: "))
		sqrtValor = math.sqrt(sqrt)
		system('clear')
		print ("The squre root of valor {} is {}".format(sqrt,sqrtValor))
		input("Press ENTER to exit!")
	elif anwser == '10':
		system('clear')
		print("Good bye sir!")
		print("Have a nice day!")
		sleep(3)
		close()
	else:
		print("Invalid option")
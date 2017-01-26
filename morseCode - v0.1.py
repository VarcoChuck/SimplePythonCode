#Import..Module
import os
import time


#Clase
class Main:
	"""Main class."""
	morseList = {'A': '.-',     'B': '-...',   'C': '-.-.', 
				'D': '-..',    'E': '.',      'F': '..-.',
				'G': '--.',    'H': '....',   'I': '..',
				'J': '.---',   'K': '-.-',    'L': '.-..',
				'M': '--',     'N': '-.',     'O': '---',
				'P': '.--.',   'Q': '--.-',   'R': '.-.',
				'S': '...',    'T': '-',      'U': '..-',
				'V': '...-',   'W': '.--',    'X': '-..-',
				'Y': '-.--',   'Z': '--..',

				'0': '-----',  '1': '.----',  '2': '..---',
				'3': '...--',  '4': '....-',  '5': '.....',
				'6': '-....',  '7': '--...',  '8': '---..',
				'9': '----.',	' ' : "<-->"
     		   }

	morseListReverse = {'.-' : 'A',	'-...' : 'B',	'-.-.' : 'C',
                        '-..' : 'D',	'.' : 'E',	'..-.' : 'F',
			'--.' : 'G',	'....' : 'H',	'..' : 'I',
			'.---' : 'J',	'-.-' : 'K',	'.-..' : 'L',
			'--' : 'M',	'-.' : 'N',	'---' : 'O',
			'.--.' : 'P',	'--.-' : 'Q',	'.-.' : 'R',
			'...' : 'S',	'-' : 'T',	'..-' : 'U',
			'...-' : 'V',	'.--' : 'W',	'-..-' : 'X',
			'-.--' : 'Y',	'--..' : 'Z',

			'-----':	'0', 	'.----':	'1',	'..---':	'2',
			'...--':	'3',	'....-':	'4',	'.....':	'5',
			'-....':	'6',	'--...':	'7',	'---..':	'8',
			'----.':	'9',	 "<-->":	' '
			} 
						
	def __init__(self):
		pass
	
	def codeTranslator(self, inputText):
		"""This function traslate the input text in morse code.."""
		outputText = ''
		text = inputText.upper()
		textLong = len(text)
		for i in range(0, textLong):
			if text[i] in main.morseList:
				outputText += main.morseList[text[i]] + ' '
				continue

		os.system('cls')
		print ("Your text is: {}".format(text))
		print ("Your morse code is: {}".format(outputText))
		raw_input ("Press ENTER to continue!")

	def codeReverse(self, inputText):
		outputText = ''
		b = ''
		text = inputText.upper()
		textLong = len(text)
		for i in range(0, textLong):
			if text[i] == ' ':
				if b in main.morseListReverse:
					outputText += main.morseListReverse[b]
					b = ''
			else:
				b += text[i]
		textLong2 = len(text)
		for i in range(textLong2 - 3, textLong):
			if text[i] == ' ':
				if b in main.morseListReverse:
					outputText += main.morseListReverse[b]
					b = ''
			else:
				b += text[i]			
		os.system('cls')
		print ("Your morse code is: {}".format(text))
		print ("Your text is: {}".format(outputText.capitalize()))
		raw_input ("Press ENTER to continue!")
#Main
main = Main()
while 1:
	os.system('cls')
	print ("Welcome to Morse Code Traslator".center(50, '*'))
	print ("\n" * 2)
	print ("Welcome Sir")
	print ("1. Text -> Morse Code")
	print ("2. Morse Code -> Text")
	print ("3. Exit")
	anwser = raw_input("> ")
	if anwser == '1':
		os.system("cls")
		print ("Type what you want: \n")
		userText = raw_input("> ")
		main.codeTranslator(userText)
	elif anwser == '2':
		os.system("cls")
		print ("Pass the Morse Code: \n")
		userText = raw_input("> ")
		main.codeReverse(userText)		
	elif anwser == '3':
		close()
	else:
		os.system('cls')
		print ("Error, select a option form 1 to 3")
		time.sleep(2)

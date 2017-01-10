import os
import time

morseList = ['A', 'B', 'C', 'D',
				'E', 'F', 'G', 'H',
				'I', 'J', 'K', 'L',
				'M', 'N', 'O', 'P',
				'Q', 'R', 'S', 'T',
				'U', 'V', 'W', 'X',
				'Y', 'Z', '0', ]
morseListCode = ['.-',	'-...',	'-.-.',	'-..',
					'.',	'..-.',	'--.',	'....',
					'..',	'.---',	'-.-',	'.-..',
					'--',	'-.',	'---',	'.--.',
					'--.-', '.-.',	'...',	'-',
					'..-',	'...-',	'.--',	'-..-',
					'-.--', '--..', '-----']
morse = []

#Functi
def encode():
	global morseList
	global morseListCode
	global morse
	os.system('cls')
	print("Type your text.\n")
	text = raw_input("> ")
	a = len(text)
	for i in range(0, a):
		if text[i].upper() in morseList:
			c = morseList.index(text[i].upper())
			morse.append(morseListCode[c])
		elif text[i].isspace():
			c = '/'
			morse.append(c)
	print("".join(morse))
	raw_input('Press ENTER to continue!')
	os.system('cls')
	print("Do you want to export the text to file?")
	anwser = raw_input("(Y/N) : ")
	if anwser.lower() == 'y':
		textFile = open('codeMorseCrypr.txt', 'w')
		for i in morse:
			textFile.write(i)
		textFile.close()

while 4:
	os.system('cls')
	print("1. Encode			[Text -> Morse Code			]")
	print("2. Help				[View Morse Code Table			]")
	print("3. Exit				[Exit Program!				]")
	choice = raw_input("What you want to do: ")
	if choice == '1':
		encode()
	elif choice == '2':
		os.system('cls')
		print("01. 'A' = .-		02. 'B' = -...	03. 'C' = -.-.	04. 'D' = -..")
		print("05. 'E' = .		06. 'F' = ..-.	07. 'G' = --.	08. 'H' = ....")
		print("09. 'I' = ..		10. 'J' = .---	11. 'K' = -.-	12. 'L' = .-..")
		print("13. 'M' = --		14. 'N' = -.	15. 'O' = ---	16. 'P' = .--.")
		print("17. 'Q' = --.-	18. 'R' = .-.	19. 'S' = ...	20. 'T' = -")
		print("21. 'U' = ..-	22. 'V' = ...-	23. 'W' = .--	24. 'X' = -..-")
		print("25. 'Y' = -.--	26. 'Z' = --..	27. ' ' = /		28. '0' = -----")
		raw_input("Press ENTER To Exit!")
	elif choice == '3':
		os.system('cls')
		print("Wait 3 second for exit!")
		print("Have a nice day sir!")
		print("Good bye!")
		time.sleep(3)
		exit()
	else:
		os.system('cls')
		print("Invalid Option!")
		time.sleep(2)	
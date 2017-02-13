import os

absPart = False

while True:
	if os.path.isdir("WarningFreeVirus"):
		if os.path.isdir("WarningFreeVirus") and os.path.isfile("WarningFreeVirus/FreeVirus.txt"):
			pass
		elif os.path.isdir("WarningFreeVirus") == False:
			os.mkdir('WarningFreeVirus')
		else:
			a = open('WarningFreeVirus/FreeVirus.txt', 'w')
			a.write('Warning You have a free virus in pc :)\n')
			a.write('GoodBye Sir!')
			a.close()
	else:
		os.mkdir('WarningFreeVirus')

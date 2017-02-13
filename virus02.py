import os

while True:
	os.mkdir('WarningFreeVirus')
	os.chdir('WarningFreeVirus')
	if os.path.isfile('FreeVirus.txt'):
		pass
	else:
		a = open('FreeVirus.txt', 'w')
		a.write('Warning Free Virus!')
		a.close()
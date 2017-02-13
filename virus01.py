import os
a = 'Virus'
for i in xrange(25):
	if a == 'a':
		os.mkdir(a)
		os.chdir(a)
		a = a + '1'
	else:
		os.mkdir(a)
		os.chdir(a)
		a = a + '1'
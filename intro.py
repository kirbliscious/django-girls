catsrule = "Cats are kings of the universe"

def catattack(name):
	if name == 'Cheetoh':
		print('king kat!')
	elif name == 'Sage':
		print('eyelashes')
	elif name == 'Basil':
		print('hi ' + name)


catnames = ['Cheetoh','Sage','Basil','Oreo','Smudge','Zoey','Charlie','Benji']
for name in catnames:
	catattack(name)
	print('cat lover')
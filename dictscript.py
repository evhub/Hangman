dictionary = open('dictionary.txt').read().splitlines()
newdict = []
#print dictionary
for i in dictionary:
	print i
	if '-' not in i and "'" not in i:
		newdict.append(i)
print newdict
open('test.txt', 'wb').write("\n".join(newdict))
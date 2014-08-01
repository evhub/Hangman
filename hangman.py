import random
import string
import operator
from hangmanai import AI
dictionary = open('dictionary.txt').read().splitlines()
spaces=""
wrongletters = 0
HANGMANPICS = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def handle_guess(guess): 
	# -1 if not found
	# -2 if won
	# position if found
	global spaces
	global wrongletters
	print spaces
	rlist=[]
	print HANGMANPICS[wrongletters]
	nothing = raw_input("Press enter to guess")
	print "-----------------------------"
	pos = word.find(guess, 0)
	if pos == -1:
		wrongletters+=1
		return -1
	else:
		spaces = list(spaces)
		clist = []
		for i in range(0,len(spaces)):
			if i%2==0:
				clist.append(spaces[i])
		clist[pos] = guess
		rlist.append(pos)
		while(True):
			if word.find(guess,pos+1)== -1:
				break
			pos = word.find(guess,pos+1)
			rlist.append(pos)
			clist[pos]=guess
		won = "".join(clist)
		if won==word:
			print word
			print "You win"
			return -2
		spaces = " ".join(clist)
		if len(rlist)>1:
			return rlist
		else:
			return pos

while(True):
	spaces = ""
	wrongletters = 0
	answer = raw_input('Want me to enter a word?')
	if answer == 'n':
		word = raw_input('Enter Word: ')
	else:
		word = random.choice(dictionary)
	for i in range(0,len(word)):
		spaces += "_ "
	answer = raw_input("Do you want the computer to play?")
	if answer == 'y':
		ai = AI(word,dictionary)
		while(True):
			guess = ai.get_letter()
			greturn = handle_guess(guess)
			if type(greturn) is list:
				for greturn in greturn:
					status = ai.update(greturn,guess)
					if status == -1:
						print "I lose!"
						break
					elif status == 1:
						print "I win!"
						break
			else:
				status = ai.update(greturn,guess)
				if status == -1:
					print HANGMANPICS[wrongletters]
					print "I lose!"
					break
				elif status == 1:
					print "I win!"
					break

	else:
		while(True):
			guess = raw_input('Guess a letter: ')
			if guess(guess) == -2:
				break

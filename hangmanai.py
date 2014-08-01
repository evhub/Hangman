import string
import operator
class AI(object):
	def __init__(self,word,dictionary):
		self.usedletters = []
		self.wrongletters = []
		self.commonletters = ['n','o','s','t','r','a','e']
		self.freqs = {}
		self.possiblewords = []
		self.cletters = True
		self.word = word
		for x in string.letters[:26]:
			self.freqs[x]=0
		for i in dictionary:					
			if len(i) == len(word):
				self.possiblewords.append(i)
	def get_letter(self):						#Common Letters									#Finish Guessing
		highfreq = max(self.freqs.iteritems(), key=operator.itemgetter(1))[0]
		newlist=[]
		print "I'm going to guess "+highfreq
		self.usedletters.append(highfreq)
		return highfreq
		
	def update(self,greturn,guess):
		# -1 if lost
		# 0 otherwise
		# returns 1 if won
		newlist=[]
		for t in self.possiblewords:
 			for i in t:
 				if i not in self.usedletters:
 					self.freqs[i]+=1
 				break
		self.freqs = {}
		for x in string.letters[:26]:
			self.freqs[x]=0
		for t in self.possiblewords:
			for i in t:
				self.freqs[i]+=1
		for k,v in self.freqs.iteritems():
			if k in self.usedletters:
				self.freqs[k]=0
		if greturn == -2:
			return 1
		elif greturn >= 0:
			for i in self.possiblewords:
				if i[greturn] == guess:
					newlist.append(i)
			self.possiblewords = newlist
			return 0
		elif greturn == -1:
			for i in self.possiblewords:
				if guess not in i:
					newlist.append(i)
			self.possiblewords = newlist
			self.wrongletters.append(guess)
			if len(self.wrongletters)==6:
				return -1
			return 0
			

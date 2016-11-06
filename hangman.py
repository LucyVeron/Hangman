#!/usr/bin/python

import sys
import random

# Picks hangword from categories
animals = ['ewe','gnu','dodo']
flowers = ['poppy','lily','daisy']
fruits = ['banana','kiwi','lime']

print 'Please select a category: '
print '1) Animals'
print '2) Flowers'
print '3) Fruits'

select = input('Your choice: ')

randomIndex = random.randrange(0,3,1)

if select == 1:
	hangword = animals[randomIndex]
elif select == 2:
	hangword = flowers[randomIndex]
elif select == 3:
	hangword = fruits[randomIndex]


# Initial variables
wrongList = []
secretList = []
for i in range(0, len(hangword)):
	secretList.insert(i,' ')



# Prints hanged man.
def gallows(n):
	if n == 1:
		print '   ___'
		print '  |'
		print '  |'
		print ' _|_'

	elif n == 2:
		print '   ___'
		print '  |   0'
		print '  |'
		print ' _|_'

	elif n == 3:
		print '   ___'
		print '  |   0'
		print '  |   |'
		print ' _|_'

	elif n == 4:
		print '   ___'
		print '  |   0'
		print '  |  -|'
		print ' _|_'

	elif n == 5:
		print '   ___'
		print '  |   0'
		print '  |  -|-'
		print ' _|_'

	elif n == 6:
		print '   ___'
		print '  |   0'
		print '  |  -|-'
		print ' _|_  l'

	elif n == 7:
		print '  ____'
		print ' |    0'
		print ' |   -|-'
		print ' |    ll'
		print '_|_     '
		print '         '
		print 'Game over.'
	elif n == 8:
		print'                  oooooooooooo '
		print'                oo            oo '
		print'  ooooo        oo                oo '
		print'  o     o     oo      xx    xx     oo '
		print'   o     o    oo      xxx   xxx      oo '
		print'   o    o   oo       xx    xx         oo '
		print'    o   o   o                          oo '
		print'    oooooooooooo                         oo '
		print'   o            o    oo            oo    oo '
		print'  oo            o    oo            oo    oo '
		print' oo   ooooooooooo      oo        oo     oo '
		print' o               o       ooooooo       oo '
		print' oo              o                    oo '
		print'  o   ooooooooooo                   oo '
		print'  oo           o  oo                oo '
		print'   ooooooooooooo    oo            oo'
		print'                     oooooooooooo'

def wrong(letter):
	# No repeated wrong guesses
	if wrongList.count(letter) == 0:
		wrongList.append(letter)

	# Display wrong guesses
	print 'Wrong guesses:',
	for i in range(0, len(wrongList)):
		print  wrongList[i],
	print ' '

# Inserts correct guesses and displays them
def secret(letter):
	for i in range(0, len(hangword)):
		if letter == hangword[i]:
			secretList.pop(i)
			secretList.insert(i,hangword[i])
	for i in range(0, len(hangword)):
		print secretList[i],
	print ' '
	for i in range(0, len(hangword)):
		print '=',
	checkWin(secretList)


# If user guessed all the letters in the word, they win.
def checkWin(secretList):
	if secretList.count(' ') == 0:
		print ' '
		gallows(8)
		sys.exit()

def main():
	# User guesses letter
	n = 1
	while (n <= 6):
		print ' '
		letter = raw_input('Guess a letter: ')
		print ' '
		# Right guess
		if (hangword.count(letter) > 0):
			gallows(n)
			print ' '
			secret(letter)
			print ' '
			print 'Wrong guesses: ',
			for i in range(0, len(wrongList)):
				print wrongList[i],
			print ' '
		# Wrong guess
		else:
			n += 1
			gallows(n)
			print ' '
			secret(letter)
			print ' '
			wrong(letter)
			print ' '
main()

import random

tie=[11,22,33]
win=[13,21,32]
lose=[12,23,31]
options=['','Rock','Paper','Scissor']


def main():
	game = getGame()
	evalWin(game)

def printChoice(player,value):
	print(f"{player} chose {options[value]}")


def getGame():
	while True:
		try:
			user=int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors:"))
			if user >= 1 and user <= 3:
				break
			else:
				print("\tValue must be 1,2, or 3")
		except ValueError:
			print("\tValue must be 1,2, or 3")
	printChoice("User",user)	

	comp=random.randint(1,3)
	printChoice("The Computer",comp)	

	return ((user*10)+comp)

def evalWin(g):
	if g in tie:
		print("\nYou Tied. Try again!\n")
	elif g in win:
		print("\nCongrats, you won! Goodbye.\n")
	else:
		print("\nYou Lost. Try again!\n")

main()

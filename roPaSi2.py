import random

wlt=[[13,21,32],[12,23,31],[11,22,33]]
options=['','Rock','Paper','Scissor']
record=[0,0,0]

def main():
	while ((not record[0] == 5) and (not record[1] == 5)):
		game = getGame()
		result=evalWin(game)

		if result=="w":
			record[0]+=1
		elif result=="l":
			record[1]+=1
		else:
			record[2]+=1

	if record[0] == 5:
		print("\tUser wins!!!")
	else:
		print("\tComputer wins.")

	print(f"\tFinal Stats (w-L-T): {record[0]}-{record[1]}-{record[2]}\n\n")

def printChoice(u,c):
	print(f"\n\tUser: {options[u]} vs.\n\tComputer: {options[c]}")

def getGame():
	while True:
		try:
			user=int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors:"))
			if user >= 1 and user <= 3:
				comp=random.randint(1,3)
				printChoice(user,comp)	
				return ((user*10)+comp)
			else:
				print("\tValue must be 1,2, or 3")
		except ValueError:
			print("\tValue must be 1,2, or 3")

def evalWin(g):
	if g in wlt[2]:
		print("\tOutcome: Tie!\n")
		result="t"
	elif g in wlt[0]:
		print("\tOutcome: Win!\n")
		result="w"
	else:
		print("\tOutcome: Loss!\n")
		result="l"
	return result

main()

import random
wl=[0,0]

def main():
	loop=True
	grandTotal=[0,0]

	while loop:
		playRound()

		grandTotal[0]+=wl[0]
		grandTotal[1]+=wl[1]

		loop=playAgain()
		if loop == True:
			wl[0]=0
			wl[1]=0

	print (f"\n\tFinal outcome\n\tWin:{grandTotal[0]} Loss:{grandTotal[1]}\n")

def playRound():
	while wl[0] < 10 and wl[1] < 10:
		outcome=playGame()
		if outcome == True:
			wl[0]+=1
		else:
			wl[1]+=1

		print (f"\tWin:{wl[0]} Loss:{wl[1]}\n")

def playGame():

	game=[random.randint(1,100),random.randint(1,100)]
	while game[0] == game[1]:
		game[0] = random.randint(1,100)

	while True:
		choice=input(f"Your number is {game[0]}, is the computer number higher or lower?(h/l): ").lower()
		
		if choice in ('h','l'):
			if (choice == 'h' and game[0] < game[1]) or (choice == 'l' and game[0] > game[1]):
				print (f'\n\tWinner, computer value was {game[1]}')
				return True
			else: 
				print (f'\n\tLoser, computer value was {game[1]}')
				return False	
		else:
			print("\tPlease enter h or l...")

def playAgain():

        userInput = str(input('Do you want to play again? (y/n): ')).lower()
        try:
                if userInput == 'y':
                        return True
                elif userInput == 'n':
                        return False
                else:
                        print('\tInvalid Input')
                        return playAgain()
        except Exception as error:
                print('\tPlease enter a valid answer')
                return playAgain()

main()

import locale
locale.setlocale( locale.LC_ALL, '' )
dayOfWeek=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

def getBottles():
	
	totalBottles = 0
	counter = 0 

	while counter < 7:
		
		todayBottles = getBottlesToday(dayOfWeek[counter])
		totalBottles += todayBottles
		
		counter = counter + 1

	return totalBottles


def getBottlesToday(DOW):

	while True:
		try:
			user_input = int(input(f'Enter number of bottles for {DOW}: '))
			if user_input >= 0:
				return user_input
			else:
				print('\tBottles must be zero or greater.')
		except ValueError:
			print('\tBottles must be a whole number.')

def calcPayout(totalBottles):

	totalPayout = totalBottles * .10
	return totalPayout

def printInfo(totalPayout,totalBottles):

	print (f'\tTotal bottles collected: {totalBottles:,}\n\tTotal payout: {locale.currency(totalPayout,grouping=True)}\n')

def askAgain():

	userInput = str(input('Do you want to end the Program? (Y/N): ')).lower()
	try:
		if userInput == 'y':
			return True
		elif userInput == 'n':
			return False
		else:
			print('\tInvalid Input')
			return askAgain()
	except Exception as error:
		print('\tPlease enter a valid answer')
		return ask_user()

def main():

	stopRunning = False
	while stopRunning == False:
		totalBottles = getBottles()
		totalPayout = calcPayout(totalBottles)
		printInfo(totalPayout,totalBottles)	
		stopRunning = askAgain()

main()

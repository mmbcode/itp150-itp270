import locale
locale.setlocale( locale.LC_ALL, '' )

# Variables
global taxRate
taxRate=.06

# Functions

def main():
	print("Welcome to the total meal price calculator")
	meal = getMealP()
	tax = calcTax(meal)
	tip = calcTip(meal)
	printResults(meal,tax,tip)

def getMealP():
	while True:
		meal=input("Enter meal price: $")
		try:
			valid=float(meal)
			if valid >= 0:
				break
			else:
				print("\tThe amount can't be negative,try again")
		except ValueError:
			print("\tAmount must be a number, try again")
	return valid

def calcTax(meal):
	return round(float(meal*taxRate),2)

def calcTip(meal):
	if meal < 6:
		tip=round(meal*.1,2)
	elif meal < 12:
		tip=round(meal*.13,2)
	elif meal < 17:
		tip=round(meal*.16,2)
	elif meal < 25:
		tip=round(meal*.19,2)
	else:
		tip=round(meal*.22,2)
	return tip

def printResults(meal,tax,tip):
	print (f"\nMeal\t:{locale.currency(meal,grouping=True)}\nTax\t:{locale.currency(tax,grouping=True)}\nTip\t:{locale.currency(tip,grouping=True)}\nTotal\t:{locale.currency(tip+tax+meal,grouping=True)}")
	
main()

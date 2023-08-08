import locale

locale.setlocale( locale.LC_ALL, '' )

# Variables
global sTaxRate,cTaxRate
sTaxRate = .04
cTaxRate = .02

# Functions

def main():
	print("Welcome to the total tax calculator program")
	sales = inputData()
	cTax = calcCounty(sales)
	sTax = calcState(sales)
	tTax = calcTotal(cTax,sTax)
	printData(cTax,sTax,tTax)

def inputData():
	while True:
		try:
			return round(float(input ("Enter the total sales for the month: $")),2)
		except ValueError:
			print(f"\n\tInvalid value.\n\n")

def calcCounty(sales):
	return round(sales * cTaxRate,2)

def calcState(sales):
	return round(sales * sTaxRate,2)

def calcTotal(c,s):
	return round(c + s,2)
	
def printData(c,s,t):
	cFormated = locale.currency(c,grouping=True)
	sFormated = locale.currency(s,grouping=True)
	tFormated = locale.currency(t,grouping=True)
	print (f"The county tax is {cFormated}\nThe state tax is {sFormated}\nThe total tax is {tFormated}\n")
	
main()

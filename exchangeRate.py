# Get exchange rate data

import json
import requests

usdRates = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd.json').json()
muricaExchange = usdRates["usd"]

worldRates = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.min.json').json()

# Main function handles user interaction

def main():

    again = 'y'

    while again == 'y':
        while True:
            convertTo = input('\nPlease enter the ISO currency code of the currency you are converting to: ').lower()

            if convertTo in worldRates:
                break
            else:
                print(f'Invalid currency code: {convertTo}. Please try again.')

        while True:
            amountString = input('Enter USD amount you want to exchange: $')

            try:
                amount = float(amountString)
                break
            except ValueError:
                print('Invalid amount. Please enter a valid value.')

        getExchange(convertTo, amount)

        while True:
            again = input('\nWould you like to do another conversion (y/n)? ').lower()

            if again not in ('y', 'n'):
                print('Invalid input. Please enter y or n.')
            else:
                break

    print('\n\tThanks and goodbye!\n\n')

# Print out the currency exchange value

def getExchange(c, a):
    rate = muricaExchange[c]
    longName = worldRates[c]
    convertValue = '{:,.2f}'.format(rate * a)

    if convertValue == '1':
        longName = longName + 's'

    if longName == '':
        longName =c.upper()

    print(f'\n\t${a:.2f} USD converts to {rate * a:.5f} {longName}')

main()

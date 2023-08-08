def main ():

# Variables

    iFile = 'ho15.txt'

# Gather data from existing file

    original = openF(iFile,'r')
    inputs = original.readlines()
    original.close()

# print header, state sales reports then total. 

    printSales('header','','')
    cState=inputs[0].split()[1]
    total = 0.0

    for line in inputs:
        num, state, revenue = line.split()
        revenue = float(revenue)

        if state != cState:
            printSales(' total:', cState, total)
            cState = state
            total = revenue
        else:
            total += revenue

        printSales(num, state, revenue)

        if line == inputs[-1]:
            printSales(' total:', cState, total)

# funtion to open files from the operating system

def openF(f,m):

    try:
        a = open(f,m)
    except IOError:
        print ('Unable to open the file')
        exit
    return a

# print sales report based on data sent in.

def printSales(n,s,r):

    if n == 'header':
         print(f"{'Sales Report by State'.center(35)}\n")
         print(f"{'Store #'.ljust(10)} {'State'.center(7)} {'Sales'.rjust(15)}")
         print(f'{"="*35}')

    else:
        moneyFormat = '${:,.2f}'.format(r)

        if n != ' total:':    
            print(f'{n.ljust(10)} {s.center(7)} {moneyFormat.rjust(15)}')
        else:
            summation = s + n
            print(f'{"-"*35}')
            print(f'{summation.rjust(17)}  {moneyFormat.rjust(15)}')
            print(f'{"-"*35}')
    
main()

def checkGrade(lg):
    if lg.upper() in ('A', 'B', 'C'):
        return('Pass')
    else:
        return('Fail')

def main():

    letterGrade = 'L'
    
    while letterGrade.upper() not in ('A','B', 'C', 'D', 'F'):
        letterGrade = input('Enter a letter grade of A, B, C, D or F: ')
        if letterGrade.upper() not in ('A','B', 'C', 'D', 'F'):
            print('Not a valid grade letter, Try again please')

    result=checkGrade(letterGrade)

    if result == 'Pass':
        print("You Passed")
    else:
        print("Take the class again")

main()

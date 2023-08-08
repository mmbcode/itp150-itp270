empDict = {101:"McNally", 102:"Sama", 103:"Jones"}


def main():
   
    print('\nWelcome to the Employee Dictionary')
    menuO = '-1'
    
    while menuO != 0:
        
        userO = input('\n\tMenu:\n\t1. Add\n\t2. Remove\n\t3. Update\n\t4. View\n\n\t0. Exit\n\n\tSelection: ')

        try:
            menuO = int(userO)
        except Exception:
            print ('\n\tInvalid option please try again\n')
        if menuO == 1:
            aDir()
        elif menuO == 2:
            rDir()
        elif menuO == 3:
            uDir()
        elif menuO == 4:
            vDir('n')

    eDir()

def aDir():

    print ('\n\t\tDirectory Addition')
    newId = max(empDict.keys()) + 1
    newVal = input ('\n\t\tPlease new name: ')
    empDict[newId] = newVal.capitalize()
    
def rDir():

    print ('\n\t\tDirectory Entry Removal')
    menuR = '9'

    while menuR not in (1,2):

        menuR = input('\n\t\t1. By Name\n\t\t2. By ID\n\t\t3. Exit\n\n\t\tSelection: ')

        try:
            menuR = int(menuR)
        except Exception:
            print ('\t\tInvalid option please try again\n')

    if menuR == 1:
        vDir('n')
        rName = input('\t\tName to be removed: ')

        for key, value in empDict.items():
            if value == rName:
                delKey = key


        del empDict[delKey]
        

    elif menuR == 2:
        vDir('id')
        idRem = 'junk'
        while idRem == 'junk':
            idRem = (input('\n\t\tID to be removed: '))
            try:
                idRem = int(idRem)
            except Exception:
                print ('\n\t\tInvalid entry')
            
        empDict.pop(idRem,None)
        
    else:
        print ('')


def uDir():
    
    print ('\n\t\tDirectory Update:\n')
    updateR = '9'

    while updateR not in (1,2):
        updateR = input('\n\t\t1. By Name\n\t\t2. By ID\n\t\t3. Exit\n\n\t\tSelection: ')

        try:
            updateR = int(updateR)
        except Exception:
            print ('\t\tInvalid option please try again\n')

        if updateR == 1:
            vDir('n')
            uName = input('\t\tName to be updated: ')

            for key, value in empDict.items():
                if value == uName:
                    uKey = key
                    
        elif updateR == 2:
            vDir('id')
            uKey = 0

            while (uKey not in empDict):
                uKeyTemp=input('\n\t\tEnter a valid ID: ')
                
                try:
                    uKey = int(uKeyTemp)
                except Exception:
                    print ('\t\tInvalid entry, try again\n')
                
    if uKey in empDict:
        newN = input('\t\tEnter update: ').capitalize()
        empDict.update({uKey:newN})
    else:
        print('\n\t\tInvalid selection.')

    

def vDir(inputVal):
    
    print ('\n\t\tDirectory Listing:\n')
    resultList = sorted(list(empDict.values()))

    if inputVal == "n": 
        loop = len(resultList)

        for i in range(0,loop):
            print ( f'\t\t{resultList[i]}')

        print ('')
        
    else:
        for key, value in empDict.items():
            print (f'\t\t{key}: {value}')
        
def eDir():
    print ('\n\tThank you, have a nice day!\n\n\n')

main()

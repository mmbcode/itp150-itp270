def main ():

# Variables

    iFile = 'ho14data.txt'
    uFile = 'ho14data_mmb.txt'
    header = ['Firstname: ', 'Lastname: ', 'Phone: ', 'Salary: ']

# Gather data from existing file

    original = openF(iFile,'r')
    inputs = original.readlines()
    original.close()

# Update data

    for line in range(len(inputs)):
        sline = inputs[line].split(',')

        for n in range(len(sline)):
           sline[n] = header[n] + sline[n]

        inputs[line] = (sline)

# Write updates to the new file

    update = openF(uFile,'w')

    for line in inputs:
        update.write(' '.join(line))

    update.close()



def openF(f,m):

    try:
        a = open(f,m)
    except IOError:
        print ('Unable to open the file')
        exit
    return a

main()

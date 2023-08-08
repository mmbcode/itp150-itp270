elements = 10
values = []

for i in range(0, elements):
    while True:
        value = (input(f'Enter number {i+1}: '))
        try:
            values.append(int(value))
            break
        except Exception:
            print('\tPlease enter an actual integer: ')

highest = values[0]
lowest = values[1]

for i in range(1, elements):

    current = values[i]

    if highest > current:
        if lowest > current:
            lowest = current
    elif highest < lowest:
        lowest = highest
    else:
        highest = current

print(f'\n\t{values}\n\n\tHighest = {highest}\tLowest = {lowest}\n\n')

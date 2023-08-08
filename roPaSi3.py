import random

wlt=[[[13,21,32],[12,23,31],[11,22,33]],[0,0,0]]
options=['','Rock','Paper','Scissor']

def main():
    while wlt[1][0] < 2 and wlt[1][1] < 2:
        game = getInput()
        getOutcome(game)

    print ("Goodbye!")

def getInput():
    while True:
        try:
            u = int(input("\n Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
            if u >= 1 and u <= 3:
                c = random.randint(1,3)
                print(f"\n\tYou chose {options[u]}.\n\tThe Computer chose {options[c]}.")
                return ((u*10)+c)
            else:
                print("\tPlease only enter an integer.  Try again.")
        except ValueError:
            print("\tPlease only enter an integer.  Try again.")

def getOutcome(g):
    if g in wlt[0][2]:
        print("\tIt's a tie!\n")
        wlt[1][2]+=1
    elif g in wlt[0][0]:
        print("\tYou won!\n")
        wlt[1][0]+=1
    else:
        print("\tYou lost!\n")
        wlt[1][1]+=1
        
    print(f"\tHuman: {wlt[1][0]} Computer: {wlt[1][1]}")

main()

from random import randint

messages = ("Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful", \
             "As I see it, yes", "Most likely", "Outlook good", "Signs point to yes", "Yes", "It is certain", \
             "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "Reply hazy, try again", \
             "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again")

counts = [0] * 19

def main ():

    playAgain = 'Y'
  
    while playAgain != 'N':
        playEight()
    
        playAgain = input(f'\nEnter N to quit, or any other key to continue ').upper()
    
    closeOut()

def playEight ():
    input ("\nPress enter to ask the Magic 8 a question")
    choice = randint(0, 19)
    print (f"\n\t{messages[choice]}")
    counts[choice] += 1

def closeOut ():
    print ("\nThe following 8 ball options were never show:\n")
    for n in range(0,19):
        if counts[n] == 0:
            print (f"\t{messages[n]}")
   
main()

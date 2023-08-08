# Variables

words = ["a type of food","a name","a place","an amnimal (plural)","a profession (plural)","a verb","a thing (plural)","a clothing (plural)","a verb"]
userInputs = []

#Functions

def main():
	inputs=getInputs()
	paraOne(inputs[0],inputs[1],inputs[2])
	paraTwo(inputs[3],inputs[4])
	paraThree(inputs[5],inputs[6],inputs[7],inputs[8])

def getInputs():
	for word in words:
		userInputs.append(input("Enter {}: ".format(word)))
	return userInputs

def paraOne(one,two,three):
	print (f"\n\n\"Say {one.lower()}!\", the photographer said as the camera flashed! {two.title()} and I had gone to {three.capitalize()} to get our photos taken on my birthday.\n")

def paraTwo(four,five):
	print (f"The first photo we really wanted was a picture of us dressed as {four.upper()} pretending to be {five.upper()}.\n")

def paraThree(six,seven,eight,nine):
	print (f"When we were {six.lower()} the second photo, it was exactly what I wanted.  We both looked like {seven.lower()} wearing {eight.lower()} and {nine.swapcase()}!\n\n")

main()

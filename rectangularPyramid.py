def main():
    again = True
    print("Welcome to the rectangular pyramid volume calculator")

    while again:
        
        validInputs = False

        while not validInputs:
            try:
                l = float(input("\n\tEnter the length of the Pyramid base: "))
                w = float(input("\tEnter the width of the Pyramid base: "))
                h = float(input("\tEnter the height of the Pyramid: "))
                validInputs = True
            except ValueError:
                print("Please enter number values.")
        volume = rectPyr(l,w,h)

        print (f"\n\t\tThe volume of this Pyramid is {volume:,.2f}\n")

        if ( input(f"Press (q) to quit or any key to continue:").lower() == "q"):
            again = False

def rectPyr(l,w,h):
    return((l*w*h)/3)

main()

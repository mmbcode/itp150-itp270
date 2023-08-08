def main():
    for kind in ("str","int","float"):
        c = getInput(kind)
        print(f"\tThe {kind} value you entered, validated as: {type(c)}\n")

def getInput(kind):
    while True:
        var = input(f"Please enter a Python {kind} data type: ")
        try:
            converted = eval(f"{kind}('{var}')")
            return converted
        except:
            print (f"\tInvalid value\n")
main()

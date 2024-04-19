# valueError
def main():
    x = getNumber("What's x? ")
    print(f"x is {x}")

def getNumber(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            else:
                print("Number must be a positive integer>>>")
        except ValueError:
            print("Number must be an integer>>>")

main()
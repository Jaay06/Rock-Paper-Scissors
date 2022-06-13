from random import randint

# all possible choices
choice = ["R", "P", "S"]

#assigns a arandom choice to computer
computer = choice[randint(0, 2)]

human = False

while human == False:
    human = input("R, P, S")
    if human == computer:
        print("it is a tie")

    elif human == "R":
        if computer == "P":
            print("you lost!", computer, "covers", human)
        else:
            print("you won!", human, "smashes", computer)

    elif human == "P":
        if computer == "S":
            print("you lost!", computer, "cuts", human)
        else:
            print("you won!", human, "covers", computer)

    elif human == "S":
        if computer == "R":
            print("you lost!", computer, "smashes", human)
        else:
            print("you won!", human, "cuts", computer)

    else:
        print("that wasn't a valid input, try again")

    human = False
    computer = choice[randint(0, 2)]

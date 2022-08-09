import time


def print_pause(m):
    print(m)
    time.sleep(2)

iteams = []


def intro():
    print_pause("You find yourself standing in an open field, filled with"
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a pirate is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.")
    iteams.clear()
    whats_game()


def whats_game():
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choose()


def choose():
    x = input("(Please enter 1 or 2.)\n").lower()
    if x == "1":
        house()
    elif x == "2":
        cave()
    else:
        choose()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out"
                "steps a gorgon.")
    print_pause("Eep! This is the gorgon's house!")
    print_pause("The gorgon attacks you!")
    print_pause("You feel a bit under-prepared for this, what with only "
                "having a tiny dagger.")
    houseChoose()


def houseChoose():
    y = input("Would you like to (1) fight or (2) run away?").lower()
    if y == "1":
        fight()
    elif y == "2":
        print_pause("You run back into the field. Luckily, you don't "
                    "seem to have been followed.")
        whats_game()
    else:
        houseChoose()


def fight():
    if "magical Sword" in iteams:
        print_pause("As the wicked fairie moves to attack, you"
                    "unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the"
                    "attack.")
        print_pause("But the wicked fairie takes one look at "
                    "your shiny new toy and runs away!")
        print_pause("You have rid the town of the wicked fairie."
                    "You are victorious!")
        would()
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the dragon.")
        print_pause("You have been defeated!")
        would()


def would():
    s = input("Would you like to play again? (y/n)").lower()
    if s == "y":
        print_pause("Excellent! Restarting the game ...")
        intro()
    elif s == "n":
        print_pause("Thanks for playing! See you next time.")
        exit()
    else:
        would()


def cave():
    print_pause("You peer cautiously into the cave.")
    if "magical Sword" in iteams:
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        whats_game()
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        iteams.append("magical Sword")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        print_pause("You walk back out to the field.")
        whats_game()

intro()

import time
import random

# use boolean to determine if player been in cage
been_inside_cave = False


# print message with n seconds delay
def pause_print(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, choice_a, choice_b):
    while True:
        choice = input(prompt).lower()
        if choice_a in choice:
            break
        elif choice_b in choice:
            break
        else:
            pause_print("Sorry, I don't understand.")
    return choice


# function to print introductory message
def intro():
    global opponent
    opponent = random.choice (["Invincible Emogo", "Kakakolo, The Merciless,",
                              "Jumpie The Destroyer,"])
    pause_print("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    pause_print(f"Rumor has it that {opponent} is somewhere"
                f" around here, and has been terrifying the nearby village.")
    pause_print("In front of you is a house.")
    pause_print("To your right is a dark cave.")
    pause_print("In your hand you hold your trusty "
                "(but not very effective) dagger.")


# encounter at the house
def house():
    pause_print("You approach the door of the house.")
    pause_print(f"You are about to knock when the door "
                f"opens and out steps {opponent}.")
    pause_print(f"Eep! This is {opponent} house!")
    pause_print(f"{opponent} attacks you!")
    battle_or_retreat()


# message if player already been in cave
def cave_story1():
    pause_print("You peer cautiously into the cave.")
    pause_print("You've been here before, and gotten all the good stuff.")
    pause_print("It's just an empty cave now.")
    pause_print("You walk back out to the field.")
    starting_point()


# message if player never been inside the cave
def cave_story2():
    global been_inside_cave
    pause_print("You peer cautiously into the cave.")
    pause_print("It turns out to be only a very small cave.")
    pause_print("Your eye catches a glint of metal behind a rock.")
    pause_print("You have found the magical Sword of Ogoroth!")
    pause_print("You discard your silly old dagger "
                "and take the sword with you.")
    pause_print("You walk back out to the field.")
    been_inside_cave = True
    starting_point()


# player chooses to start at house or at cave
def starting_point():
    global been_inside_cave
    pause_print("Enter 1 to knock on the door of the house.")
    pause_print("Enter 2 to peer into the cave.")
    choice = valid_input("What would you like to do?\n(Please enter 1 or 2.)", "1", "2")
    if choice == "1":
        house()
    elif choice == "2":
        if been_inside_cave is True:
            cave_story1()
        else:
            cave_story2()
    # else:
    #     pause_print("Invalid Entry!")
     # starting_point()


# battle outcome
def fight():
    global been_inside_cave
    if been_inside_cave is True:
        pause_print(f"{opponent} moves to attack, "
                    f"you unsheath your new sword.")
        pause_print("The Sword of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the attack.")
        pause_print(f"But {opponent} takes one look "
                    "at your shiny new toy and runs away!")
        pause_print(f"You have rid the town of {opponent} . "
                    f"You are victorious!")
        restart()
    else:
        pause_print("You do your best...")
        pause_print(f"but your dagger is no match for {opponent}.")
        pause_print("You have been defeated!")
        restart()


# option to decline to fight
def run():
    pause_print("You run back into the field.Luckily, "
                "you don't seem to have been followed.")
    starting_point()


def battle_or_retreat():
    choice = valid_input("Do you want to fight (F) or run away (R)?", "f", "r")
    if choice == "f":
        fight()
    elif choice == "r":
        run()
    # else:
    #     pause_print("Invalid selection! Choose F to fight or R to run")
        # battle_or_retreat()


# prompt to reply or end play
def restart():
    choice = valid_input("Would you like to play again? (y/n)", "y", "n")
    if choice == "y":
        pause_print("Hold on..restarting game")
        intro()
        starting_point()
    elif choice == "n":
        pause_print("thank you, goodbye")
        quit()
    # else:
    #     pause_print("Invalid Selection..select Y or N")
        # restart()


# entry point
def play_game():
    intro()
    starting_point()
    battle_or_retreat()


play_game()

import time
import random

# use boolean to determine if player been in cage
been_inside_cave = False


# print message with n seconds delay
def pause_print(message):
    print(message)
    time.sleep(2)


# vairable to randomly select opponent
opponent = random.choice(["Invincible Emogo", "Kakakolo, The Merciless,",
                          "Jumpie The Destroyer,"])


# function to print introductory message
def intro():
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
    house_or_cave = input("What would you like to do?\n(Please enter 1 or 2.)")
    if house_or_cave == "1":
        house()
    elif house_or_cave == "2":
        if been_inside_cave is True:
            cave_story1()
        else:
            cave_story2()
    else:
        pause_print("Invalid Entry!")
        starting_point()


# battle outcome
def fight():
    global been_inside_cave
    if been_inside_cave is True:
        pause_print(f"{opponent} moves to attack, "
                    f"you unsheath your new sword.")
        pause_print("The Sword of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the attack.")
        pause_print("But the troll takes one look "
                    "at your shiny new toy and runs away!")
        pause_print(f"You have rid the town of {opponent} . "
                    f"You are victorious!")
        restart_inquiry()
    else:
        pause_print("You do your best...")
        pause_print(f"but your dagger is no match for {opponent}.")
        pause_print("You have been defeated!")
        restart_inquiry()


# option to decline to fight
def run():
    pause_print("You run back into the field.Luckily, "
                "you don't seem to have been followed.")
    starting_point()


def battle_or_retreat():
    fight_or_run = input("Do you want to fight (F) or run away (R)?").lower()
    if "f" in fight_or_run:
        fight()
    elif "r" in fight_or_run:
        run()
    else:
        pause_print("Invalid selection! Choose F to fight or R to run")
        battle_or_retreat()


# prompt to reply or end play
def restart_inquiry():
    new_game = input("Would you like to play again? (y/n)\n").lower()
    if "y" in new_game:
        pause_print("Hold on..restarting game")
        intro()
        starting_point()
    elif "n" in new_game:
        pause_print("thank you, goodbye")
        quit()
    else:
        pause_print("Invalid Selection..select Y or N")
        restart_inquiry()


# entry point
def play_game():
    intro()
    starting_point()
    battle_or_retreat()


play_game()

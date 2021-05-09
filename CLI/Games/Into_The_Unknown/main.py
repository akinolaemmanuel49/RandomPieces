from .character import Character
from .story import Quest


def createCharacter():
    name = str(input("Enter your name?"))
    confirm_name = str(input(f"Do you want {name} "\
                     "to be your character's name?\n"\
                     "Enter \"Y\" for YES and \"N\" for NO."))
    confirm_name = confirm_name.upper()
    while confirm_name != "Y":
        if confirm_name == "N":
            return createCharacter()
        elif (confirm_name != "Y") or (confirm_name != "N"):
            raise("Invalid input. Quitting program ...")
    
    classSelect = str(input("Choose a class?\n\
                  1. CLASS => ASSAULT: \n\
                  STATS: \n\
                  HITPOINTS: 10\n\
                  DEFENCE:   5\n\
                  ATTACK:    15\n\
                  AGILITY:   10\n\
                  \n\
                  2. CLASS => RECON: \n\
                  STATS: \n\
                  HITPOINTS: 10\n\
                  DEFENCE:   5\n\
                  ATTACK:    5\n\
                  AGILITY:   20\n\
                  \n\
                  3. CLASS => TANK: \n\
                  STATS: \n\
                  HITPOINTS: 15\n\
                  DEFENCE:   15\n\
                  ATTACK:    5\n\
                  AGILITY:   5\n"))
    if classSelect == "1":
        character = Character(name, 10, 5, 15, 10)
        print(character)
        return character
    elif classSelect == "2":
        character = Character(name, 10, 5, 5, 20)
        print(character)
        return character
    elif classSelect == "3":
        character = Character(name, 15, 15, 5, 5)
        print(character)
        return character
    else:
        raise("Invalid input! Quitting program ...")

player = createCharacter()
quest = Quest(player)
quest.story()

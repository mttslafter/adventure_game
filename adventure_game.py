import time
import random

items = [100, "rusty sword", "wooden shield"]


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, "{option}" is invalid. Please '
                    'try again!')


def Check_backpack():
    print(items)


def Not_a_choice():
    print_pause("The universe does not understand.")


def intro():
    print_pause("Hello adventurer! Welcome to Blergenspoop!")
    print_pause("You've been hired to find and defeat the "
                "creature that's been eating their livestock.\n")
    print_pause("You arrive with 100 gold in your pocket, "
                "a rusty sword, and a wooden shield.")
    print_pause("In Blergenspoop there is a tavern, a small market "
                ", and 2 paths leading out of the village.\n")


def dice_game():
    while True:
        gamble_choice = valid_input("Would you like to play?\n"
                                    "1. Yes\n"
                                    "2. No\n"
                                    "3. Check gold\n", ['1', '2', '3'])
        if gamble_choice == '1':
            if items[0] >= 25:
                dice_roll = random.randint(1, 20)
                print(dice_roll)
                if dice_roll >= 11:
                    items[0] = items[0] + 25
                    print_pause("You win!")
                else:
                    items[0] = items[0] - 25
                    print_pause("Oh no! You lose.")
            else:
                print_pause("Unfortunately, you do not have enough to play.\n")
                break
        if gamble_choice == '2':
            print_pause("Maybe some other time then.\n")
            break
        else:
            print_pause(items[0])


def Tavern_options():
    while True:
        tavern_choice = valid_input("What would you like to do?\n"
                                    "1. Speak to the lady\n"
                                    "2. Speak to the old man\n"
                                    "3. Leave\n", ['1', '2', '3'])
        if tavern_choice == '1':
            print_pause("You speak to the lady behind the bar.")
            print_pause("She tells you that people in town say the creature\n"
                        "has been coming from the left path leading "
                        "out of the village")
            print_pause("She also says the right path leads to a small group\n"
                        "of bandits who are very fond of gold and \n"
                        "harrass anyone who comes near them. So be careful.\n")
        elif tavern_choice == '2':
            print_pause("You approach the old man.")
            print_pause("He tells you he knows nothing of the "
                        "creature and doesn't really care.\n")
            print_pause("But if you would like to play a game "
                        "and wager some coin\n"
                        "he would be more than happy to oblige.\n")
            print_pause("The old man puts a single 20 sided dice on the table")
            print_pause("He explains if he rolls a 1-10, you lose 25 gold.")
            print_pause("If he rolls an 11-20, you win 25 gold.\n")
            dice_game()
        else:
            print_pause("You leave the tavern.")
            break


def Market_options():
    while True:
        market_choice = valid_input("What would you like to do?\n"
                                    "1. Buy the sword.\n"
                                    "2. Buy the shield.\n"
                                    "3. Check items.\n"
                                    "4. Leave.\n", ['1', '2', '3', '4'])
        if market_choice == '1':
            if "steel sword" in items:
                print_pause("You already have a steel sword.\n")
            elif items[0] >= 50:
                items[0] = items[0] - 50
                items.append("steel sword")
                print_pause("You have obtained a steel sword!\n"
                            "This will add +5 to your monster fight!\n")
            else:
                print_pause("You do not have enough gold\n")
        elif market_choice == '2':
            if "steel shield" in items:
                print_pause("You already have a steel shield.\n")
            elif items[0] >= 100:
                items[0] = items[0] - 100
                items.append("steel shield")
                print_pause("You have obtained a steel shield!\n"
                            "This will add +5 to your monster fight!\n")
            else:
                print_pause("You do not have enough gold\n")
        elif market_choice == '3':
            print(items)
        else:
            print_pause("You leave the market square.\n")
            break


def Bandit_options():
    while True:
        bandit_response = valid_input("What do you do?\n"
                                      "1. Ask him to help rid the village "
                                      "of the monster.\n"
                                      "2. Tell him he stinks and needs a "
                                      "bath.\n"
                                      "3. Apologize and say you have the "
                                      "wrong house.\n", ['1', '2', '3'])
        if bandit_response == '1':
            print_pause("The man responds saying they do not "
                        "work for free. If\n"
                        "you have 100 gold they'd be more "
                        "than happy to help.\n")
            pay_bandit = valid_input("Do you accept?\n"
                                     "1. Yes\n"
                                     "2. No\n", ['1', '2'])
            if pay_bandit == '1':
                if items[0] >= 100:
                    items[0] = items[0] - 100
                    print_pause("The large man happily accepts and "
                                "hands you a glowing \n"
                                "orb. He explains that if you throw "
                                "it on the ground \n"
                                "they will be summoned and help you fight.\n")
                    print_pause("You have obtained the bandit orb!\n"
                                "This will add +5 to your monster fight!\n")
                    items.append("bandit orb")
                    break
                elif items[0] < 100:
                    print_pause("You do not have enough gold.\n")
            else:
                print_pause("The large man spits on the ground "
                            "and tells you to \n"
                            "take off.\n")
                break
        elif bandit_response == '2':
            print_pause("The large mans tattoos begin to glow and "
                        "he pushes you onto the ground\n"
                        "without even touching you.\n")
            print_pause("He says a lot of rude things and then "
                        "slams the door shut.\n")
            items.append("bandits curse")
            break
        else:
            print_pause("He grunts and then closes the door.\n")
            break


def Right_path_options():
    while True:
        bandit_choice = valid_input("What would you like to do?\n"
                                    "1. Knock on the front door.\n"
                                    "2. Leave\n", ['1', '2'])
        if bandit_choice == '1':
            if 'bandits curse' in items:
                print_pause("A strange force is keeping you from "
                            "approaching the house.\n")
                Right_path_options()
                break
            if 'bandit orb' in items:
                print_pause("The large man opens the door and is "
                            "confused as to why you're still there.")
                Right_path_options()
                break
            else:
                print_pause("You knock on the front door.\n")
                print_pause("After a few moments a large hairy man "
                            "with strange tattoos\n"
                            "opens the front door.\n")
                print_pause("He very rudely asks why you're on their "
                            "property.\n")
                Bandit_options()
        else:
            print_pause("You leave the property.")
            break


def Hydra_Fight():
    while True:
        fight_hydra = valid_input("What do you do??\n"
                                  "1. FIGHT! (you must roll a 15 or "
                                  "higher on a 20 sided dice)\n"
                                  "2. RUN AWAY!!\n", ['1', '2'])
        if fight_hydra == '1':
            dice_roll = random.randint(1, 20)
            if "steel sword" in items:
                dice_roll = dice_roll + 5
                print_pause("Your new sword shines brightly "
                            "in the dark cave!")
            if "steel shield" in items:
                dice_roll = dice_roll + 5
                print_pause("The steel shield holds strong "
                            "against the enemy!")
            if "bandit orb" in items:
                dice_roll = dice_roll + 5
                print_pause("You throw the bandit orb to the ground "
                            "and summon your new allies!")
            print(dice_roll)
            if dice_roll >= 15:
                print_pause("As the ferocious monster attacks and "
                            "snaps, you manage to\n"
                            "dodge and get close enough to stab "
                            "the beast in the heart!\n")
                print_pause("It falls to the ground and exhales its "
                            "last breath.")
                print_pause("You are victorious!")
                Play_again()
            else:
                print_pause("As valiant as you are, one of the "
                            "beasts heads grabs you from\n"
                            "behind and throws you into the air "
                            "before swallowing you whole!")
                print_pause("You have lost.")
                Play_again()
        else:
            print_pause("You run for your life!")
            break


def Cave_options():
    while True:
        cave_choice = valid_input("What do you do?\n"
                                  "1. Go inside\n"
                                  "2. Leave\n", ['1', '2'])
        if cave_choice == '1':
            print_pause("You enter the cave.\n")
            print_pause("As you walk inside you notice horrible odors "
                        "and bits of raw, uneaten food.\n")
            print_pause("Before too long a giant Hydra rises "
                        "from the back of the cave!!\n")
            Hydra_Fight()
        else:
            print_pause("You decide to leave for now and come "
                        "back another time.\n")
            break


def Tavern():
    print_pause("You arrive in the tavern. It's pretty dull.")
    print_pause("There's a lady working behind the bar.\n"
                "Also there's an old man rolling some dice "
                "at a table by himself.\n")
    Tavern_options()


def Market():
    print_pause("You arrive in the market square of the town.\n")
    print_pause("There are various vendors selling food items and\n"
                "necessities for the village.\n")
    print_pause("A man with a large cart waves you down.")
    print_pause("He notices that your sword is rusty and "
                "your shield\n"
                "is made of wood.\n")
    print_pause("He pulls a shiny steel sword and shield from his cart.\n")
    print_pause("He offers them to you. 50 gold for the sword "
                "and 100 gold for the shield.\n")
    Market_options()


def Right_path():
    print_pause("You take the path leading to the right "
                "out of the village.\n")
    print_pause("Eventually you stumble across a small "
                "cabin with bits\n"
                "of trash and empty bottles scattered "
                "around the front.\n")
    Right_path_options()


def Left_path():
    print_pause("You take the path leading to the left "
                "out of the village.\n"
                "You notice large, strange footprints "
                "along your way.\n")
    print_pause("Eventually you find a cave with strange "
                "odors coming from it.")
    Cave_options()


def Play_game():
    while True:
        choice = valid_input("Where would you like to go?\n"
                             "1. Tavern\n"
                             "2. Market\n"
                             "3. Right path\n"
                             "4. Left path\n"
                             "5. Check backpack\n", ['1', '2', '3', '4', '5'])
        if choice == '1':
            Tavern()
        if choice == '2':
            Market()
        if choice == '3':
            Right_path()
        if choice == '4':
            Left_path()
        else:
            Check_backpack()


def Play_again():
    while True:
        play_again = valid_input("Would you like to play again?\n"
                                 "1. Yes \n"
                                 "2. No\n", ['1', '2'])
        if play_again == '1':
            print_pause("Adventuring awaits!\n")
            Play_game()
        else:
            print_pause("Thanks for playing!")
            exit(0)


def game():
    intro()
    while True:
        Play_game()


if __name__ == '__main__':
    game()

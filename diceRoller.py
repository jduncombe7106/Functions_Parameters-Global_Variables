import random
import time

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def roll():
    print("rolling.....")
    roll = random.randint(0,5)
    return(roll)


def show_dice(roll):
    if roll == 0:
        print(s1)
    elif roll == 1:
        print(s2)
    elif roll == 2:
        print(s3)
    elif roll == 3:
        print(s4)
    elif roll == 4:
        print(s5)
    elif roll == 5:
        print(s6)


roll = roll()
time.sleep(1)

userinput = raw_input("to roll a dice type a 'Y'")

if userinput == "Y":
    show_dice(roll)

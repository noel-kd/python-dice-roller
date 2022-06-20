#A simple looping dice roller
#Created by Kyle Noel, 20Jun2022

import random as rand

#Header
print("------------- Virtual Dice Roller -------------")
print("\nEnter 'R' to roll the die...")

#Roll check
roll = input(">> ")
roll = roll.upper()

#Err handling
while roll != 'R':
    print("\nInvalid entry. Enter 'R' to roll the die...")
    roll = input(">> ")
    roll = roll.upper()

#Display fist rollCount
rollCount = 1
print("------------------- Roll  {} -------------------".format(rollCount))

#Randomize and print each roll
#Loop until user declares otherwise
loop = True
while loop is True:
    result = rand.randint(1, 6)
    if result == 1:
            print(""" 
             _____________
            |             |
            |             |
            |      O      |
            |             |
            |_____________|

            You rolled a one!               
                        """)
    elif result == 2:
            print(""" 
             _____________
            |             |
            |   O         |
            |             |
            |         O   |
            |_____________|

            You rolled a two!
                        """)

    elif result == 3:
            print(""" 
             _____________
            |             |
            |   O         |
            |      O      |
            |         O   |
            |_____________|

            You rolled a three!
                        """)

    elif result == 4:
            print(""" 
             _____________
            |             |
            |   O     O   |
            |             |
            |   O     O   |
            |_____________|

            You rolled a four!
                        """)

    elif result == 5:
            print(""" 
             _____________
            |             |
            |   O     O   |
            |      O      |
            |   O     O   |
            |_____________|

            You rolled a five!
                        """)

    elif result == 6:
            print(""" 
             _____________
            |             |
            |   O     O   |
            |   O     O   |
            |   O     O   |
            |_____________|

            You rolled a six!
                        """)

    rollCount += 1

    #Reroll check
    print("Roll again? Y/N")
    rerun = input(">> ")
    rerun = rerun.upper()
    if rerun == 'Y':
        loop = True
        print("------------------- Roll  {} -------------------".format(rollCount))
    #Terminate program if input not Y
    else:
        loop = False
        print("------------- Program  Terminated -------------")

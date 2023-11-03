print(
    '''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    '''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You are at the crossroad. Where do you want to go? Type: left or right\n").lower()

if choice1 != "left":
    print("Fall into a hole. Game over")
else:
    choice2 = input("You found yourself on a pier. You can see an island in the middle of a lake."
                    "Do you swim or wait for a boat? Type: swim or wait\n").lower()
    if choice2 != "wait":
        print("You are attacked by a monstrous fish and drown by a result. Game Over.")
    else:
        choice3 = input("On a island there is a castle with 3 entrances. Which door do you choose?"
                        "Type: red, yellow or blue.\n").lower()
        if choice3 == "red":
            print("You get drenched in oil and set on fire. Game Over")
        elif choice3 == "blue":
            print("You get eaten by wolves. Game Over")
        elif choice3 == "yellow":
            print("You found a treasure chest. You WIN!")
        else:
            print("Game Over.")

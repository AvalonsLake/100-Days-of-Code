from pkg_resources import working_set

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("You're at a cross road. Where do you go? \n Type 'left' or 'right' \n ").lower()
if left_or_right == "left":
    wait_or_swim = input("You've come to a lake. You can see an island in the middle of it. "
                         "\n Type 'wait' to wait for a boat or type 'swim' to swim across.\n ").lower()
    if wait_or_swim == "wait":
        print("After a while, a boat arrives and takes you across the lake.\n"
              " You now stand on the islands beach unharmed, and Before you is a house with three doors. \n"
              "One with an X, one with a C, and one with an R. A small sign next to the house reads \n"
              "'The treasure lay behind a Pirates favorite letter'\n"
              "Hint: a Pirates true love")
        which_door = input("Which door do you choose? Type 'x', 'c', or 'r' \n").lower()
        if which_door == "x":
            print("'X marks the spot, and all pirates love treasure' you say as you open the door. \n"
                  "as you walk inside the door slams shut behind you and the floor opens to reveal a spike pit\n"
                  "as you fall, you realize your mistake. A pirates true love is the-\n"
                  "You Lose" )
        elif which_door == "c":
            print("'A pirates true love will always be the C!' you chuckle to yourself as you open the door\n"
                  "You walk inside a small hallway as you walk to the end and turn the corner,\n"
                  "you find the treasure room, wall to wall in gems, art, coins, and a large open chest in the center of the room. \n"
                  "Looking at it all you realize, this might take a few trips...\n"
                  "You Win!")
        elif which_door == "r":
            print("'Arrrr me hearties, this be the door!' you chuckle to yourself as you open the door. \n"
                  "as you walk inside the door slams shut behind you and the floor opens to reveal a spike pit\n"
                  "as you fall, you realize your mistake. A pirates true love is the-\n"
                  "You Lose")
    elif wait_or_swim == "swim":
        print("You start to swim across the lake and make good time. About half-way across your legs start to cramp \n"
              "you cry for help as you start to tread water but no one comes. \n"
              "after what feels like hours your muscles give way and you start to sink \n"
              "you lose")
elif left_or_right == "right":
    print("You've come to a forest. It is shrouded in mist")
    enter_or_leave = input("Do you enter the forest? or turn around? type 'enter' or 'turn around' \n").lower()
    if enter_or_leave == "enter":
        print("you enter the forest and quickly become lost. You'll never make it out much less find the treasure.\n"
              "You lose")
    elif enter_or_leave == "turn around":
        print("you turn around and start to walk back. While walking you hear a loud hissing noise \n"
              "you look down to see a viper coiled at you feet as it bites you. \n"
              "you collapse as the venom quickly takes effect and the world turns to black \n"
              "you lose")
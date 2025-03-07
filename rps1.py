import sys
import random

playagain = True

while playagain :
    gopika = input('Enter \n1 for Rock\n2 for Paper\n3 for Scissors : \n')

    player = int(gopika)

    if player < 1 or player > 3 :
        sys.exit('You must enter 1,2,3. ')

    computer_choice = random.choice("123")

    computer = int(computer_choice)

    print()
    print("Gopika chose : " + str(player))
    print("Python chose : " + str(computer))
    print()

    if player == 1 and computer == 3 :
        print("🎉 Gopika Win")
    elif player == 2 and computer == 1 :
        print("🎉 Gopika Win")
    elif player == 3 and computer == 2 :
        print("🎉 Gopika Win")
    elif player == computer :
        print("😒 Tie Game")
    else:
        print("🐍 Python Win")

    playagain = input("\nPlayagin ?\nY for Yes \nQ for Quit\n")

    if playagain.lower() == 'y':
        continue
    else :
        print("Thank you for Playing")
        playagain = False

sys.exit("Bye 😴")
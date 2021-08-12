import random
def swggame():
    play=input("Welcome to the Snake,Water and Gun game Press s for Snake,w for Water and g for Gun \n Rules:\n * SNAKE will drink WATER \n * GUN shoots the SNAKE \n * GUN will have no effect on WATER \n To play press ENTER and to quit press q: ")
    while play!='q':
        player1=input("Choose your gesture: ")
        player2=random.randint(1,3)
        if player2==1:
            player2='s'
        elif player2==2:
            player2='w'
        else:
            player2='g'
        if player1=='s' or player1=='w' or player1=='g' and player2=='s' or player2=='w' or player2=='g':
            print(f"Computer chosed {player2}")
            if player1.lower()=='s' and player2.lower()=='w':
                print("You won! \n")
                return swggame()
            elif player1.lower()=='w' and player2.lower()=='g':
                print("You won! \n")
                return swggame()
            elif player1.lower()=='g' and player2.lower()=='s':
                print("You won! \n")
                return swggame()
            elif player2.lower()=='s' and player1.lower()=='w':
                print("Computer wins! \n")
                return swggame()
            elif player2.lower()=='w' and player1.lower()=='g':
                print("Computer wins! \n")
                return swggame()
            elif player2.lower()=='g' and player1.lower()=='s':
                print("Computer wins! \n")
                return swggame()
            else:
                print("Draw! \n")
                return swggame()
        else:
            print("Invalid input!!!")
            break

swggame()

    
    
    
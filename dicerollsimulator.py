import random

def main():
    player1=0
    player2=0
    rounds=1
    player1wins=0
    player2wins=0
    roll_again=0
    start=input("Welcome to the dice game to play press ENTER to exit press q: ")
    if start.lower()!="q":
        print("Lets Go")
        name1=input("Enter player1 name: ")
        name2=input("Enter player2 name: ")
    else:
        print("Thanks for playing")
        return start
    while rounds!=4:
        roll_again=input("To roll the dice press ENTER to quit press q :")
        if roll_again.lower()!="q":
            print("Rounds: " +str(rounds))
            player1=dice_roll()
            print(str(name1) +" has scored: " + str(player1))
            player2=dice_roll()
            print(str(name2)+ " has scored: " +str(player2))
            rounds=rounds+1
        else:
            print("Thanks for playing")
            rounds=rounds+1
            break
        if player1 > player2:
            print(str(name1) + " wins! ")
            player1wins=player1wins+1
        elif player1 < player2:
            print(str(name2)+ " wins! ")
            player2wins=player2wins+1
        else:
            print("Draw! ")
    if player1wins>player2wins:
        print(str(name1) + " has won rounds: "+str(player1wins))
    elif player1wins<player2wins:
        print(str(name2) + " has won rounds: " +str(player2wins))
    else:
        print("There is a draw")
        

def dice_roll():
    num_rolled=random.randint(1,6)
    return num_rolled;

main()

        




    


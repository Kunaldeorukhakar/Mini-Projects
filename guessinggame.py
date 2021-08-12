import random
def guessnum():
    randnum=random.randint(1,10)
    return randnum

def main():
    num=0
    playernum=0
    chances=1
    num=guessnum()
    print("Welcome to the guessing game")
    while chances!=4:
        playernum=int(input("Enter the number: "))
        if playernum<num:
            print("Your number is lower than the number your chances remaining: " +str(3-chances))
            chances=chances+1
        elif playernum>num:
            print("Your number is higher than the number your chances remaining: " +str(3-chances))
            chances=chances+1
        else:
            print("Well done! you have guessed the right number in chance: "+str(chances))
            break
    print("The correct number was: "+str(num))
    
         
main()

        
    
    
    
    
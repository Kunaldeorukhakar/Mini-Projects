rounds=1
ans=0
points=0
while rounds!=11:
    print("1.What is the capital of India?")
    print("A.Maharashtra \t\tB.Uttar pradesh \nC.Delhi \t\tD.Madhya pradesh")
    ans=input("Ans: ")
    if ans.upper()=="C":
        print("\nCorrect Answer\n")
        points=points+5
        rounds=rounds+1
    else:
        print("Incorrect Answer")
        break
    print("2.Who is the national animal of India?")
    print("A.Tiger \t\tB.Lion \nC.Elephant \t\tD.Kangaroo")
    ans=input("Ans: ")
    if ans.upper()=="A":
        print("\nCorrect Answer\n")
        points=points+5
        rounds=rounds+1
    else:
        print("Incorrect Answer")
        break
    print("3.Who is the national Bird of India?")
    print("A.Penguin \t\tB.Peacock \nC.Parrot \t\tD.Pigeon")
    ans=input("Ans: ")
    if ans.upper()=="B":
        print("\nCorrect Answer\n")
        points=points+5
        rounds=rounds+1
    else:
        print("Incorrect Answer")
        break
    print("4.What is the currency of India?")
    print("A.Dollar \t\tB.Ruppee \nC.Euro \t\tD.Yen")
    ans=input("Ans: ")
    if ans.upper()=="B":
        print("\nCorrect Answer\n")
        points=points+5
        rounds=rounds+1
    else:
        print("Incorrect Answer")
        break
    print("5.Which is the country with the most people?")
    print("A.India \t\tB.England \nC.China \t\tD.Japan")
    ans=input("Ans: ")
    if ans.upper()=="C":
        print("\nCorrect Answer\n")
        points=points+5
        rounds=rounds+1
    else:
        print("Incorrect Answer")
        break
    print("6.Which insect has colourful wings?")
    print("A.HoneyBee \t\tB.Housefly \nC.Mosquito \t\tD.Butterfly")
    ans=input("Ans: ")
    if ans.upper()=="D":
        print("\nCorrect Answer\n")
        points=points+5
        rounds=rounds+1
    else:
        print("Incorrect Answer")
        break
    print("7.Fastest animal on earth is?")
    print("A.Cheetah \t\tB.Tiger \nC.Dear \t\tD.Lion")
    ans=input("Ans: ")
    if ans.upper()=="A":
        print("\nCorrect Answer\n")
        points=points+5
        rounds=rounds+1
    else:
        print("Incorrect Answer")
        break
    print("8.Which bird cannot fly?")
    print("A.Owl \t\tB.Peacock \nC.Parrot \t\tD.Ostrich")
    ans=input("Ans: ")
    if ans.upper()=="D":
        print("\nCorrect Answer\n")
        points=points+5
        rounds=rounds+1
    else:
        print("Incorrect Answer")
        break
    print("9.We get solar energy from ?")
    print("A.Sun \t\tB.Tree \nC.Fire \t\tD.Moon")
    ans=input("Ans: ")
    if ans.upper()=="A":
        print("\nCorrect Answer\n")
        points=points+5
        rounds=rounds+1
    else:
        print("Incorrect Answer")
        break
    print("10.Capital of Maharashtra is?")
    print("A.Pune \t\tB.Nagpur \nC.Mumbai \t\tD.Ratnagiri")
    ans=input("Ans: ")
    if ans.upper()=="C":
        print("\nCorrect Answer\n")
        points=points+5
        rounds=rounds+1
    else:
        print("Incorrect Answer")
        break
print("Your total points are: "+ str(points))


# computer-user
probabilityies = {
    "Stone-Stone":"Tie",
    "Stone-Scissor":"Computer wins",
    "Stone-Paper":"User wins",
    "Scissor-Scissor":"Tie",
    "Scissor-Stone":"User wins",
    "Scissor-Paper":"Computer wins",
    "Paper-Paper":"Tie",
    "Paper-Stone":"Computer wins",
    "Paper-Scissor":"User wins"
}
Tie = 0
Computer = 0
User = 0
life = 10
def computer_choice():
    import random
    list1 = ["Stone","Scissor","Paper"]
    result = random.choice(list1)
    return result

def playGame(user_name):
    global life,Tie,Computer,User;
    while life!=0:
        life-=1
        print(f"\t\t\t\t\t\t\t\tlife:{life}\nScore Card:\t\tComputer: {Computer}\t\t\t\t\t{user_name}: {User}\t\t\t\t\tTie: {Tie}")
        user_choice = int(input("Chose (1-Stone/2-Scissor/3-Paper) "))
        if(user_choice==1):
            user_choice = "Stone"
        elif(user_choice==2):
            user_choice = "Scissor"
        elif(user_choice==3):
            user_choice = "Paper"
        user_choice = user_choice.capitalize()
        C_choice = computer_choice()
        check_winer = f"{C_choice}-{user_choice}"
        winer_result = probabilityies[check_winer]
        if(winer_result=="Tie"):
            Tie+=1
            print("\nIt's an Tie\n")
        elif(winer_result=="Computer wins"):
            Computer+=1
            print("\nComputer wins\n")
        elif(winer_result=="User wins"):
            User+=1
            print(f"\n{user_name} wins\n")

def scoreBoard(user_name):
    print("***************************** Result *****************************")
    print(f"{user_name}'s Score Card:\nComputer: {Computer}\n{user_name}: {User}\nTie: {Tie}")
    if(Computer>User and Computer>Tie):
        print("Oppps computer won the match ")
    elif(User>Computer and User>Tie):
        print("Bravo! you won the match ")
    elif(Tie>Computer and Tie>User):
        print("Well try its an draw")
    elif(Computer==User):
        print("Well try its an draw")
    else:
        print("Try again")
    print("***************************** Result *****************************")


for i in range(18):
    print("\U0001F93E",end="")
print(" ",end="")
print("Stone Paper Scissor Game",end="")
    
print(" ",end="")
for i in range(18):
    print("\U0001F93E",end="")
print("\n\n\n")
user_name = input("Enter your name: ")
playGame(user_name)
scoreBoard(user_name)
input()
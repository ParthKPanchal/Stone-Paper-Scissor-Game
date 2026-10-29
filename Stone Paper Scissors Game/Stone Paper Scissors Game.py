'''
-1 - Stone
0 - Paper
1 - Scissor
'''
import random
computer=random.choice([-1,0,1])
youstr=input("Enter your choice (Stone, Paper, Scissor): ").lower()
youDist={"stone":-1,"paper":0,"scissor":1}
reverseDist={-1:"Stone",0:"Paper",1:"Scissor"}

you=youDist[youstr]
print(f"You chose {reverseDist[you]} \nComputer chose {reverseDist[computer]}")

if(computer==you):
    print("It's a tie!")

else:
    if(computer==-1 and you == 1):
        print("You Lose! Computer wins!")

    elif(computer==-1 and you == 0):
        print("You Win! Computer loses!")

    elif(computer==0 and you == -1):
        print("You Lose! Computer wins!")

    elif(computer==0 and you == 1):
        print("You Win! Computer loses!")

    elif(computer==1 and you == 0):
        print("You Lose! Computer wins!")

    elif(computer==1 and you == -1):
        print("You Win! Computer loses!")

    else:
        print("Invalid input! Please enter Stone, Paper, or Scissors.")


import random

def GameWin(comp,you):
    if(comp == you):
        return None
    
    elif comp == "S":
        if you == "W":
            return False
        elif you == "G":
            return True
    
    elif comp == "W":
        if you == "G":
            return False
        elif you == "S":
            return True

    elif comp == "G":
        if you == "S":
            return False
        elif you == "W":
            return True


print("Computers turn snake(S), water(W),gun(G)")
RandomNo=random.randint(1,3)

if RandomNo == 1:
    comp = "S"
elif RandomNo == 2:
    comp = "W"
elif RandomNo == 3:
    comp = "G"


you = input("Your Turn Snake(S),water(W),gun(G):-  ")

if(you!="G" or you!="S" or You!="W" ):
    print("Please Enter Correct Choice Snake(S), Water(W) , Gun()")
    you = input("Your Turn Snake(S),water(W),gun(G):-  ")


a = GameWin(comp,you)

print(f"Computer Choose {comp}")
print(f"You Choose {you}")

if a == None:
    print("The Game Is Tied!!!!")
elif a == True:
    print("Congratulations You Won Game!!!")

else:
    print("You Loose the game!!!")

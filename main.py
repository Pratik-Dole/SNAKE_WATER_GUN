# This Is Our 1st Project, Where We Create A Game Which Is A Snake, Water, Gun Game. 

# Rules.
# --> Here, 1 Denotes -> Snake
# --> Here, 2 Denotes -> Water
# --> Here, 3 Denotes -> Gun
# --> Same Options Gives Draw As A Result
# --> Snake Win Over Water 
# --> Water Win Over Gun 
# --> Gun Win Over Snake 

# Firstly We Take Computer's Input.
import random

computer = random.randint(1,3)
# print(computer)   # Checking For Computer Input

# Take User Input
print("")   # Empty Print For Spacing.
print(f":: Welcome To The Snake Water Gun Game ::\n")
print(f"Choose One From --> Snake, Water, Gun")
print(f"Enter 1 For \"Snake\"")
print(f"Enter 2 For \"Water\"")
print(f"Enter 3 For \"Gun\"\n")
userInput = int(input("Enter Your No : "))
print("")   # Empty Print For Spacing.
# print(userInput)       # Checking For User Input

# Create A Check For Proper Input.
if(userInput == 1 or userInput == 2 or userInput == 3):
    print("Let's Play\n")

else:
    print("Please Enter A Valid Number Between 1 To 3")

# Create Win Scenario Over Computer.
if(computer == 1 and userInput == 3):
    print("You Win !")
elif(computer == 2 and userInput == 1):
    print("You Win !")
elif(computer == 3 and userInput == 2):
    print("You Win !")

# Create Lose Scenario Over Computer.
if(computer == 1 and userInput == 2):
    print("You Lose, Better Luck Time !")
elif(computer == 2 and userInput == 3):
    print("You Lose, Better Luck Time !")
elif(computer == 3 and userInput == 1):
    print("You Lose, Better Luck Time !")

# Create Draw Scenario Over Computer.
if(computer == 1 and userInput == 1):
    print("It's A Draw !")
elif(computer == 2 and userInput == 2):
    print("It's A Draw !")
elif(computer == 3 and userInput == 3):
    print("It's A Draw !")

# So, Finally We Nailed It.
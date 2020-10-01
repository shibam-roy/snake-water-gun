import random

gap="                                                                                 "
# list of choices
choice=["stone","paper","scissors"]
# wins,losses and tie
tie="tie! no one gets any point\n"
win="user got a point!\n"
lose="computer got a point!\n"
# variables
no_of_chances=10
chances=0
computerkapoint=0
playerkapoint=0
# functions
print("choose- stone,paper or scissors")
if chances<no_of_chances:
        user=input()
        computer=random.choice(choice)
        print("computer's choice:-",computer)
        chances +=1
        if user=='stone':
                pass
        if user=='scissor':
                pass
        if user=='paper':
                pass
        else:
                print('no such command')
                playerkapoint-=1



        
               
# tie condition
if user==computer:
	print(tie)
	
#win conditions

if user=="stone" and computer=="scissors":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

elif user=="paper" and computer=="stone":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

elif user=="scissors" or "scissor" and computer=="paper":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

#lose conditions

elif computer=="stone" and user=="scissors":
        print(lose)
        computerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

elif computer=="paper" and user=="stone":
        print(lose)
        computerkapoint += 1  
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

elif computer=="scissors" or "scissor" and user=="paper":
        print(lose)
        computerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)


#game exit and game over condition

if chances>no_of_chances:
        print("game over")
        if playerkapoint>computerkapoint:
                print("you win!")
                
        else:
                print("you loose, computer won!")

#2
                
if chances<no_of_chances:
        user=input()
        computer=random.choice(choice)
        print("computer's choice:-",computer)
        chances +=1
else:
        print("no such command")

        
               
# tie condition
if user==computer:
	print(tie)
	
#win conditions

if user=="stone" and computer=="scissors":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

elif user=="paper" and computer=="stone":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

elif user=="scissors" or "scissor" and computer=="paper":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

#lose conditions

elif computer=="stone" and user=="scissors":
        print(lose)
        computerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

elif computer=="paper" and user=="stone":
        print(lose)
        computerkapoint += 1  
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

elif computer=="scissors" or "scissor" and user=="paper":
        print(lose)
        computerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)


#game exit and game over condition

if chances>no_of_chances:
        print("game over")
        if playerkapoint>computerkapoint:
                print("you win!")
                
        else:
                print("you loose, computer won!")



#3

if chances<no_of_chances:
        user=input()
        computer=random.choice(choice)
        print("computer's choice:-",computer)
        chances +=1
else:
        print("no such command")

        
               
# tie condition
if user==computer:
	print(tie)
	
#win conditions

elif user=="stone" and computer=="scissors":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

elif user=="paper" and computer=="stone":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

elif user=="scissors" or "scissor" and computer=="paper":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

#lose conditions

elif computer=="stone" and user=="scissors":
        print(lose)
        computerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

elif computer=="paper" and user=="stone":
        print(lose)
        computerkapoint += 1  
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

elif computer=="scissors" or "scissor" and user=="paper":
        print(lose)
        computerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)


#unknown

if chances<no_of_chances:
        user=input()
        computer=random.choice(choice)
        print("computer's choice:-",computer)
        chances +=1
else:
        print("no such command")

        
               
# tie condition
if user==computer:
	print(tie)
	
#win conditions

if user=="stone" and computer=="scissors":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

if user=="paper" and computer=="stone":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

if user=="scissors" or "scissor" and computer=="paper":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

#lose conditions

if computer=="stone" and user=="scissors":
        print(lose)
        computerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

if computer=="paper" and user=="stone":
        print(lose)
        computerkapoint += 1  
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

if computer=="scissors" or "scissor" and user=="paper":
        print(lose)
        computerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)





#4

if chances<no_of_chances:
        user=input()
        computer=random.choice(choice)
        print("computer's choice:-",computer)
        chances +=1
else:
        print("no such command")

        
               
# tie condition
if user==computer:
	print(tie)
	
#win conditions

if user=="stone" and computer=="scissors":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

if user=="paper" and computer=="stone":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

if user=="scissors" or "scissor" and computer=="paper":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

#lose conditions

if computer=="stone" and user=="scissors":
        print(lose)
        computerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

if computer=="paper" and user=="stone":
        print(lose)
        computerkapoint += 1  
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

if computer=="scissors" or "scissor" and user=="paper":
        print(lose)
        computerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)


#game exit and game over condition

if chances>no_of_chances:
        print("game over")
        if playerkapoint>computerkapoint:
                print("you win!")
                
        else:
                print("you loose, computer won!")


#5

if chances<no_of_chances:
        user=input()
        computer=random.choice(choice)
        print("computer's choice:-",computer)
        chances +=1
else:
        print("no such command")

        
               
# tie condition
if user==computer:
	print(tie)
	
#win conditions

if user=="stone" and computer=="scissors":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

if user=="paper" and computer=="stone":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

if user=="scissors" or "scissor" and computer=="paper":
        print(win)
        playerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

#lose conditions

if computer=="stone" and user=="scissors":
        print(lose)
        computerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

if computer=="paper" and user=="stone":
        print(lose)
        computerkapoint += 1  
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)

if computer=="scissors" or "scissor" and user=="paper":
        print(lose)
        computerkapoint += 1
        print("users point is:-",playerkapoint)
        print("computer's point is:-",computerkapoint)


#game exit and game over condition

if chances>no_of_chances:
        print("game over")
        if playerkapoint>computerkapoint:
                print("you win!")
                
        else:
                print("you loose, computer won!")
















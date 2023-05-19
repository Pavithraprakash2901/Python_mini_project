import random

print("Welcome to our game!>>>>")

name =input("Enter your name!!    ")

print("Are you ready to play" +  name +"  ")

ans=input("Enter Y for yes , N for no  ").lower()
if(ans=='n'):
    print("Thank you>>>...!!!")
    quit();
    
else:
    

    user_wins=0
    computer_wins=0

    options=["r","p","s"]

    while(True):
        user_input=input("Enter Type Rock-->r/Paper-->p/Scissors-->s or 'Q' TO QUIT  : ").lower()
       
        if(user_input== "q"):
            print("Your score" +str(user_wins))
            print("Computer score " + str(computer_wins))
            if(user_input > computer_pick):
                print("********Hooray...!!! YOU NAILED IT...!! :) ****")
            elif(user_input==computer_pick):
                print("****The war is Draw>>>*****")
            else:
                print("******SORRY.... YOU LOST!! :(  *******")
            break
   
        if user_input not in options:
            continue
    
        random_number=random.randint(0,2)
        computer_pick=options[random_number]
    
        print("computer Picked" , computer_pick +".")
        
        if(user_input == computer_pick):
            print("TIEE........")
        
        else:    
    
            if user_input=='r' and computer_pick=='s':
               print("You win!")
               user_wins+=1
    
            elif  user_input=='p' and  computer_pick =='r':
               print("You win!")
               user_wins+=1
        
            elif  user_input=='s' and  computer_pick=='p':
               print("You win!")
               user_wins+=1
    
            else:
               print("You Lost")
               computer_wins+=1 


print("Good Bye... See You Again :)")

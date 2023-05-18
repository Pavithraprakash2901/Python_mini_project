import random


name=input("Enter your name: ")


top_of_range=input("Enter the range for a number: ")

if(top_of_range.isdigit()):
    top_of_range=int(top_of_range)
    
    if(top_of_range == 0):
        print("Please Enter no greater than zero:  ")
        quit()
        
    
        
else:
    print("This is not a number.Enter a number next time! :( ")
    quit()
    
random_number=random.randint(0,top_of_range)

while(True):
    user_guess=input("Make a guess lah!!!---->")
    if(user_guess.isdigit()):
        user_guess=int(user_guess)
        
    else:
        print("This is not a number.Enter a number Next time! :( ")
        continue
    
    if(user_guess==random_number):
        print("Hooray...!! " +name +" :) You did it. ");
        quit();
        
    else:
        if(user_guess > random_number):
            print("Your guess is above the random number")
        else:
            print("Your guess is below the random number")
            
            
            

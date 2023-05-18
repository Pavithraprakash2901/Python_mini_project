print("Welcome to my Computer Quiz: ")

name=input("Enter Your Name: ")

print("Do yu wnt to play our Game : ")

score=0

playing=input("Enter your choice(Yes/No): ").lower()
if(playing != "yes" ):
    quit()
else:
    print("\n")     
    print("okay... lah!! Let's Play : ) ")
     
answer=input("What does CPU stands for? ").lower()
if(answer == "central processing unit"):
    score+=1 
    print("***Correct**** :) ")
else:
    print("***Incorrect*** :( ")
        

   
answer=input("What does RAM stands for? ").lower()
if(answer == "random access memory"):
    score+=1 
    print("***Correct*** :) ")
else:
    print("***Incorrect*** :( ")      
    
    
answer=input("What does ROM stands for? ").lower()
if(answer == "read only memory"):
    score+=1 
    print("***Correct*** :) ")
else:
    print("***Incorrect*** :( ")          

print("\n")             
print( " :) Hey " + name + " :> your's score is : " +str(score))        
print("You got  " + str((score/3)*100)  +"  of the questions correct!!" )







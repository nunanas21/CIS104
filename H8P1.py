import random 

def RollRandomNumber():
    return random.randint(1,7)

keepGoing = True
while (keepGoing): #input while above step one because we want to get random number each time 
    randNumber = RollRandomNumber() #step 1
    print (randNumber) #step 2
    
    answer=input("Would you like to roll again Yes or No?") #step3
    #if so, 
    if answer.upper ()== "YES" or answer.upper() =="Y": #changes what is inputed to upper case
        print ("OK we'll roll again.") #repeat
        keepGoing = True #if not, 
    else: #exit 
        print ("Goodbye!")
        keepGoing = False

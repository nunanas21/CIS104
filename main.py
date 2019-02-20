import calculator


n1= float(input("Enter first number ")) #user enters the first number
n2= float(input("Enter second number ")) #user enters the second number
oper= str(input("Please select operation +, - , * , or / ")) # user selects the operative


if (oper == '+'):  
    Cvalue = calculator.add (n1, n2)
    print (Cvalue)
  
if (oper == '-'):
    Cvalue = calculator.subtract (n1, n2)
    print (Cvalue)

if (oper == '*'):
    Cvalue = calculator.multiply (n1, n2)
    print (Cvalue)

if  (oper =='/'):
    Cvalue = calculator.divide (n1, n2) # hey pull up the calcultaor function
    print (Cvalue)

if (oper == 'i'or 'I'): # if user inputs lower case or uppercase I 
    Cvalue = calculator.invert (n1)
    print (Cvalue)
 
if (oper == '^'):
    Cvalue = calculator.power (n1, n2 )
    print (Cvalue)


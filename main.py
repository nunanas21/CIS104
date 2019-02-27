import calculator
import unittest


n1= float(input("Enter first number ")) #user enters the first number
n2= float(input("Enter second number ")) #user enters the second number
oper= str(input("Please select operation +, - , * , or / ")) # user selects the operative

while (oper !='x'): # while the operator does not equal to x. Do the following below
    
    if (oper == '+'):  
        value = calculator.add (n1, n2)
        print (value)
  
    elif (oper == '-'):
        value = calculator.subtract (n1, n2)
        print (value)

    elif (oper == '*'):
        value = calculator.multiply (n1, n2)
        print (value)

    elif  (oper =='/'):
        value = calculator.divide (n1, n2) # hey pull up the calcultaor function
        print (value)

    elif (oper.upper == "I"): # if user inputs lower case or uppercase I 
         value = calculator.invert (n1)
         print (value)
 
    elif (oper == '^'):
         value = calculator.power (n1, n2 )
         print (value)
    elif (oper=='r'):
        calculator.recall
    elif (op == 's'):
        calculator.cur_store

    n1= float(input("Enter first number ")) #user enters the first number
    n2= float(input("Enter second number ")) #user enters the second number
    oper= str(input("Please select operation +, - , * , or / ")) # user selects the operative



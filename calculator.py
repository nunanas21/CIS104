



current_memory = 0.0


def add (n1 , n2): # add the two numbers and return the sum
    return n1 +n2
def subtract (n1, n2): #subtract the two numbers and return the difference
    return n1- n2
def multiply (n1, n2): #multiply the two numbers and return the product
    return n1* n2
def divide (n1, n2): #divide the to numbers and return the quotiant
    return n1/n2

def invert (n1): #invert the two numbers by multiplying by negative 1
    return n1 * -1

def power (n1, n2): # 
    return n1 ^ n2 

def recall(): #recall the current memory that was stored
    return current_memory

def cur_store(n1): # it will store the current value 
    current_memory + n1

def clr(): # clear the current memory value 
    global current_memory
    current_memory = 0.0

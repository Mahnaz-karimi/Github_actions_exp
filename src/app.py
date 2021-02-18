from flask import Flask
import random

app = Flask(__name__)

if __name__== "__main__":
    app.run()
    
def square(digit):
    #digit = int(input("Enter an integer number: "))
    #   calculate square using exponent operator
    square = digit**2
    print(f"Square of {digit} is {square}")
    return square
    
def div(a, b):
    if b != 0:
        c = a/b
    else:
        c = "you cant divide to zero"
    return c

def multi(a,b):
   return a*b

def sum(a,b):
    return a+b

def subtract(a,b):
    return a-b

def boolean(a):
    if a<0:
        return True
    else:
        return False
    
@app.route("/")
def index():
    a = random.randint(-150, 150)
    b= square(a)   
    c= "Square of {} is {}.  ".format(a, b)
    d = random.randint(-150, 150)
    if d != 0:
        f = a/d
        st = "/n div of {} on {} is : {}".format(a, d,f)
    else:
        st = "/n you cant divide to zero"
    
    
    return c, st

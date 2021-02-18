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
    
@app.route("/")
def index():
    a = random.randint(-150, 150)
    b= square(a)   
    c= "Square of {} is {}.".format(a, b)
    return c

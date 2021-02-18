from flask import Flask

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
    a=10
    b= square(a)    
    return "Square of {a} is {b}"

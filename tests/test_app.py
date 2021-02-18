from app import square,div,multi
import random
def test_square():
    a = random.randint(-150, 150)
    b= a*a
    assert b == square(a)

def test_div():
    a = random.randint(-150, 150)
    b = random.randint(-150, 150)
    if b != 0:
        c = a/b
    else:
        c = "you cant divide to zero"
    assert c == div(a,b)

def test_multi():
    a = random.randint(-150, 150)
    b = random.randint(-150, 150)
    c= a*b
    assert c == multi(a,b)
    

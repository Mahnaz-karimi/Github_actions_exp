from app import square
import random
def test_square():
    a = random.randint(-150, 150)
    b= a*a
    assert b == square(a)

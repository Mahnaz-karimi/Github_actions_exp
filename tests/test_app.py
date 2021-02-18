from app import index, square
def test_index():
    a=10
    b= square(a)    
    c="Square of {a} is {b}"
    assert index() == c

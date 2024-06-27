print("hello world")

def outer():
    def inner():
        print("inner")

    return inner

def factor():
    pass

# this is added by amit

class Emlpoyee:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
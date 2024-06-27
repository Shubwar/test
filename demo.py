print("hello world")

def outer():
    def inner():
        print("inner")

    return inner


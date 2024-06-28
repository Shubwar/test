from .constants import USERNAME, PASSWORD

def login(user, password):
    """login function"""
    if user == USERNAME and password == PASSWORD:
        print("user logged in successfully")
    else:
        print("invalid credentials")

def logout():
    print("successfully logged out")
    
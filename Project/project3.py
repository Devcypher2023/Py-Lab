username = input("Please enter the username: ")
password = input("please enter the password: ")
user = ("admin")
passw = ("admin")

if username == user and password == passw:
    print("successfully login")
else:
    print("wrong username or password")
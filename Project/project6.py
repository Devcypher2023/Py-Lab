 #!/usr/bin/python3
a = input("please enter your first integer: ")
b = input("please enter your sceond integer: ")
x = a.isdigit()
y = b.isdigit()

if x == True and y == True:
    z = int(a) + int(b)
    print(f"The sum of {a} and {b} is: {z}")
else:
    print("invalid entry")
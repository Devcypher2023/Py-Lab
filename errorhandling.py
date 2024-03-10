"""
a=10
try:

    print(a)
except Exception as e:
    print(e)
#else:
    #print("no error")


print("hello")
"""
try:
    int1 = int(input("Enter int: "))
    int2 = int(input("Enter int: "))
    sum = int1 + int2
    print(sum)
except ValueError:
    print("Error")
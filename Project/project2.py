string = input("Enter a string: ")
a = len(string.strip())

if a < 4:
    print(f"The string you enterd in is: {string.strip()} and it is {a} characters long this is an invalid entry")
else:
    print(f"The string you enterd in is: {string.strip()} and it is {a} characters long this is a valid entry")
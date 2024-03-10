email = input("Please enter your email address: ")
value_bool = '@' in email
if value_bool == True:
    print("email is valid")
else:
    print("invalid entry")
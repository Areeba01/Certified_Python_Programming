fn=input("Enter your first name: ")

ln=input("Enter your last name: ")
fullname=fn+" "+ln
print("your full name is: ",fullname)
revname=list(reversed(fullname))
print("your reversed full name is :",end="")
for i in revname:
    print(i,end="")

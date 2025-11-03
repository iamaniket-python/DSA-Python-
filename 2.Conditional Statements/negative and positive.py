x=int(input("Enter a first Number="))
y=int(input("Enter a second number="))
z=int(input("Enter a third number="))

if ( x > y  and x > z):
    print(f"{x} is greatest number")
elif (y > x and y > z):
    print(f"{y} is the greatest number")
elif (z > x and z > y):
    print(f"{z} is the gretaest number ")
else:
    print("hello India")
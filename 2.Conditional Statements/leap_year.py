x=int(input("Enter a year:"))

if ( x % 4 ==0 and x % 400 == 0):
    print("it is a leap year")
else:
    print("it is not a leap year")
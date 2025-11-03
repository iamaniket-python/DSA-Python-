x=int(input("Enter a number="))

if( x < 5):
    print("0 % tax",x)
elif ( x < 10):
    print("with 20% tax" ,x * 100000 * 0.2)
else:
    print("with 30 % tax", x * 100000 * 0.3)
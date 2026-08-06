# Find the smallest element in a list.

numbers=list(map(int,input("Enter a number=").split()))

smallest= numbers[0]

for num in numbers:
    if num < smallest:
        largest =num

print("smallest element",smallest)
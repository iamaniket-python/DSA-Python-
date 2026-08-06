# Find the largest element in a list

numbers=list(map(int,input("Enter a number=").split()))

largest= numbers[0]

for num in numbers:
    if num >largest:
        largest =num

print("Largest element",largest)
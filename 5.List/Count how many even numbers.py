# Count how many even numbers are in a list

numbers = [2, 7, 10, 15, 8, 3, 12]
count=0
for i in numbers:
    if i % 2 == 0:
        count += 1
print(count)

# output= 4
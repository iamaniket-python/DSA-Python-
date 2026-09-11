# Count Divisible by 5

numbers = [10, 12, 25, 33, 40, 47, 50]
count =0
for i in numbers:
    if i % 5 == 0:
        count +=1

print(count)
# Count how many numbers are greater than 50.

numbers = [25, 67, 12, 89, 45, 72, 34, 55]
count =0
for i in numbers:
    if i > 50:
        count += 1
print(count)
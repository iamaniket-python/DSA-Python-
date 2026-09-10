# Find minimum number

numbers=[45,12,78,9,56]
min_num= numbers[0]
for i in numbers:
    if i < min_num:
        min_num = i

print(min_num)
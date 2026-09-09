# Write a program to find the second largest number in a list

numbers=[10, 5, 20, 8, 15]
largest_numbers=0
second_largest =0

for i in numbers:
    if i > largest_numbers:
        second_largest =largest_numbers
        largest_numbers = i

    elif i > second_largest:
        second_largest = i

print(second_largest)









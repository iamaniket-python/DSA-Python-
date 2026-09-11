# Remove Duplicates

numbers = [10, 20, 10, 30, 20, 40, 30]

empty_list=[]

for i in numbers:
    if i not in empty_list:
        empty_list.append(i)

print(empty_list)


# OUTPUT=[10, 20, 30, 40]
# Reverse a list without using reverse() or slicing

numbers=[34,32,45,78]
reverse_list=[]

for i in range(len(numbers) -1,-1,-1):
    reverse_list.append(numbers[i])

print(reverse_list)
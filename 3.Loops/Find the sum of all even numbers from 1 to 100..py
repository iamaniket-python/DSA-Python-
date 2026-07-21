# Find the sum of all even numbers from 1 to 100.
total_sum=0
for i in range(1,101):
    if (i % 2 ==0):
        total_sum +=1

print("Sum of even numbers ",total_sum)
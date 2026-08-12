# give an array with some interger type values .write a python script to sort array values?

arr=[23,43,56,21,45,78,87]
n=len(arr)

for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] =arr[j+1],arr[j]

print("sorted array",arr)

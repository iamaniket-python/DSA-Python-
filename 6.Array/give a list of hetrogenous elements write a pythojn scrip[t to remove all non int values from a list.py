arr = [10, "Aniket", 25, 3.14, "Python", 40, True, 55]

result = []

for item in arr:
    if type(item) == int:
        result.append(item)

print("Original list:", arr)
print("Integer values:", result)
def two(nums, target):
    n_map = {}

    for i, num in enumerate(nums):
        indi = target - num
        if indi in n_map:
            return [n_map[indi], i]
            n_map[num] = i


print(two([2, 7, 11, 15],9))
# print(two([3,2,4],6))
# print(two([3,3],6))
print(two([2, 7, 11, 15], 9))
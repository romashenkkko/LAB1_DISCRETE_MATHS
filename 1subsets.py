given_set = [[], [1, 2], 1, 2, 3]


def power_set(nums):
    subsets = [[]]
    for element in nums:
        new_subsets = [subset + [element] for subset in subsets]
        subsets.extend(new_subsets)
    return subsets


result = power_set(given_set)
print(result)
print("Number of power set elements is", len(result))

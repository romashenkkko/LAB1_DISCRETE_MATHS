given_set = input("Enter the set: ")
given_set = eval(given_set)


def power_set(nums):
    subsets = [[]]
    for element in nums:
        new_subsets = [subset + [element] for subset in subsets]
        subsets.extend(new_subsets)
    return subsets


result = power_set(given_set)
print(result)
print("Number of power set elements is", len(result))

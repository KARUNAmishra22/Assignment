dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

# (a) Concatenate dictionaries
nums = {**dic1, **dic2, **dic3}

# (b) Add a new key/value pair
nums[7] = 70

# (c) Update the value of the item with key 3
nums[3] = 80

# (d) Remove the third item (key 5) from dictionary
key_to_remove = list(nums.keys())[2]
del nums[key_to_remove]

# (e) Sum all the items in the dictionary
sum_values = sum(nums.values())

# (f) Multiply all the items in the dictionary
from functools import reduce
import operator
product_values = reduce(operator.mul, nums.values(), 1)

# (g) Retrieve the maximum and minimum values in nums
max_value = max(nums.values())
min_value = min(nums.values())

print(f"Concatenated dictionary: {nums}")
print(f"Sum of all items: {sum_values}")
print(f"Product of all items: {product_values}")
print(f"Max value: {max_value}, Min value: {min_value}")
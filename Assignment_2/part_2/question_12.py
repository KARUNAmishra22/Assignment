# Create two sets
set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

# (a) Perform a union of the sets and print the length
union_set = set1 | set2
print(f"Union of sets: {union_set}")
print(f"Length of the union set: {len(union_set)}")

# (b) Perform an intersection of set1 and set2
intersection_set = set1 & set2
print(f"Intersection of sets: {intersection_set}")

# (c) Compute the symmetric difference between set1 and set2
symmetric_difference = set1 ^ set2
print(f"Symmetric difference: {symmetric_difference}")

# (d) Add the value 40 to set1 and check if the set changes
set1.add(40)  # Adding 40 to set1 (it won't change as 40 is already in set1)
print(f"Set1 after adding 40: {set1}")

# (e) Remove value 20 from set2
set2.remove(20)  # Removes the value 20 from set2
print(f"Set2 after removing 20: {set2}")

def compare_lists():
    # Prompt user to enter integer values for two lists
    list1 = list(map(int, input("Enter integers for the first list (separated by spaces): ").split()))
    list2 = list(map(int, input("Enter integers for the second list (separated by spaces): ").split()))

    # (a) Check if the lists are of the same length
    if len(list1) == len(list2):
        print("The lists are of the same length.")
    else:
        print("The lists are not of the same length.")

    # (b) Check if the elements in each list sum to the same value
    if sum(list1) == sum(list2):
        print("The sums of the elements in both lists are the same.")
    else:
        print("The sums of the elements in both lists are not the same.")

    # (c) Check if there are any values that occur in both lists
    common_values = set(list1) & set(list2)
    if common_values:
        print(f"The following values occur in both lists: {common_values}")
    else:
        print("There are no values that occur in both lists.")

# Example usage
compare_lists()

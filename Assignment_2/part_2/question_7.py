def count_a_in_names():
    # Prompt the user to enter a list of names
    names = input("Enter a list of names (separated by spaces): ").split()

    # Initialize a counter for the letter 'a'
    count_a = 0

    # Loop through each name in the list
    for name in names:
        count_a += name.lower().count('a')  # Count occurrences of 'a' in each name (case-insensitive)

    print(f"The letter 'a' appears {count_a} times in the list of names.")

count_a_in_names()


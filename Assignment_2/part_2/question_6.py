def filter_numbers():
    numbers = []
    while True:
        try:
            num = int(input("Enter an integer (or a non-integer to stop): "))
            if 1 <= num <= 100:
                numbers.append(num)
        except ValueError:
            break
    return numbers

result = filter_numbers()
print(f"Filtered numbers between 1 and 100: {result}")


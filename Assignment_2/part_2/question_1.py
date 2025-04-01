def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    
    return {"Uppercase Letters": upper_count, "Lowercase Letters": lower_count}

# Example usage:
input_string = "Hello World!"
result = count_upper_lower(input_string)
print(result)

def count_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            # Counting lines
            num_lines = len(lines)
            
            # Counting words and characters
            num_words = 0
            num_characters = 0
            for line in lines:
                words = line.split()  # Split line into words
                num_words += len(words)  # Add number of words in the line
                num_characters += len(line)  # Add the number of characters in the line
            
            # Output the results
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_characters}")
    
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = input("Enter the path to the text file: ")
count_file_contents(file_path)

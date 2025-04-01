def find_and_replace_word(file_path, old_word, new_word):
    try:
        # Open the file in read mode to get its content
        with open(file_path, 'r') as file:
            content = file.read()

        # Replace the old word with the new word
        updated_content = content.replace(old_word, new_word)

        # Open the file in write mode to update it with the new content
        with open(file_path, 'w') as file:
            file.write(updated_content)

        print(f"Successfully replaced '{old_word}' with '{new_word}' in the file.")

    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = input("Enter the path to the file: ")
old_word = input("Enter the word to be replaced: ")
new_word = input("Enter the word to replace it with: ")

find_and_replace_word(file_path, old_word, new_word)

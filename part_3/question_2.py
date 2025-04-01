def copy_file_contents(source_file, destination_file):
    try:
        # Open the source file in read mode and the destination file in write mode
        with open(source_file, 'r') as src_file:
            content = src_file.read()  # Read the entire content of the source file
        
        # Open the destination file in write mode
        with open(destination_file, 'w') as dest_file:
            dest_file.write(content)  # Write the content to the destination file

        print(f"Contents successfully copied from '{source_file}' to '{destination_file}'.")

    except FileNotFoundError:
        print(f"The source file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = input("Enter the path to the source file: ")
destination_file = input("Enter the path to the destination file: ")

copy_file_contents(source_file, destination_file)

def main():
    # We know the filename is learn.txt
    input_filename = "learn.txt"
    
    try:
        # Try to open and read the file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            print(f"Successfully read {len(content)} characters from {input_filename}")
        
        # Modify the content (converting to uppercase)
        modified_content = content.upper()
        
        # Create output filename
        output_filename = "learn_modified.txt"
        
        # Write modified content to a new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            print(f"Successfully wrote modified content to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{input_filename}'.")
    except UnicodeDecodeError:
        print(f"Error: The file '{input_filename}' contains characters that cannot be decoded.")
        print("Try opening the file in binary mode instead.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
while True:
    input_string = input("Enter a string (or 'exit' to quit): ").strip()
    
    if input_string.lower() == 'exit':
        print("Exiting the program.")
        break
    elif len(input_string) <= 1:
        print("Input must be more than one character. Please try again.")
        continue
    
    try:
        if not input_string:
            raise ValueError("Input cannot be empty. Please enter a valid string.")
        
        reversed_string = input_string[::-1]
        
        if input_string == reversed_string:
            print(f'"{input_string}" is a palindrome. :)')
        else:
            print(f'"{input_string}" is not a palindrome. :(')
    
    except ValueError as ve:
        print(ve)




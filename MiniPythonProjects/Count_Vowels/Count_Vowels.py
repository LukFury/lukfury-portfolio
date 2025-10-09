while True:
    input_string = input("Enter a string: ")
    try:
        if input_string.strip() == "":
            raise ValueError("Input string cannot be empty.")
        vowel_count = sum(1 for char in input_string if char.lower() in "aeiou")
        print("Number of vowels:", vowel_count)
        break
    except ValueError as e:
        print("Error:", e)
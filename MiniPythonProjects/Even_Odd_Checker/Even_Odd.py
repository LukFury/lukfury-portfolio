while True:
    input_number = input("Enter a number: ")
    try:
        if not input_number.isdigit():
            raise ValueError("No letters allowed try again")
    except ValueError as e:
        print("Error:", e)
        continue
    input_number = int(input_number)
    
    if input_number % 2 == 0:
        print("Even")
    else:
        print("Odd")
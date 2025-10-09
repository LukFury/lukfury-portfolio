input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))
print("Sum of numbers:", sum(numbers))
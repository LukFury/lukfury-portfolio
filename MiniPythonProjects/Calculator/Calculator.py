import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

total = None

while True:
    if total is None:
        try:
            total = float(input("Enter the first number: ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    op = input("Enter an operator (+, -, *, /) or 'reset' to reset the calculator or 'exit' to quit: ").strip().lower()
    if op == 'reset':
        total = None
        clear()
        continue

    if op == 'exit':
        clear()
        print(f"Final result: {total}")
        break
    
    try:
        num = float(input("Enter the next number: ").strip())
        if op == '+':
            total += num
        elif op == '-':
            total -= num
        elif op == '*':
            total *= num
        elif op == '/':
            if num == 0:
                raise ValueError("Cannot divide by zero.")
            total /= num
        else:
            raise ValueError("Invalid operator. Please use +, -, *, or /.")
        clear()
        print("Current total:", total)
    except ValueError as e:
        print("Error:", e)
        continue
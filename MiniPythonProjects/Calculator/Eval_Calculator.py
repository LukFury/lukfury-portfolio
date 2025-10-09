import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

result = None
allowed_chars = "0123456789+-*/(). "

while True:
    
    expr = input("Enter a mathematical expression (or 'exit' to quit): ").strip().lower()
    
    if expr == 'exit':
        clear()
        print("Exiting the calculator.")
        break
    
    if not expr:
        print("No input provided. Please enter a valid expression.")
        continue
    
    if expr == 'reset':
        result = None
        clear()
        continue

    try:
        # Evaluate the expression safely
        if not all(char in allowed_chars for char in expr):
            raise ValueError("Invalid characters in expression.")

        # --- Smart continuation ---
        if result is not None and expr[0] in "+-*/":
            expr = str(result) + expr
            
        # Use eval with caution
        result = eval(expr, {"__builtins__": None}, {})
        print("Result:", result)
        
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("Error:", e)
import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear()
while True:
    num = input("Press enter for a Random prime number (or type 'exit' to quit): ").strip()
    if num.lower() == 'exit':
        clear()
        print("Exiting the program.")
        break
    try:
        num = random.randint(2, 100)  # Generate a random integer between 2 and 100
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"Random prime number generated: {num}")
        else:
            print(f"Random number generated: {num} (not prime)")
    except ValueError:
        clear()
        print("Please enter a valid positive integer.")
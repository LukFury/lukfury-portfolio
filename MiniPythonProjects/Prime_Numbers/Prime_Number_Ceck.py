import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear()
while True:
    
    num = input("Enter a positive integer (or 'exit' to quit): ").strip()
    
    if num.lower() == 'exit':
        clear()
        print("Exiting the program.")
        break
    try:
        num = int(num)
        
        if num <= 1:
            clear()
            print("Please enter a positive integer greater than 1.")
            continue
        
        if num > 1:
            for i in range(2, num):
                if num % i == 0: # if divisible by anything other than 1 and itself
                    clear()
                    print(f"{num} is not a prime number.")
                    break
            else:
                clear()
                print(f"{num} is a prime number.")
            break
                
    except ValueError:
        clear()
        print("Please enter a valid positive integer.")
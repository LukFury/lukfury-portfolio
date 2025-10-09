import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear()
while True:
    base_unit = input("Enter the base unit (C for Celsius, F for Fahrenheit, K for Kelvin) or type 'exit' to quit: ").strip().upper()
    if base_unit == 'EXIT':
        clear()
        print("Exiting the program.")
        break
    if base_unit not in ['C', 'F', 'K']:
        clear()
        print("Invalid base unit. Please enter C, F, or K.")
        continue
    target_unit = input("Enter the target unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()
    if target_unit == 'EXIT':
        clear()
        print("Exiting the program.")
        break
    if base_unit not in ['C', 'F', 'K']:
        clear()
        print("Invalid base unit. Please enter C, F, or K.")
        continue
    try:
        value = float(input(f"Enter the temperature value in {base_unit}: ").strip())
        if base_unit == 'C':
            if target_unit == 'F':
                converted = (value * 9/5) + 32
            elif target_unit == 'K':
                converted = value + 273.15
            else:
                converted = value
        elif base_unit == 'F':
            if target_unit == 'C':
                converted = (value - 32) * 5/9
            elif target_unit == 'K':
                converted = (value - 32) * 5/9 + 273.15
            else:
                converted = value
        elif base_unit == 'K':
            if target_unit == 'C':
                converted = value - 273.15
            elif target_unit == 'F':
                converted = (value - 273.15) * 9/5 + 32
            else:
                converted = value
        else:
            clear()
            print("Invalid base unit. Please enter C, F, or K.")
            continue
        clear()
        print(f"{value} {base_unit} is equal to {converted:.2f} {target_unit}.")
    except ValueError:
        clear()
        print("Please enter a valid temperature value.")
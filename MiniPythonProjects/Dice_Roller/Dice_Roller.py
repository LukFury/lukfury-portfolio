import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
while True:
    dice = input("Enter the type of dice you want to roll (e.g., d6, 2d20) or 'q' to quit: ").strip().lower()
    
    if dice == 'q':
        clear()
        print("Exiting the Dice Roller. Goodbye!")
        break 
    
    # ✅ Validate dice format
    if 'd' not in dice or dice.count('d') != 1:
        clear()
        print("Invalid input. Please enter a valid dice type (e.g., d6, 2d20).")
        continue
    
    # ✅ Split dice into number of dice and sides
    parts = dice.split('d')
    num_dice = int(parts[0]) if parts[0] else 1
    sides = int(parts[1])
    
    if sides <= 0:
        clear()
        print("The number of sides must be a positive integer.")
        continue

    # 🎲 Roll the dice
    results = [random.randint(1, sides) for _ in range(num_dice)]
    total = sum(results)

    clear()
    if max(results) == sides:
        print(f"Critical Hit! You rolled {dice}: {results} → Total: {total}")
    elif min(results) == 1:
        print(f"Critical Miss! You rolled {dice}: {results} → Total: {total}")
    elif all(r == sides for r in results):
        print(f"✨ PERFECT ROLL! Every die maxed out! ✨")
    elif all(r == 1 for r in results):
        print(f"💀 Catastrophic Failure! Every die rolled 1! 💀")
    else:
        print(f"You rolled {dice}: {results} → Total: {total}")


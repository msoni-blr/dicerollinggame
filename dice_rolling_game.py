import random

while True:
    command = input("Roll the dice? (y/n): ")
    if command.lower() == "y":
        print(f"({random.randint(1,6)}, {random.randint(1,6)})")
    elif command.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
import os
print("Saving to:", os.getcwd())  #This will show you exactly where Python is saving the file.

operations = {
    "1": "Add",
    "2": "Subtract",
    "3": "Multiply",
    "4": "Divide",
    "5": "Square",
    "6": "Square root",
    "7": "Cube",
    "8": "Modulus",
    "9": "Power",
    "10": "Show History",
    "11": "Clear History",
    "12": "Exit"
}

history = []

def save_to_file(entry):
    with open("history.txt", "a") as file:
        file.write(entry + "\n")

def clear_file():
    with open("history.txt", "w") as file:
        pass  # Just opens in write mode and empties the file

while True:
    # Display the menu
    print("\n--- Calculator Menu ---")
    for key, value in operations.items():
        print(f"{key}. {value}")

    # Get user input
    choice = input("Choose an operation (1-12): ").strip()  #.strip() is used bcz if we enter input with (spaces along with operation numbers it'll give output as invalid choice,
    #as we use .strip() it'll take the input and perform correct operation even if we enter the space before or after the operaation number)

    if choice not in operations:
        print("Invalid choice. Please try again.")
        continue

    print(f"You selected: {operations[choice]}")

    if choice == "12":
        print("Exiting calculator. Bye!")
        break

    elif choice == "10":
        print("Showing History:")
        if not history:
            print("No history yet.")
        else:
            for item in history:
                print(item)

    elif choice == "11":
        print("Clearing History...")
        history.clear()
        clear_file()
        print("History Cleared!")

    elif choice == "5":
        #try and except are used if we input any random input like letters instead of number then these functions will not show the error like this:  
        # ValueError: could not convert string to float
        #instead it will show: Invalid input. Please enter valid numbers and continues the calculation loop
        try:
            num = float(input("Enter a number: ").strip())
            result = num ** 2
            operation = f"{num} * {num} = {result}"
            print("Result:", operation)
            history.append(operation)
            save_to_file(operation)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "6":
        try:
            num = float(input("Enter a number: ").strip())
            result = num ** 0.5
            operation = f"√{num} = {result}"
            print("Result:", operation)
            history.append(operation)
            save_to_file(operation)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "7":
        try:
            num = float(input("Enter a number: ").strip())
            result = num ** 3
            operation = f"{num}³ = {result}"
            print("Result:", operation)
            history.append(operation)
            save_to_file(operation)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "8":
        try:
            num1 = float(input("Enter first number: ").strip())
            num2 = float(input("Enter second number: ").strip())
            result = num1 % num2
            operation = f"{num1} % {num2} = {result}"
            print("Result:", operation)
            history.append(operation)
            save_to_file(operation)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    elif choice == "9":
        try:
            num1 = float(input("Enter base number: ").strip())
            num2 = float(input("Enter exponent: ").strip())
            result = num1 ** num2
            operation = f"{num1} ^ {num2} = {result}"
            print("Result:", operation)
            history.append(operation)
            save_to_file(operation)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    elif choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: ").strip())
            num2 = float(input("Enter second number: ").strip())

            if choice == "1":
                result = num1 + num2
                operation = f"{num1} + {num2} = {result}"
            elif choice == "2":
                result = num1 - num2
                operation = f"{num1} - {num2} = {result}"
            elif choice == "3":
                result = num1 * num2
                operation = f"{num1} * {num2} = {result}"
            elif choice == "4":
                if num2 == 0:
                    operation = "Error: Cannot divide by zero."
                else:
                    result = num1 / num2
                    operation = f"{num1} / {num2} = {result}"

            print("Result:", operation)
            history.append(operation)
            save_to_file(operation)

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
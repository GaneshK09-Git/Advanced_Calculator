import os
# Python doesn’t automatically know how to calculate sine, cosine, or tangent — these are mathematical functions,
# so we import the math module which gives us access to:
# math.sin(x)
# math.cos(x)
# math.tan(x)
import math  #Needed for sin, cos, tan calculations
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
    "10": "Sine",
    "11": "Cosine",
    "12": "Tangent",
    "13": "Cosecant (1/sin)",
    "14": "Secant (1/cos)",
    "15": "Cotangent (1/tan)",
    "16": "Show History",
    "17": "Clear History",
    "18": "Exit"
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
    choice = input("Choose an operation (1-18): ").strip()  #.strip() removes any spaces before or after the operation number

    if choice not in operations:
        print("Invalid choice. Please try again.")
        continue

    print(f"You selected: {operations[choice]}")

    #Exiting Calculator:
    if choice == "18":
        print("Exiting calculator. Bye!")
        break
    
    #Showing History:
    elif choice == "16":
        print("Showing History:")
        if not history:
            print("No history yet.")
        else:
            for item in history:
                print(item)

    #Clearing History:
    elif choice == "17":
        print("Clearing History...")
        history.clear()
        clear_file()
        print("History Cleared!")

    #Square:
    elif choice == "5":
        #try and except are used for error handling.
        # Example: if we input any random input like letters instead of number then these functions will not show the error as below:  
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

    # Square root:
    elif choice == "6":
        try:
            num = float(input("Enter a number: ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue        #Only skip if there was a problem

        #This part only runs if no exception was raised
        result = num ** 0.5
        operation = f"sqrt({num}) = {result}"
        print("Result:", operation)
        history.append(operation)
        save_to_file(operation)

    #Cube:
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

    #Modulus:
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

    #Power:
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

    #Sine:
    elif choice == "10":
        try:
            angle = float(input("Enter an angle in degrees: ").strip())
            #math.sin() takes the angle in radians, not degrees. So we’ll use: math.radians(degree or angle) to convert degrees into radians
            result = math.sin(math.radians(angle)) 
            operation = f"sin({angle}°) = {result}"
            print("Result:", operation)
            history.append(operation)
            save_to_file(operation)
        except ValueError:
            print("Invalid input. Please enter a valid angle.")

    #Cosine:
    elif choice == "11":
        try:
            angle = float(input("Enter angle in degrees: ").strip())
            radians = math.radians(angle)
            result = math.cos(radians)
            operation = f"cos({angle}°) = {result}"
            print("Result:", operation)
            history.append(operation)
            save_to_file(operation)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    #Tangent:
    elif choice == "12":
        try:
            angle = float(input("Enter angle in degrees: ").strip())
            radians = math.radians(angle)
            result = math.tan(radians)
            operation = f"tan({angle}°) = {result}"
            print("Result:", operation)
            history.append(operation)
            save_to_file(operation)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    #Add, Sub, Mul, Div:
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
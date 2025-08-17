## > Python Calculator with History

---

A simple yet powerful command-line calculator built with Python.

It supports multiple mathematical operations, keeps a calculation history, and even allows saving results to a file for later reference.

---

## Features:

- Perform basic operations: Addition, Subtraction, Multiplication, Division
- Advanced operations: Square, Square Root, Cube, Power, Modulus
- Maintain a session-based calculation history
- Save history automatically to a history.txt file
- Clear history anytime (both in memory and file)
- Error handling for invalid inputs and division by zero
- User-friendly menu-driven interface

---

## 📂 Project Structure:

- Calculator-Project

   ┣ 📜 calculator.py       # Main Python script
  
   ┣ 📜 history.txt         # Stores calculation history (auto-created)
  
   ┗ 📜 README.md           # Project documentation

---

## Installation & Usage:

a. Clone the Repository
   git clone https://github.com/your-username/Calculator-Project.git
   cd Calculator-Project

b. Run the Script
- Make sure you have Python 3.x installed.

  python calculator.py

c. Use the Menu
  --- Calculator Menu ---
  1. Add
  2. Subtract
  3. Multiply
  4. Divide
  5. Square
  6. Square root
  7. Cube
  8. Modulus
  9. Power
  10. Show History
  11. Clear History
  12. Exit

---

## Example session:

  Choose an operation (1-12): 1
  
  Enter first number: 10
  
  Enter second number: 5
  
  Result: 10 + 5 = 15


## History is stored automatically in both memory and history.txt.

--- Calculator Menu ---

10. Show History


## Showing History:

10 + 5 = 15

25 - 7 = 18

9 * 3 = 27

100 / 20 = 5.0


---


## Error Handling:

- Handles invalid numeric inputs (e.g., typing letters instead of numbers)

- Prevents division by zero

- Trims unnecessary spaces in inputs using .strip()
  

---


## Contributing:

- Contributions are welcome!

- Fork the repo

- Create a new branch (feature-new-op)

- Commit changes

- Submit a Pull Request 🚀

---


## License:

This project is licensed under the MIT License – free to use and modify.

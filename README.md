### Python Basic Calculator

This simple Python program performs four basic arithmetic operations (addition, subtraction, multiplication, and division) on two user-provided numbers. It calculates all operations simultaneously and displays the formatted results.

#### Features
- Takes two numerical inputs and an operator symbol
- Performs all four arithmetic operations
- Displays formatted results including:
  - Sum of the numbers
  - Difference between the numbers
  - Product of the numbers
  - Quotient from division
- Simple command-line interface

#### How to Use
1. Run the program using Python:
   ```bash
   python calculator.py
   ```
2. Follow the interactive prompts:
   - Enter the first number when prompted
   - Enter the second number when prompted
   - Enter any one of these operator symbols: `+`, `-`, `*`, or `/`
3. View all four calculated results

#### Example
```
Enter the first number: 10
Enter the second number: 4
Enter +, -, *, or /: *

Results of your two numbers:
Sum: 14.0
Difference: 6.0
Product: 40.0
Quotient: 2.5
```

#### Important Notes
- **Division by zero**: The program will crash if you enter `0` as the second number
- **Input validation**: The program expects numerical inputs. Entering non-numeric values will cause errors
- **Operator usage**: The operator symbol you enter doesn't affect the calculations - all four operations are always performed
- **Floating-point numbers**: The program handles both integers and decimal numbers

#### Requirements
- Python 3.x installed on your system

#### Limitations
- No error handling for invalid inputs
- No support for advanced operations (exponents, roots, etc.)
- Always performs all four operations regardless of user's operator selection

This program serves as a basic demonstration of arithmetic operations in Python and is suitable for educational purposes.

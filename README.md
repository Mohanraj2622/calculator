# Virtual Calculator

This repository contains three files related to a virtual calculator application: an HTML file for a web-based calculator, a Python script for a command-line calculator, and an alternative HTML file without the `eval()` function.

## Contents

1. **calculator.html**
   - An HTML file that creates a virtual calculator interface using HTML, CSS, and JavaScript.
   - The calculator has buttons for digits, operators, and basic operations like clear, delete, and evaluate.
   - The JavaScript code handles button clicks, updates the display, and performs calculations using the `eval()` function.

2. **calculator.py**
   - A Python script that implements a command-line calculator.
   - The script uses regular expressions to parse user input and perform arithmetic operations.
   - It supports addition, subtraction, multiplication, and division operations.
   - Error handling is included for division by zero and invalid expressions.

3. **without_eval.html**
   - An HTML file that creates a virtual calculator interface without using the `eval()` function.
   - The calculator has a similar layout and functionality as the `calculator.html` file.
   - Instead of using `eval()`, it uses a custom JavaScript function `evaluateExpression()` to parse and evaluate the expression.
   - The `evaluateExpression()` function splits the expression into operands and operators and performs the corresponding arithmetic operations.

## Usage

### calculator.html

1. Open the `calculator.html` file in a web browser.
2. The calculator interface will be displayed.
3. Click the buttons to enter numbers and operators.
4. Click the "=" button to evaluate the expression and display the result.
5. Use the "C" button to clear the display and the "DEL" button to delete the last character.

### calculator.py

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `calculator.py` file.
3. Run the script by executing `python calculator.py`.
4. The calculator will prompt you to enter an expression.
5. Enter a valid arithmetic expression (e.g., `2 + 3`, `5.5 * 2.2`, etc.).
6. The result will be displayed.
7. To exit the calculator, enter `quit`.

### without_eval.html

1. Open the `without_eval.html` file in a web browser.
2. The calculator interface will be displayed.
3. Click the buttons to enter numbers and operators.
4. Click the "=" button to evaluate the expression and display the result.
5. Use the "AC" button to clear the expression and the "Del" button to delete the last character.

## Note

While the `calculator.html` file uses the `eval()` function for evaluation, which can be a security risk if user input is not properly sanitized, the `without_eval.html` file avoids using `eval()` and instead uses a custom function `evaluateExpression()` to parse and evaluate the expression. This approach is generally considered safer, although it may have limitations in handling more complex expressions.

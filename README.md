# Temperature Converter

A Python program that converts temperatures between Celsius and Fahrenheit based on user input.

## Features
- Lets the user choose a conversion type: Celsius to Fahrenheit or Fahrenheit to Celsius
- Accepts a temperature from the user and displays the converted result
- Prints a warning for very hot or very cold temperatures

## Requirements
- Python 3 (download from [python.org](https://www.python.org))
- On Windows, check **Add Python to PATH** during installation.

## How to Run

1. Click the green **Code** button above and choose **Download ZIP**, then unzip the folder.
2. Open the folder and make sure `temperature_converter.py` is inside it.
3. Open a terminal in that folder:
   - **Windows:** Click the address bar in File Explorer, type `powershell`, and press Enter.
   - **Mac:** Open Terminal and use `cd` to move into the folder.
4. Run the program:
   - **Windows:** `py temperature_converter.py`
   - **Mac:** `python3 temperature_converter.py`
5. Follow the prompts. Type a value and press Enter.

### Example
1. Enter `1` or `2` to choose the conversion type.
2. Enter the temperature you want to convert.

## What I Learned
- 'float' converts that string into a decimal number, so the program can do math with the temperature.
- Multiway decisions:  `if`, `elif`, and `else` form a decision structure. This program checks the user's choice in order and runs only the matching branch. Each branch works like a branch of a tree (decision tree)
- Separate checks: Additional `if` statements at the end run on their own. They print a warning when the temperature is very hot or very cold.
- Handling invalid input: When the user enters something other than `1` or `2`, the `else` branch prints an error message. The `return` statement then ends the function so the program doesn't try to use a temperature that wan't entered

## Course
Built for Computer Programming I, Messiah University

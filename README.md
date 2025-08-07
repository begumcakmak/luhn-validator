# Credit Card Number Validator (Luhn Algorithm)

This is a simple Python program that validates credit card numbers using the Luhn algorithm.

## Features

- Accepts user input for credit card numbers.
- Cleans input by removing spaces and dashes.
- Validates the number using the Luhn checksum algorithm.
- Supports exit command to quit the program.
- Handles invalid inputs gracefully.

## How It Works

The program reverses the card number and processes digits in odd and even positions separately:
- Odd-position digits are summed directly.
- Even-position digits are doubled; if the result is greater than 9, its digits are summed.
- The total sum is then checked to be divisible by 10 for a valid card number.

## Usage

1. Run the program:
   ```bash
   python card_validator.py
2. Enter a credit card number when prompted. You can include spaces or dashes.
3. Type `exit` to quit the program.

## Example

Enter card number (or type 'exit' to quit): 4539 1488 0343 6467  
VALID!

Enter card number (or type 'exit' to quit): 1234 5678 9012 3456  
INVALID!

Enter card number (or type 'exit' to quit): exit

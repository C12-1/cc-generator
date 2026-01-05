# Credit Card Generator Script

## Overview
This Python script generates random credit card numbers based on provided BIN patterns or BIN files. It creates validly formatted credit card numbers with expiration dates and CVV codes for testing and educational purposes.

## Features

- **BIN Input Support**: Accepts single BIN patterns or text files containing multiple BINs
- **Flexible Format**: Supports patterns like `456654|xx|xx|xxx` where `xx` represents random generation
- **Random Generation**: Generates random card numbers, expiration dates, and CVV codes
- **Batch Processing**: Can generate multiple cards from single or multiple BINs
- **File Output**: Saves generated cards to timestamped text files

## Installation

### Prerequisites
- Python 3.x
- Required Python packages:
  ```bash
  pip install colorama
  ```

### Setup
1. Clone or download the script
2. Ensure Python is installed on your system
3. Install the required package:
   ```bash
   pip install colorama
   ```

## Usage

### Running the Script
```bash
python script_name.py
```

### Input Options

#### Option 1: Single BIN Pattern
```
[+] write the path of the file (txt) 
[+] write the bin ex:456654|xx|xx|xxx >> 456789|05|30|123
[+] or use the all_test_inputs above
```

**Format**: `BIN|MM|YY|CVV`
- **BIN**: First 6-12 digits of the card (6-12 digits)
- **MM**: Month (01-12) or `xx` for random month
- **YY**: Year (24-33) or `xx` for random year
- **CVV**: 3-4 digit CVV or `xxx`/`xxxx` for random CVV

**Examples**:
- `456789|05|30|123` - Fixed values
- `456789|xx|30|xxx` - Random month and CVV, fixed year
- `456789|xx|xx|xxxx` - Random month, year, and 4-digit CVV

#### Option 2: BIN File
```
[+] write the path of the file (txt) 
[+] write the bin ex:456654|xx|xx|xxx >> bins.txt
```

Create a text file (`bins.txt`) with one BIN pattern per line:
```
456789|xx|30|xxx
512345|05|xx|123
378282|xx|xx|xxxx
```

### Output
- Generated cards are displayed in the console in blue text
- All generated cards are saved to a timestamped file: `YYYY-MM-DD HH-MM-SS CCs.txt`
- Each line in the output file follows the format: `CARD_NUMBER|MM|YYYY|CVV`

## Functions

### `checking()`
- Displays the script banner
- Handles user input (file path or BIN pattern)
- Validates input and returns cleaned BIN data

### `shufling()`
- Returns a random digit (0-9)

### `firts_num(num)`
- Completes the card number to 16 digits using random numbers
- Validates BIN length (must be 6-12 digits)

### `month_year(num)`
- Generates expiration date (MM|YYYY)
- Handles various input patterns with random generation where needed

### `cvv(num)`
- Generates CVV codes (3 or 4 digits)
- Supports random generation or fixed values

### `randomizing(number)`
- Main generation function
- Prompts for number of cards to generate
- Handles both single BIN and BIN list inputs
- Writes results to file and displays in console

## Examples

### Example 1: Single BIN
```
Input: 456789|xx|30|xxx
Output: 4567891234567890|05|2030|123
```

### Example 2: Multiple Cards from File
```
Input file (bins.txt):
456789|xx|30|xxx
512345|05|xx|123

Command: python script.py
Input: bins.txt
How many cards: 10
Output: Generates 10 cards for each BIN pattern
```

## Important Notes

⚠️ **DISCLAIMER**: 
- This tool is for **EDUCATIONAL PURPOSES ONLY**
- Generated credit card numbers are **NOT VALID** for real transactions
- Do not use this tool for illegal activities
- Always comply with local laws and regulations
- The creator (@C12) is not responsible for misuse

## File Structure
- `script_name.py` - Main script file
- `bins.txt` - Example BIN file (user-created)
- `YYYY-MM-DD HH-MM-SS CCs.txt` - Generated output files

## Error Handling
The script includes basic error handling for:
- Invalid file paths
- Incorrect BIN formats
- Invalid date ranges
- Input validation errors

## Requirements
- Python 3.x
- colorama library

## License
This script is provided for educational purposes. Users are responsible for ensuring they use it legally and ethically.

---
**Created by**: @C12  
**Use Responsibly**: Only use for legitimate testing and educational purposes

# Password Generator
This is a simple Python script that generates secure passwords conforming to the NIST 800-63B standard. The passwords are randomly generated and include a mix of uppercase and lowercase letters, digits, and special characters.

## Features
- Generates passwords of customizable length.
- Allows generating multiple passwords at once.
- Ensures the first character is always a letter (uppercase or lowercase).
- Complies with the NIST 800-63B standard by ensuring a minimum password length of 8 characters.

## Requirements
- Python 3.x

## Usage
1. Clone or download the repository.
2.  Run the script using Python 3.

## Command-Line Arguments
- `length`: The length of the password(s) to generate. Default is 12.
- `number`: The number of passwords to generate. Default is 1.

## Examples
1. Generate a single password with the default length (12 characters):
<pre>python3 pgen.py</pre>
2. Generate a password of length 15:
<pre>python3 password_generator.py 15</pre>
3. Generate 5 passwords of length 10:
<pre>python3 password_generator.py 10 5</pre>

## Notes
- If the specified password length is less than 8, the program will exit with an error message.
- The first character of the password is always a letter to ensure compatibility with systems that require passwords to start with a letter.

## Code Overview
The script consists of two main functions:
- `generate_password(length=12)`: Generates a single password of the specified length.
- `main()`: Handles command-line arguments and generates the requested number of passwords.

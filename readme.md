# Password Validation Program

## Description
This Python program validates user passwords based on specific conditions to ensure security. It checks for:
- Minimum length requirement.
- Inclusion of letters, numbers, and symbols.

The user can enter passwords, and the program provides feedback on whether the password meets the required conditions or not.

---

## Features
1. **Interactive User Interface**:
   - Displays password rules using the `/help` command.
   - Guides the user through entering and validating passwords.
2. **Validation Criteria**:
   - Password must be at least 8 characters long.
   - Password must include:
     - At least one letter (a-z, A-Z).
     - At least one number (0-9).
     - At least one symbol (e.g., @, #, $, etc.).
3. **Continuous Validation**:
   - Allows users to validate multiple passwords in one session.
   - Provides the option to exit after each validation.

---

## How It Works
1. The program prompts the user for input:
   - `/help` displays the password validation rules.
   - If no command is provided, it proceeds to validate passwords.
2. Users enter their password, and the program checks:
   - Length: Is it 8 or more characters?
   - Contains at least one letter, one number, and one symbol.
3. Feedback is provided for valid and invalid passwords.
4. The user can choose to validate another password or exit.

---

## Usage
1. Run the script using Python:
   ```bash
   python password_validation.py
 #fox
```markdown
# ISBN Validator

A Python program that validates ISBN-10 and ISBN-13 codes based on user input. It checks whether the entered ISBN is valid according to the checksum calculation rules, handling various input errors gracefully.

---

## Features

- Validates ISBN-10 and ISBN-13 codes.
- Handles invalid characters and incorrect lengths.
- Provides clear error messages for user mistakes.
- Uses separate functions for check digit calculations.

---

## How to Use

1. Run the program.
2. When prompted, enter the ISBN and its length separated by a comma, with no hyphens or spaces.  
   **Format:** `ISBN,Length`  
   **Examples:**  
   ``
   1530051126,10
   9781530051120,13
   080442957X,10
   ``

3. The program will output whether the ISBN code is valid or specify the type of error.

---

## Example Inputs and Expected Outputs

| Input                   | Output                     | Description                                |
|-------------------------|----------------------------|--------------------------------------------|
| `1530051126,10`         | `Valid ISBN Code.`         | Valid ISBN-10 code                       |
| `9781530051120,13`       | `Valid ISBN Code.`         | Valid ISBN-13 code                       |
| `1530051125,10`          | `Invalid ISBN Code.`       | Check digit mismatch                     |
| `1530051126,9`           | `ISBN-10 code should be 10 digits long.` | Incorrect length for ISBN-10     |
| `15-0051126,10`          | `Invalid character was found.` | Invalid character (hyphen)             |
| `1530051125,A`           | `Length must be a number.` | Non-numeric length input                |
| `1530051126,13`          | `ISBN-13 code should be 13 digits long.` | Length mismatch for ISBN-13       |

---

## Implementation Details

- **Function `validate_isbn(isbn, length)`**: Checks the validity of the ISBN based on length and checksum.
- **Function `calculate_check_digit_10(main_digits_list)`**: Computes the check digit for ISBN-10.
- **Function `calculate_check_digit_13(main_digits_list)`**: Computes the check digit for ISBN-13.
- **Input validation**: Ensures correct format, length, and characters, providing user-friendly error messages.

---

## How to Run

```python
# Uncomment the following line to enable running the main function
# main()
``

**Note:** Remember to comment out or remove the call to `main()` when running automated tests to avoid interference.

---

## License

This project is for educational purposes and is provided as-is without warranty.

---

## Contact

For questions or feedback, please contact ME At jordanleturgez@gmail.com
---

Would you like me to customize this further, add badges, or include setup instructions?

def validate_isbn(isbn, length):
    # Check if ISBN contains only valid characters (digits or 'X' if length==10)
    if length == 10:
        # ISBN-10 can have digits or 'X' as check digit
        if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
            print('Invalid character was found.')
            return
    elif length == 13:
        # ISBN-13 should be all digits
        if not isbn.isdigit():
            print('Invalid character was found.')
            return
    else:
        # Should not reach here if input validated properly
        print(f'ISBN-{length} code should be 10 or 13 digits long.')
        return

    # Validate length
    if len(isbn) != length:
        if length == 10:
            print('ISBN-10 code should be 10 digits long.')
        else:
            print('ISBN-13 code should be 13 digits long.')
        return

    main_digits = isbn[:-1]
    given_check_digit = isbn[-1]

    # Convert main digits to integers
    main_digits_list = []
    try:
        for digit in main_digits:
            main_digits_list.append(int(digit))
    except ValueError:
        print('Invalid character was found.')
        return

    # Calculate expected check digit
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Compare check digits
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    result = 11 - (digits_sum % 11)
    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    result = 10 - (digits_sum % 10)
    if result == 10:
        return '0'
    else:
        return str(result)


def main():
    user_input = input('Enter ISBN and length: ')

    # Check if input contains comma
    if ',' not in user_input:
        print('Enter comma-separated values.')
        return

    values = user_input.split(',')
    if len(values) != 2:
        print('Enter comma-separated values.')
        return

    isbn = values[0].strip()
    length_str = values[1].strip()

    # Validate length input
    try:
        length = int(length_str)
    except ValueError:
        print('Length must be a number.')
        return

    # Validate length value
    if length not in [10, 13]:
        print('Length should be 10 or 13.')
        return

    # Validate ISBN
    validate_isbn(isbn, length)

# Uncomment the following line during testing
# main()

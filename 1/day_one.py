
NUMBER_DICT = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def do_part_one(lines):
    """Function for finding Part 1 answer"""
    calibration_sum = 0

    for line in lines:
        calibration_list = []
        for character in line:
            if character.isdigit():
                calibration_list.append(character)

        calibration_sum += int(calibration_list[0] + calibration_list[-1])

    print(f"The calibration sum for Part 1 is {calibration_sum}.")

def identify_calibration_value(line_len, calibration_list):
    """Identify the calibration value"""
    min_index = line_len
    max_index = 0

    for index, value in calibration_list:
        if index <= min_index:
            min_index = index
            first_digit = value

        if index >= max_index:
            max_index = index
            second_digit = value

    return int(first_digit + second_digit)

def do_part_two(lines):
    """Function for finding Part 2 answer"""
    calibration_sum = 0

    for line in lines:
        calibration_list = []

        # Handle digit substrings
        for key, val in NUMBER_DICT.items():

            # Find first and last occurrences of substring, if any
            first_index = line.find(key)
            last_index = line.rfind(key)

            if first_index != -1:
                calibration_list.append((first_index, val))

            # If there's only one occurrence, don't store the duplicate
            if last_index not in [-1, first_index]:
                calibration_list.append((last_index, val))

        # Handle digit characters
        for index, character in enumerate(line):
            if character.isdigit():
                calibration_list.append((index, character))

        calibration_sum += identify_calibration_value(len(line) - 1, calibration_list)
    print(f"The calibration sum for Part 2 is {calibration_sum}.")

def main():
    """Main function"""
    with open('input.txt', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]

    do_part_one(lines)
    do_part_two(lines)

if __name__ == "__main__":
    main()

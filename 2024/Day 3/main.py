import re


def process_input_part_1(input):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, input)

    total = 0
    for match in matches:
        x, y = map(int, match)
        result = x * y
        total += result

    return total


def process_input_part_2(input):
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    total = 0
    mul_enabled = True

    pattern = f"({do_pattern}|{dont_pattern})"
    chunks = re.split(pattern, input)

    for chunk in chunks:
        if chunk == "do()":
            mul_enabled = True
        elif chunk == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                matches = re.findall(mul_pattern, chunk)
                for match in matches:
                    x, y = map(int, match)
                    result = x * y
                    total += result

    return total


def main():
    file_path = "files/input.txt"

    with open(file_path, "r") as file:
        input = file.read().strip()
        result = process_input_part_1(input)
        print(f"The total of all multiplications for Part 1 is: {result}")
        result = process_input_part_2(input)
        print(f"The total of all multiplications for Part 2 is: {result}")


if __name__ == "__main__":
    main()

from pathlib import Path
import numpy as np


def binary_to_fixed_length_list(number, length):
    binary_str = bin(number)[2:]  # Convert to binary and remove '0b' prefix
    padded_binary_str = binary_str.zfill(length)  # Pad with leading zeros
    return list(padded_binary_str)


def main(input: str):
    datafile = Path("day07") / input
    lines = datafile.read_text().splitlines()
    output = 0
    for line in lines:
        (result_str, numbers_str) = line.split(": ")
        result = int(result_str)
        numbers_str = numbers_str.split(" ")
        numbers = np.array([int(number) for number in numbers_str])

        num_operators = np.size(numbers) - 1  # total number of operators
        max_comb = 2**num_operators - 1  # start with '0000' -> max is '1111'

        comb = 0
        while comb <= max_comb:
            result_test = numbers[0]
            # get binary number for operator assignment (0 -> +, 1 -> *)
            operators = binary_to_fixed_length_list(comb, num_operators)
            for ind, operator in enumerate(operators):
                if operator == "0":
                    result_test += numbers[ind + 1]
                else:
                    result_test *= numbers[ind + 1]
            if result_test == result:
                output += result
                break
            else:
                comb += 1

    return output


def test():
    result = main("test.txt")
    expected = 3749
    assert result == expected, f"test failed {result} != {expected}"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)

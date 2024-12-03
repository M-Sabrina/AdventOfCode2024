from pathlib import Path
import re


def main(input: str):
    output = 0
    data = (Path("day03") / input).read_text()
    pattern_1 = re.compile(r"mul\(\d+,\d+\)")
    matches_1 = pattern_1.findall(data)
    pattern_2 = re.compile(r"\d+")
    for pair in matches_1:
        numbers = pattern_2.findall(pair)
        output = output + int(numbers[0]) * int(numbers[1])
    return output


def test():
    assert main("test1.txt") == 161, "test failed"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)

from pathlib import Path
import re


def main(input: str):
    output = 0
    data = "do" + (Path("day03") / input).read_text()
    # print(data)
    data = data.replace("\n", "")
    data = data.replace("don't", "NO")
    data = data.replace("do", "YES")
    # print(data)
    cleaned_data = re.sub(r"NO.*?YES", "", data)
    cleaned_data = re.sub(r"NO.*", "", cleaned_data)
    # print(cleaned_data)
    pattern_1 = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    matches_1 = pattern_1.findall(cleaned_data)
    pattern_2 = re.compile(r"\d+")
    for pair in matches_1:
        numbers = pattern_2.findall(pair)
        output = output + int(numbers[0]) * int(numbers[1])
    return output


def test():
    assert main("test2.txt") == 48, "test failed"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)

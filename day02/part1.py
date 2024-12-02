import numpy as np
from pathlib import Path


def main(input: str):
    data = open(Path("day02") / input)
    rowstrings = data.readlines()
    data.close()
    output = 0
    for rowstring in rowstrings:
        row = np.fromstring(rowstring, dtype=int, sep=" ")
        diff_row = np.diff(row)
        if (np.all(diff_row > 0) or np.all(diff_row < 0)) and np.all(
            np.abs(diff_row) <= 3
        ):
            output = output + 1
    return output


def test():
    assert main("test.txt") == 2, "test failed"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)

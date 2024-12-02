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
        else:
            for index, _ in enumerate(row):
                short_row = np.delete(row, index)
                diff_short_row = np.diff(short_row)
                if (
                    np.all(diff_short_row > 0) or np.all(diff_short_row < 0)
                ) and np.all(np.abs(diff_short_row) <= 3):
                    output = output + 1
                    break
    return output


def test():
    assert main("test.txt") == 4, "test failed"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)

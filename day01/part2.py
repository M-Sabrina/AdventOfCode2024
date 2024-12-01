import numpy as np
import pandas as pd
from pathlib import Path


def main(input: str):
    data = pd.read_csv(Path("day01") / input, sep="   ", header=None, engine="python")
    col1 = data.iloc[:, 0]
    col2 = data.iloc[:, 1]
    output = 0
    for n in col1:
        output = output + n * np.count_nonzero(col2 == n)
    return output


def test():
    assert main("test.txt") == 31, "test failed"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)

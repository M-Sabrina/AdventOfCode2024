import numpy as np
from pathlib import Path


def main(input: str):
    datafile = Path("day04") / input
    lines_str = datafile.read_text().splitlines()
    matrix = np.array([list(line) for line in lines_str])

    mas = np.array(["M", "A", "S"])
    sam = np.flip(mas)

    output = 0
    (rows, cols) = matrix.shape
    # search X-mas
    for row in range(rows - 2):
        for col in range(cols - 2):
            investigate = matrix[row : row + 3, col : col + 3]
            diagonal_forward = investigate.diagonal()
            diagonal_backward = np.fliplr(investigate).diagonal()
            if (
                ((diagonal_forward == mas).all() and (diagonal_backward == sam).all())
                or (
                    (diagonal_forward == sam).all() and (diagonal_backward == mas).all()
                )
                or (
                    (diagonal_forward == sam).all() and (diagonal_backward == sam).all()
                )
                or (
                    (diagonal_forward == mas).all() and (diagonal_backward == mas).all()
                )
            ):
                output += 1

    return output


def test():
    result = main("test.txt")
    expected = 9
    assert result == expected, f"test failed {result} != {expected}"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)

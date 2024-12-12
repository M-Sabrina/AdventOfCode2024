import numpy as np
from pathlib import Path


def main(input: str):
    datafile = Path("day04") / input
    lines_str = datafile.read_text().splitlines()
    matrix = np.array([list(line) for line in lines_str])
    horizontal_xmas = np.array(["X", "M", "A", "S"])

    output = 0

    (rows, cols) = matrix.shape
    # search vertically
    for col in range(cols):
        for row in range(rows - 3):
            investigate = matrix[row : row + 4, col]
            if (investigate == horizontal_xmas).all() or (
                investigate == np.flip(horizontal_xmas)
            ).all():
                output += 1

    # # search horizontally
    for row in range(rows):
        for col in range(cols - 3):
            investigate = matrix[row, col : col + 4]
            if (investigate == horizontal_xmas).all() or (
                investigate == np.flip(horizontal_xmas)
            ).all():
                output += 1

    # search \ diagonals
    for row in range(rows - 3):
        for col in range(cols - 3):
            investigate = matrix[row : row + 4, col : col + 4]
            diagonal = investigate.diagonal()
            if (diagonal == horizontal_xmas).all() or (
                diagonal == np.flip(horizontal_xmas)
            ).all():
                output += 1

    # search / diagonals
    for row in range(rows - 3):
        for col in range(cols - 3):
            investigate = matrix[row : row + 4, col : col + 4]
            diagonal = np.fliplr(investigate).diagonal()
            if (diagonal == horizontal_xmas).all() or (
                diagonal == np.flip(horizontal_xmas)
            ).all():
                output += 1

    return output


def test():
    result = main("test.txt")
    expected = 18
    assert result == expected, f"test failed {result} != {expected}"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)

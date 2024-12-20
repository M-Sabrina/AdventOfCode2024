from pathlib import Path
import numpy as np


def rotate_right(direction: str):
    if direction == ">":
        return "v"
    elif direction == "<":
        return "^"
    elif direction == "v":
        return "<"
    elif direction == "^":
        return ">"


def main(input: str):
    datafile = Path("day06") / input
    lines = datafile.read_text().splitlines()
    map = np.array([list(line) for line in lines])
    (max_row, max_col) = map.shape
    map_X = np.zeros_like(map, dtype=int)

    while True:
        for symbol in ["<", ">", "^", "v"]:
            if symbol in map:
                (row, col) = np.where(map == symbol)
                direction = symbol

        map_X[row, col] = 1

        if direction == ">":
            new_row = row
            new_col = col + 1
        elif direction == "<":
            new_row = row
            new_col = col - 1
        elif direction == "v":
            new_row = row + 1
            new_col = col
        elif direction == "^":
            new_row = row - 1
            new_col = col

        if new_row < 0 or new_row >= max_row or new_col < 0 or new_col >= max_col:
            break
        elif map[new_row, new_col] == "#":
            direction = rotate_right(direction)
            map[row, col] = direction
            continue
        else:
            map[row, col] = "."
            map[new_row, new_col] = direction
            (row, col) = (new_row, new_col)

    output = np.sum(map_X)
    return output


def test():
    result = main("test.txt")
    expected = 41
    assert result == expected, f"test failed {result} != {expected}"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)

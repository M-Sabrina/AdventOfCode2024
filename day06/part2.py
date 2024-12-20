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


def forbidden(row: int, col: int, map: np.array):
    symbol = map[row, col]
    forbidden_symbols = ["#", "v", "^", ">", "<"]
    if symbol in forbidden_symbols:
        return True
    else:
        return False


def check_for_loops(row: int, col: int, map: np.array):
    (max_row, max_col) = map.shape
    new_map = np.copy(map)
    new_map[row, col] = "#"
    path_map = np.copy(new_map)

    for symbol in ["<", ">", "^", "v"]:
        if symbol in new_map:
            (row, col) = np.where(new_map == symbol)
            direction = symbol

    count = 0
    while True:
        count += 1
        # if count % 10000 == 0:
        #     np.savetxt("path_map.csv", path_map, fmt="%s", delimiter=" ")
        #     np.savetxt("new_map.csv", new_map, fmt="%s", delimiter=" ")

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

        # guard leaves map -> no loop
        if new_row < 0 or new_row >= max_row or new_col < 0 or new_col >= max_col:
            return False
        # guard has walked here before -> loop
        elif path_map[new_row, new_col] == direction:
            return True
        # guard encounters obstacle -> turns right
        elif new_map[new_row, new_col] == "#":
            direction = rotate_right(direction)
            new_map[row, col] = direction
            if path_map[row, col] == direction:
                return True
        # guard walks straight
        else:
            new_map[row, col] = "."
            path_map[row, col] = direction
            new_map[new_row, new_col] = direction
            (row, col) = (new_row, new_col)


def main(input: str):
    datafile = Path("day06") / input
    lines = datafile.read_text().splitlines()
    map = np.array([list(line) for line in lines])
    (max_row, max_col) = map.shape

    output = 0
    for row in range(max_row):
        for col in range(max_col):
            # if not (row == 6 and col == 36):
            #     continue
            if not forbidden(row, col, map):
                print(f"{row=} {col=}")
                contains_loop = check_for_loops(row, col, map)
                if contains_loop:
                    output += 1

    return output


def test():
    result = main("test.txt")
    expected = 6
    assert result == expected, f"test failed {result} != {expected}"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)

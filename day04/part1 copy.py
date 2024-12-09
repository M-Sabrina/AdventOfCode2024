import numpy as np
from pathlib import Path


def get_diagonal(array, r, c, direction):
    """
    Get the first 4 values along a diagonal starting at (r, c) in the given direction.

    Parameters:
    - array: 2D numpy array
    - r, c: starting row and column indices
    - direction: one of "top-right", "top-left", "bottom-right", "bottom-left"

    Returns:
    - List of 4 diagonal values
    """
    # Directions mapping
    direction_map = {
        "top-right": (1, 1),  # row+1, col+1
        "top-left": (1, -1),  # row+1, col-1
        "bottom-right": (-1, 1),  # row-1, col+1
        "bottom-left": (-1, -1),  # row-1, col-1
    }

    if direction not in direction_map:
        raise ValueError(
            "Invalid direction. Choose from 'top-right', 'top-left', 'bottom-right', 'bottom-left'."
        )

    # Get the row and column increment values based on direction
    row_inc, col_inc = direction_map[direction]

    # Check if there is enough space to get 4 elements
    values = []
    for i in range(4):
        new_r = r + i * row_inc
        new_c = c + i * col_inc
        # Ensure the new indices are within bounds
        if 0 <= new_r < array.shape[0] and 0 <= new_c < array.shape[1]:
            values.append(array[new_r, new_c])
        else:
            raise IndexError(
                "Starting index is too close to the boundary for 4 elements in the given direction."
            )

    return np.array(values)


def check_surroundings(lines: np.array, o_r: int, o_c: int):
    columns = lines.shape[1]
    rows = lines.shape[0]
    right = lines[o_r, o_c : min(o_c + 4, columns)]
    left = lines[o_r, o_c : max(o_c - 4, 0) : -1]
    bottom = lines[o_r : min(o_r + 4, rows), o_c]
    top = lines[o_r : max(o_r - 4, 0) : -1, o_c]

    top_right = get_diagonal(lines, o_r, o_c, "top-right")
    top_left = get_diagonal(lines, o_r, o_c, "top-left")
    bottom_right = get_diagonal(lines, o_r, o_c, "bottom-right")
    bottom_left = get_diagonal(lines, o_r, o_c, "bottom_left")

    right.join("")


def main(input: str):
    datafile = Path("day04") / input
    lines_str = datafile.read_text().splitlines()
    lines = np.array([list(line) for line in lines_str])
    x_r_all, x_c_all = np.where(lines == "X")
    for x_r, x_c in zip(x_r_all, x_c_all):
        (m_r_all, m_c_all) = check_surroundings(lines, x_r, x_c)
        print(m_r_all)
    output = 0
    return output


def test():
    assert main("test.txt") == 18, "test failed"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)

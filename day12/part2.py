import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    import numpy as np
    from numpy.typing import NDArray
    return NDArray, Path, np


@app.cell
def _(NDArray, char):
    def check_plot(row: int, col: int, plant: char, garden: NDArray, visited: set):
        perimeter = 0
        max_row, max_col = garden.shape

        # check left
        if (col - 1 >= 0) and (garden[row, col - 1] != plant) or (col - 1 == -1):
            # check up & down
            action = "left"
            if not (
                (row - 1, col, action) in visited
                or (row + 1, col, action) in visited
            ):
                perimeter += 1
            visited.add((row, col, action))
            # print(f"left: {row=} {col=}")

        # check right
        if (
            (col + 1 < max_col)
            and (garden[row, col + 1] != plant)
            or (col + 1 == max_col)
        ):
            # check up & down
            action = "right"
            if not (
                (row - 1, col, action) in visited
                or (row + 1, col, action) in visited
            ):
                perimeter += 1
            visited.add((row, col, action))
            # print(f"right: {row=} {col=}")

        # check top
        if (row - 1 >= 0) and (garden[row - 1, col] != plant) or (row - 1 == -1):
            # right & left
            action = "top"
            if not (
                (row, col - 1, action) in visited
                or (row, col + 1, action) in visited
            ):
                perimeter += 1
            visited.add((row, col, action))
            # print(f"top: {row=} {col=}")

        # check below
        if (
            (row + 1 < max_row)
            and (garden[row + 1, col] != plant)
            or (row + 1 == max_row)
        ):
            # right & left
            action = "below"
            if not (
                (row, col - 1, action) in visited
                or (row, col + 1, action) in visited
            ):
                perimeter += 1
            visited.add((row, col, action))
            # print(f"below: {row=} {col=}")

        return perimeter
    return (check_plot,)


@app.cell
def _(NDArray, char):
    def flood_fill(
        array: NDArray,
        row,
        col,
        visited: set,
        value: char,
        region_label: int,
        regions: NDArray,
    ):
        stack = [(row, col)]

        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            regions[cx, cy] = region_label

            # Check all 4 directions (up, down, left, right)
            for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
                if 0 <= nx < array.shape[0] and 0 <= ny < array.shape[1]:
                    if array[nx, ny] == value and (nx, ny) not in visited:
                        stack.append((nx, ny))
    return (flood_fill,)


@app.cell
def _(NDArray, flood_fill, np):
    def find_connected_regions(array: NDArray):
        visited = set()
        regions = np.zeros_like(array, dtype=int)
        region_label = 0

        for row in range(array.shape[0]):
            for col in range(array.shape[1]):
                if (row, col) not in visited:
                    value = array[row, col]
                    flood_fill(
                        array, row, col, visited, value, region_label, regions
                    )
                    region_label += 1

        return regions
    return (find_connected_regions,)


@app.cell
def _(Path, check_plot, find_connected_regions, np):
    def main(input: str):
        datafile = Path("day12") / input
        rows = datafile.read_text().splitlines()
        garden = np.array([list(row) for row in rows])
        plants = np.unique(garden)

        regions = np.zeros_like(garden, dtype=int)
        # step 1: identify regions
        regions = find_connected_regions(garden)
        # print(regions)

        # step 2: calculate prices of regions
        price = 0
        for region in range(np.max(regions) + 1):
            visited = set()
            rows, cols = np.where(regions == region)
            area = 0
            perimeter = 0
            plant = garden[rows[0], cols[0]]
            for row, col in zip(rows, cols):
                area += 1
                perimeter += check_plot(row, col, plant, garden, visited)
            region_price = area * perimeter
            # print(f"A region of {plant} plants with price {area} * {perimeter} = {region_price}")
            price += region_price
        return price
    return (main,)


@app.cell
def _(main):
    test_result = main("test.txt")
    expected = 1206
    if test_result != expected:
        print(f"test failed {test_result} != {expected}")
    else:
        print(main("input.txt"))
    return expected, test_result


if __name__ == "__main__":
    app.run()

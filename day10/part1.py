import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    import numpy as np
    from numpy.typing import NDArray
    return NDArray, Path, np


@app.cell
def _(NDArray, np):
    def hike(row: int, col: int, map: NDArray, map_score: NDArray):
        max_row, max_col = np.shape(map)
        if map[row, col] == 9:
            # print(f"Trailhead at: {row} {col}")
            map_score[row, col] += 1
        else:
            for scan_row, scan_col in [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ]:
                # print(f"{row=}, {col=}")
                if not (
                    scan_row < 0
                    or scan_row >= max_row
                    or scan_col < 0
                    or scan_col >= max_col
                ):
                    if map[scan_row, scan_col] == (map[row, col] + 1):
                        # print(f"Next step: {scan_row} {scan_col}")
                        hike(scan_row, scan_col, map, map_score)
    return (hike,)


@app.cell
def _(Path, hike, np):
    def main(input: str):
        datafile = Path("day10") / input
        lines = datafile.read_text().splitlines()
        map = np.array([list(line) for line in lines]).astype(int)
        start_y, start_x = np.where(map == 0)
        score = 0
        map_score = np.array([])
        for y0, x0 in zip(start_y, start_x):
            # print(f"Start at: {y0} {x0}")
            map_score = np.zeros_like(map, dtype=int)
            hike(y0, x0, map, map_score)
            map_score[np.where(map_score > 0)] = 1
            score += np.sum(map_score)
        # print(map_score)
        return score
    return (main,)


@app.cell
def _(main):
    result = main("test.txt")
    expected = 36
    if result != expected:
        print(f"test failed {result} != {expected}")
    else:
        print(main("input.txt"))
    return expected, result


if __name__ == "__main__":
    app.run()

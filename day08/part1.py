import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    import numpy as np
    from itertools import combinations
    return Path, combinations, np


@app.cell
def _(combinations):
    def generate_combinations(arr):
        comb_list = []
        for r in range(2, len(arr) + 1):
            comb_list.extend(combinations(arr, r))
        return comb_list
    return (generate_combinations,)


@app.cell
def _(Path, generate_combinations, np):
    def main(input: str):
        datafile = Path("day08") / input
        lines = datafile.read_text().splitlines()
        map = np.array([list(line) for line in lines])
        (max_y, max_x) = map.shape

        map_antinodes = np.zeros(map.shape)

        frequencies = np.unique_values(map)
        dots_index = np.where(frequencies != ".")
        frequencies = frequencies[dots_index]

        for frequency in frequencies:
            (y, x) = np.where(map == frequency)
            antennas = np.arange(len(x))
            combinations = generate_combinations(antennas)
            for combination in combinations:
                if len(combination) != 2:
                    continue

                (x_1, x_2) = (
                    x[combination[0]],
                    x[combination[1]],
                )
                (y_1, y_2) = (
                    y[combination[0]],
                    y[combination[1]],
                )

                delta_x = x_2 - x_1
                delta_y = y_2 - y_1

                node_1_x = x_1 - delta_x
                node_1_y = y_1 - delta_y
                if (
                    node_1_x >= 0
                    and node_1_x < max_x
                    and node_1_y >= 0
                    and node_1_y < max_y
                ):
                    map_antinodes[node_1_y, node_1_x] = 1

                node_2_x = x_2 + delta_x
                node_2_y = y_2 + delta_y
                if (
                    node_2_x >= 0
                    and node_2_x < max_x
                    and node_2_y >= 0
                    and node_2_y < max_y
                ):
                    map_antinodes[node_2_y, node_2_x] = 1

        return np.count_nonzero(map_antinodes == 1)
    return (main,)


@app.cell
def _(main):
    result = main("test.txt")
    expected = 14
    if result != expected:
        print(f"test failed {result} != {expected}")
    else:
        print(main("input.txt"))
    return expected, result


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

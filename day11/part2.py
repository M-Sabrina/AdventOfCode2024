import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    import numpy as np
    return Path, np


@app.cell
def _():
    def split_integer(val: int, digits: int):
        half_length = digits // 2
        divisor = 10**half_length
        val1 = val // divisor
        val2 = val % divisor
        return val1, val2
    return (split_integer,)


@app.cell
def _():
    def blink(
        stone: int, count: int, collection: dict[tuple[int, int], int]
    ) -> int:
        if (stone, count) in collection:
            return collection[(stone, count)]
        elif count == 0:
            return 1
        digits = len(str(stone))
        if stone == 0:
            return blink(1, count - 1, collection)
        elif digits % 2 == 0:
            left = int(str(stone)[0 : digits // 2])
            right = int(str(stone)[digits // 2 : digits])
            return blink(left, count - 1, collection) + blink(
                right, count - 1, collection
            )
        else:
            new_stone = stone * 2024
            value = blink(new_stone, count - 1, collection)
            collection[(stone, count)] = value
            return value
    return (blink,)


@app.cell
def _(Path, blink):
    def main(input: str, count: int):
        datafile = Path("day11") / input
        stones = list(map(int, datafile.read_text().strip().split(" ")))
        output = 0
        collection = {}
        for stone in stones:
            output += blink(stone, count, collection)
        return output
    return (main,)


@app.cell
def _(main):
    test_result = main("test.txt", 25)
    expected = 55312
    if test_result != expected:
        print(f"test failed {test_result} != {expected}")
    else:
        print(main("input.txt", 75))
    return expected, test_result


if __name__ == "__main__":
    app.run()

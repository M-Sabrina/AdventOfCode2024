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
def _(np, split_integer):
    def blink(stones: list[int]):
        ind = 0
        while ind < len(stones):
            val = stones[ind]
            if val == 0:
                stones[ind] = 1
                ind += 1
                continue
            digits = int(np.log10(val)) + 1
            if digits % 2 == 0:
                val1, val2 = split_integer(val, digits)
                stones[ind] = val1
                stones.insert(ind + 1, val2)
                ind += 2
            else:
                stones[ind] = val * 2024
                ind += 1
            # print(stones)
    return (blink,)


@app.cell
def _(Path, blink):
    def main(input: str, count: int):
        datafile = Path("day11") / input
        stones = list(map(int, datafile.read_text().strip().split(" ")))
        print(stones)
        for n in range(count):
            blink(stones)
        return len(stones)
    return (main,)


@app.cell
def _(main):
    test_result = main("test.txt", 25)
    expected = 55312
    if test_result != expected:
        print(f"test failed {test_result} != {expected}")
    else:
        print(main("input.txt", 25))
    return expected, test_result


if __name__ == "__main__":
    app.run()

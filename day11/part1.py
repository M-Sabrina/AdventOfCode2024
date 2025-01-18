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
    def blink(stones: list[int]):
        ind = 0
        while ind < len(stones):
            val = stones[ind]
            digits = len(str(val))
            if val == 0:
                stones[ind] = 1
                ind += 1
            elif digits % 2 == 0:
                val1 = int(str(val)[0 : digits // 2])
                val2 = int(str(val)[digits // 2 : digits])
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
    def main(input: str):
        datafile = Path("day11") / input
        stones = list(map(int, datafile.read_text().strip().split(" ")))
        # print(stones)
        for n in range(25):
            blink(stones)
        return len(stones)
    return (main,)


@app.cell
def _(main):
    result = main("test.txt")
    expected = 55312
    if result != expected:
        print(f"test failed {result} != {expected}")
    else:
        print(main("input.txt"))
    return expected, result


if __name__ == "__main__":
    app.run()

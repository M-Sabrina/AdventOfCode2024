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
def _(np):
    def blink(stones: list[int], count: int):
        # key: number, entry: (result1, result2, index_increment)
        collection = dict([(0, (1, np.nan, 1)), (1, (2024, np.nan, 1))])
        for c in range(count):
            # print(c)
            ind = 0
            while ind < len(stones):
                val = stones[ind]
                digits = len(str(val))
                if val in collection:
                    (val1, val2, index_increment) = collection[val]
                    if np.isnan(val2):
                        stones[ind] = val1
                    else:
                        stones[ind] = val1
                        stones.insert(ind + 1, val2)
                    ind += index_increment
                else:
                    if digits % 2 == 0:
                        val1 = int(str(val)[0 : digits // 2])
                        val2 = int(str(val)[digits // 2 : digits])
                        stones[ind] = val1
                        stones.insert(ind + 1, val2)
                        ind += 2
                        collection[val] = (val1, val2, 2)
                    else:
                        new_val = val * 2024
                        collection[val] = (new_val, np.nan, 1)
                        stones[ind] = new_val
                        ind += 1
        # print(stones)
        return len(stones)
    return (blink,)


@app.cell
def _(Path, blink):
    def main(input: str, count: int):
        datafile = Path("day11") / input
        stones = list(map(int, datafile.read_text().strip().split(" ")))
        # print(stones)
        return blink(stones, count)
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

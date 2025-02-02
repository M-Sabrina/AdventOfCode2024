import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    import numpy as np
    return Path, np


@app.cell
def _(Path, np):
    def main(input: str, xmax: int, ymax: int):
        datafile = Path("day14") / input
        lines = datafile.read_text().splitlines()
        map = np.zeros((xmax, ymax))
        for line in lines:
            x = int(line.split(",")[0].split("p=")[1])
            y = int(line.split(",")[1].split(" ")[0])
            vx = int(line.split("v=")[1].split(",")[0])
            vy = int(line.split(",")[2])
            # print(f"{x=} {y=} {vx=} {vy=}")
            for ind in range(100):
                x = np.mod(x + vx, xmax)
                y = np.mod(y + vy, ymax)
            map[x, y] += 1
        map_t = np.transpose(map)
        q1 = map[0 : int(xmax // 2), 0 : int(ymax // 2)]
        q2 = map[int(xmax // 2) + 1 : xmax, 0 : int(ymax // 2)]
        q3 = map[0 : int(xmax // 2), int(ymax // 2) + 1 : ymax]
        q4 = map[int(xmax // 2) + 1 : xmax, int(ymax // 2) + 1 : ymax]
        return int(np.sum(q1) * np.sum(q2) * np.sum(q3) * np.sum(q4))
    return (main,)


@app.cell
def _(main):
    test_result = main("test.txt", 11, 7)
    expected = 12
    if test_result != expected:
        print(f"test failed {test_result} != {expected}")
    else:
        print(main("input.txt", 101, 103))
    return expected, test_result


if __name__ == "__main__":
    app.run()

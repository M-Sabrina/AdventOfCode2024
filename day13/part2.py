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
    def main(input: str):
        datafile = Path("day13") / input
        configs = datafile.read_text().split(f"\n\n")

        minimal_cost = np.zeros(len(configs))

        for idx, config in enumerate(configs):
            lines = config.splitlines()
            #
            line_A = lines[0]
            X_A = int(line_A.split("X+")[1].split(",")[0])
            Y_A = int(line_A.split("Y+")[1])
            #
            line_B = lines[1]
            X_B = int(line_B.split("X+")[1].split(",")[0])
            Y_B = int(line_B.split("Y+")[1])
            #
            line_price = lines[2]
            X_price = int(line_price.split("X=")[1].split(",")[0]) + 10000000000000
            Y_price = int(line_price.split("Y=")[1]) + 10000000000000
            #
            B = (Y_price - X_price * Y_A / X_A) / (Y_B - X_B * Y_A / X_A)
            A = (X_price - B * X_B) / X_A
            #
            A = round(A, 3)
            B = round(B, 3)
            #
            # print(f"{idx=} {A=} {B=}")
            if A.is_integer() and B.is_integer() and A >= 0 and B >= 0:
                minimal_cost[idx] = A * 3 + B

        return int(np.sum(minimal_cost))
    return (main,)


@app.cell
def _(main):
    print(main("input.txt"))
    return


if __name__ == "__main__":
    app.run()

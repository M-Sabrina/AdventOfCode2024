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
            X_price = int(line_price.split("X=")[1].split(",")[0])
            Y_price = int(line_price.split("Y=")[1])
            #
            # print(f"{X_A=} {Y_A=} {X_B=} {Y_B=} {X_price=} {Y_price=}")
            #
            # winning_A = []
            # winning_B = []
            costs_win = []
            can_win = False
            for push_button_A in range(101):
                for push_button_B in range(101):
                    X = push_button_A * X_A + push_button_B * X_B
                    Y = push_button_A * Y_A + push_button_B * Y_B
                    if (X, Y) == (X_price, Y_price):
                        can_win = True
                        cost = 3 * push_button_A + push_button_B
                        # winning_A.append(push_button_A)
                        # winning_B.append(push_button_B)
                        costs_win.append(cost)
            if can_win:
                cheapest = costs_win.index(min(costs_win))
                minimal_cost[idx] = costs_win[cheapest]

        return int(np.sum(minimal_cost))
    return (main,)


@app.cell
def _(main):
    test_result = main("test.txt")
    expected = 480
    if test_result != expected:
        print(f"test failed {test_result} != {expected}")
    else:
        print(main("input.txt"))
    return expected, test_result


if __name__ == "__main__":
    app.run()

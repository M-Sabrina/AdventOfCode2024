import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    import numpy as np

    return Path, np


@app.cell
def _():
    # thank you: https://stackoverflow.com/questions/34559663/convert-decimal-to-ternarybase3-in-python
    def ternary(n):
        if n == 0:
            return "0"
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
        return "".join(reversed(nums))

    return (ternary,)


@app.cell
def _(Path, np, ternary):
    def main(input: str):
        datafile = Path("day07") / input
        lines = datafile.read_text().splitlines()
        output = 0
        for line in lines:
            (result_str, numbers_str) = line.split(": ")
            result = int(result_str)
            numbers_str = numbers_str.split(" ")
            numbers = np.array([int(number) for number in numbers_str])

            num_operators = np.size(numbers) - 1  # total number of operators
            max_comb = 3**num_operators - 1  # start with '0000' -> max is '2222'

            comb = 0
            while comb <= max_comb:
                result_test = numbers[0]
                # get ternary number for operator assignment (0 -> +, 1 -> *, 2 -> ||)
                ternary_nopadding = ternary(comb)
                operators = list(
                    ternary_nopadding.zfill(num_operators)
                )  # Pad with leading zeros
                for ind, operator in enumerate(operators):
                    if operator == "0":
                        result_test += numbers[ind + 1]
                    elif operator == "1":
                        result_test *= numbers[ind + 1]
                    else:
                        left_side = str(result_test)
                        right_side = str(numbers[ind + 1])
                        result_test = int(left_side + right_side)
                if result_test == result:
                    output += result
                    break
                else:
                    comb += 1

        return output

    return (main,)


@app.cell
def _(main):
    result = main("test.txt")
    expected = 11387
    if result != expected:
        print(f"test failed {result} != {expected}")
    return expected, result


@app.cell
def _(main):
    main("input.txt")
    return


if __name__ == "__main__":
    app.run()

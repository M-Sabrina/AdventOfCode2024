import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    return (Path,)


@app.cell
def _(Path, blink):
    def main(input: str):
        datafile = Path("day12") / input
        map = list(map(int, datafile.read_text().strip().split(" ")))

        return 0
    return (main,)


@app.cell
def _(main):
    test_result = main("test.txt")
    expected = 55312
    if test_result != expected:
        print(f"test failed {test_result} != {expected}")
    else:
        print(main("input.txt"))
    return expected, test_result


if __name__ == "__main__":
    app.run()

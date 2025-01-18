import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import matplotlib.pyplot as plt
    import marimo as mo
    import numpy as np
    return mo, np, plt


@app.cell
def _(mo):
    slider = mo.ui.slider(start=1, stop=100, step=1)
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(f"Current value of {slider.value=}")
    return


@app.cell
def _(slider):
    slider
    return


@app.cell
def _(np, slider):
    x = np.linspace(0, 2*np.pi * slider.value, 10000)
    y = np.sin(x)
    return x, y


@app.cell
def _(plt, x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    return ax, fig


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

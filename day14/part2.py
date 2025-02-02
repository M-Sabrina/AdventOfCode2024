import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    import numpy as np
    from numpy import count_nonzero
    import matplotlib.pyplot as plt
    return Path, count_nonzero, np, plt


@app.cell
def _(Path, np, plt):
    def main(input: str, xmax: int, ymax: int):
        save_dir = Path("./day14/maps_part2")
        save_dir.mkdir(exist_ok=True)

        datafile = Path("day14") / input
        lines = datafile.read_text().splitlines()
        num_robots = len(lines)
        robots = np.zeros((num_robots, 4))
        for ind, line in enumerate(lines):
            x = int(line.split(",")[0].split("p=")[1])
            y = int(line.split(",")[1].split(" ")[0])
            vx = int(line.split("v=")[1].split(",")[0])
            vy = int(line.split(",")[2])
            robots[ind, 0] = x
            robots[ind, 1] = y
            robots[ind, 2] = vx
            robots[ind, 3] = vy
        for iteration in range(10000):
            map = np.zeros((xmax, ymax), dtype=int)
            for ind in range(num_robots):
                x = robots[ind, 0]
                y = robots[ind, 1]
                vx = robots[ind, 2]
                vy = robots[ind, 3]
                x = int(np.mod(x + vx, xmax))
                y = int(np.mod(y + vy, ymax))
                robots[ind, 0] = x
                robots[ind, 1] = y
                map[x, y] += 1
            map_t = np.transpose(map)
            plt.imsave(save_dir / f"map_{iteration + 1}.png", map_t)
        return 0
        # Check folder "maps_part2" and search for smallest png image!
        # small as in least disk space
    return (main,)


@app.cell
def _(main):
    main("input.txt", 101, 103)
    return


if __name__ == "__main__":
    app.run()

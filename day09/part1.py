import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    import numpy as np
    return Path, np


@app.cell
def _(memory_map, memory_map_ind, np):
    def convert_map(disk_map: np.array):
        memory = np.zeros(np.sum(disk_map))
        memory_ind = 0
        id_number = 0
        for ind, digit in enumerate(disk_map):
            if np.mod(ind, 2) == 0:
                for d in range(digit):
                    memory[memory_ind] = id_number
                    memory_ind += 1
                id_number += 1
            else:
                for d in range(digit):
                    memory_map[memory_map_ind] = np.nan
                    memory_map_ind += 1
        return memory
    return (convert_map,)


@app.cell
def _(np):
    def defragment(memory: np.array):
        sorted = False
        for ind, element in enumerate(memory):
            if np.isnan(element):
                # find index of highest not nan element
                for highest_ind, highest_element in enumerate(memory[::-1]):
                    if not np.isnan(highest_element):
                        break
                corr_highest_ind = len(memory) - 1 - highest_ind
                # break loop if sorting is complete
                if corr_highest_ind < ind:
                    sorted = True
                # swap memory location of highest_element to index
                else:
                    memory[ind] = highest_element
                    memory[corr_highest_ind] = np.nan
            if sorted:
                return memory
    return (defragment,)


@app.cell
def _(np):
    def checksum(memory: np.array):
        checksum = 0
        for ind, element in enumerate(memory):
            if np.isnan(element):
                break
            checksum += ind * element
        return checksum
    return (checksum,)


@app.cell
def _(Path, checksum, convert_map, defragment, np):
    def main(input: str):
        datafile = Path("day09") / input
        disk_map = np.array([int(s) for s in datafile.read_text().strip()])
        memory = convert_map(disk_map)
        # print(memory)
        compact_memory = defragment(memory)
        # print(compact_memory)
        return checksum(compact_memory)
    return (main,)


@app.cell
def _(main):
    result = main("test.txt")
    expected = 1928
    if result != expected:
        print(f"test failed {result} != {expected}")
    else:
        print(main("input.txt"))
    return expected, result


if __name__ == "__main__":
    app.run()

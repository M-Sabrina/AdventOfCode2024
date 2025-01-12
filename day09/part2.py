import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    import numpy as np
    from numpy.typing import NDArray
    return NDArray, Path, np


@app.cell
def _(NDArray, np):
    def convert_map(disk_map: NDArray[int]):
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
                    memory[memory_ind] = np.nan
                    memory_ind += 1
        return memory
    return (convert_map,)


@app.cell
def _(NDArray, np):
    def fragment(memory: NDArray[int]):
        for file_ID in range(int(np.nanmax(memory)), -1, -1):
            block_size = np.count_nonzero(memory == file_ID)
            file_ID_start_ind = np.where(memory == file_ID)[0][0]
            # find free space that can fit current block
            found_block = False
            ind = 0
            while not found_block and ind < len(memory):
                if np.isnan(memory[ind]):
                    if ind > file_ID_start_ind:
                        break
                    # get size of free block
                    free_size = 0
                    while ind + free_size < len(memory) and np.isnan(
                        memory[ind + free_size]
                    ):
                        free_size += 1
                    if free_size >= block_size:
                        found_block = True
                        break
                    else:
                        ind += free_size
                else:
                    ind += 1
            if found_block:
                file_ID_ind = np.where(memory == file_ID)
                memory[file_ID_ind] = np.repeat(np.nan, block_size)
                memory[ind : ind + block_size] = np.repeat(file_ID, block_size)
        return memory
    return (fragment,)


@app.cell
def _(NDArray, np):
    def checksum(memory: NDArray[int]):
        checksum = 0
        for ind, element in enumerate(memory):
            if np.isnan(element):
                continue
            checksum += ind * element
        return checksum
    return (checksum,)


@app.cell
def _(Path, checksum, convert_map, fragment, np):
    def main(input: str):
        datafile = Path("day09") / input
        disk_map = np.array([int(s) for s in datafile.read_text().strip()])
        memory = convert_map(disk_map)
        # print(memory)
        compact_memory = fragment(memory)
        # print(compact_memory)
        return checksum(compact_memory)
    return (main,)


@app.cell
def _(main):
    result = main("test.txt")
    expected = 2858
    if result != expected:
        print(f"test failed {result} != {expected}")
    else:
        print(main("input.txt"))
    return expected, result


if __name__ == "__main__":
    app.run()

import utils
import numpy as np

AXES=(0, 1)
TOP_LEFT=(-1, -1)
LEFT=(0, -1)
BOTTOM_LEFT=(1, -1)
BOTTOM=(1, 0)
BOTTOM_RIGHT=(1, 1)
RIGHT=(0, 1)
TOP_RIGHT=(-1, 1)
TOP=(-1, 0)

def flash(arr):
    return (np.roll(arr, TOP_LEFT, AXES) + np.roll(arr, LEFT, AXES) + np.roll(arr, BOTTOM_LEFT, AXES)
            + np.roll(arr, BOTTOM, AXES) + np.roll(arr, BOTTOM_RIGHT, AXES) + np.roll(arr, RIGHT, AXES)
            + np.roll(arr, TOP_RIGHT, AXES) + np.roll(arr, TOP, AXES))

def step(arr: np.ndarray):
    result = np.pad(arr, 1, 'constant', constant_values=0) # pad the input array
    result[1:-1, 1:-1] += 1  # add 1 to everything in the array
    flashed = np.zeros_like(result, dtype=np.bool8) # bool array to hold indices that have flashed
    while True: # loop to flash
        result[flashed] = 0 # set flashed to 0, as it is a requirement
        rg9 = (result > 9) # find values greater than 9 that will flash
        flashed = flashed | rg9 
        flashes = (rg9 + 0) # coerce into ints
        if flashes.sum() == 0: # if no new values exist that will flash in this step, break
            break
        new_flashes = flash(flashes)
        result[1:-1, 1:-1] += new_flashes[1:-1, 1:-1]

    return (result[1:-1, 1:-1], flashed[1:-1, 1:-1].sum())

def part1and2(arr: np.ndarray, steps: int) -> tuple[int, int]:
    current = arr
    total_flashes: int = 0
    i = 0
    while True:
        i += 1
        n, f = step(current)
        current = n
        if i <= steps:
            total_flashes += f
        if f == arr.size:
            break
    return (total_flashes, i)


data = np.array([list(map(int, x)) for x in utils.get_input('d11').strip().splitlines()])
p1, p2 = part1and2(data, 100)
print(f"part 1: {p1}")
print(f"part 2: {p2}")
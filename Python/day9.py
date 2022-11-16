import utils
import numpy as np

def local_minima(array2d: np.ndarray):
    padded = np.pad(array2d, 1, mode='constant', constant_values=9) # pad the edges with 9s
    res = ((padded < np.roll(padded,  1, 0)) &
            (padded < np.roll(padded, -1, 0)) &
            (padded < np.roll(padded,  1, 1)) &
            (padded < np.roll(padded, -1, 1)))
    
    return res[1:-1, 1:-1]

def check(arr, r, c) -> int:
    if arr[r,c]:
        arr[r,c]=False
        return 1 + check(arr, r, max(c-1, 0)) + check(arr, r, min(c+1, arr.shape[1]-1)) + check(arr, max(r-1, 0), c) + check(arr, min(r+1, arr.shape[0]-1), c)
    return 0

def part2(array2d: np.ndarray, locations: np.ndarray):
    res=array2d<9 # gets all the basinerinos
    bsums = [] # basin sums
    for l in locations:
        bsums.append(check(res, l[0], l[1]))
    bsums.sort(reverse=True)
    return bsums[0] * bsums[1] * bsums[2]

data = np.array([list(map(int, x)) for x in utils.get_input('d9').splitlines()], dtype=np.uint8)
minima = local_minima(data)

print(f"part 1: {(data[minima]+1).sum()}")
print(f"part 2: {part2(data, np.column_stack(np.where(minima)))}")
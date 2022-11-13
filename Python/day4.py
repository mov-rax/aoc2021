import utils
import numpy as np
import itertools as it
import re
class Grid:

    def __init__(self, rawdata: np.ndarray) -> None:
        self.raw = np.array(rawdata, dtype=complex)
        self.numdict: dict[int, tuple[int, int]] = {}
        dims = self.raw.shape
        for r in range(dims[0]):
            for c in range(dims[1]):
                self.numdict[rawdata[r,c]] = [r,c]

    def mark(self, num: int) -> None:
        if num in self.numdict:
            location = self.numdict[num]
            self.raw[location[0], location[1]] += (0 + 1j)

    def mark_and_check(self, num: int) -> bool:
        self.mark(num)
        b = self.has_bingo()
        print(b)
        return self.has_bingo()

    def has_bingo(self) -> bool:
        shape = self.raw.shape
        cols = self.raw.sum(axis=0)
        rows = self.raw.sum(axis=1)
        for c in cols:
            if c.imag == shape[0]:
                return True
        for r in rows:
            if r.imag == shape[1]:
                return True
        return False

    def clone(self):
        return type(self)(self.raw.copy())


    def calc_score(self) -> int:
        filtered = map(lambda r: list(filter(lambda v: v.imag == 0, r)), self.raw)
        return int(sum(it.chain.from_iterable(filtered)).real)     

    def __str__(self) -> str:
        return f"{self.raw}"
    

def process(data: str):
    parts = data.strip().split('\n\n')
    nums = parts[0]
    rawgrids = parts[1::]
    strgrids = [grid.splitlines() for grid in rawgrids]
    numgrids = map(lambda x: list(map(lambda y: list(map(int, re.split("[ ]+", y.strip()))), x)), strgrids)
    return (np.array([int(x) for x in nums.split(',')]), np.array(list(numgrids)))

def part1(data: str):
    nums, rawgrids = process(data)
    grids = list(map(Grid, rawgrids))
    for num in nums:
        for grid in grids:
            grid.mark(num)
            if grid.has_bingo():
                return grid.calc_score() * num

def part2(data: str):
    nums, rawgrids = process(data)
    grids = [Grid(x) for x in rawgrids]
    for n in nums:
        temp = []
        for g in grids:
            g.mark(n)
            if not g.has_bingo():
                temp.append(g)
            if len(grids) == 1 and g.has_bingo():
                return g.calc_score() * n
        grids = temp
            
    return -1

data = utils.get_input('d4')

print(f"part 1: {part1(data)}")
print(f"part 2: {part2(data)}")

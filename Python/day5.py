from __future__ import annotations
import utils
import numpy as np

class Coord(object):

    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.x1 = x1
        self.y1 = y1 
        self.x2 = x2 
        self.y2 = y2 
    
    def from_str(s: str) -> Coord:
        splitted = s.split(' -> ')
        left = list(map(int, splitted[0].split(',')))
        right = list(map(int, splitted[1].split(',')))
        return Coord(left[0], left[1], right[0], right[1])

def part1(coords: list[Coord]) -> int:
    mat = np.zeros((1000, 1000), dtype=np.uint8)
    for coord in coords:
        if (coord.x1 == coord.x2) or (coord.y1 == coord.y2):
            x1, x2 = (coord.x1, coord.x2) if coord.x2 >= coord.x1 else (coord.x2, coord.x1)
            y1, y2 = (coord.y1, coord.y2) if coord.y2 >= coord.y1 else (coord.y2, coord.y1)
            mat[y1:(y2+1), x1:(x2+1)] += 1
    
    f = lambda x: x > 1
    return len(mat[f(mat)]) # get the number of vals > 1 using boolean masking

def part2(coords: list[Coord]) -> int:
    mat = np.zeros((1000, 1000), dtype=np.uint8)
    for coord in coords:
        if (coord.x1 == coord.x2) or (coord.y1 == coord.y2):
            x1, x2 = (coord.x1, coord.x2) if coord.x2 >= coord.x1 else (coord.x2, coord.x1)
            y1, y2 = (coord.y1, coord.y2) if coord.y2 >= coord.y1 else (coord.y2, coord.y1)
            mat[y1:(y2+1), x1:(x2+1)] += 1 # horizontal/vertical lines
        else:   # diagonal lines
            xd = 1 if (coord.x2 - coord.x1) > 0 else -1
            yd = 1 if (coord.y2 - coord.y1) > 0 else -1
            x, y = coord.x1, coord.y1
            while (x != coord.x2) and (y != coord.y2):
                mat[y, x] += 1
                y += yd
                x += xd
            mat[y, x] += 1
    
    f = lambda x: x > 1
    return len(mat[f(mat)])
    
data = utils.get_input('d5').strip().splitlines()
coords = list(map(Coord.from_str, data))
print(f"part 1: {part1(coords)}")
print(f"part 2: {part2(coords)}")
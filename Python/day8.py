import utils 
import functools as ft

lendict = {
    2 : [1],
    3 : [7],
    4 : [4],
    5 : [2, 3, 5],
    6 : [0, 6, 9],
    7 : [8]
}

def toseg(s:str) -> int:
    return ft.reduce(lambda a,v: a | (1 << ord(v) - ord('a')), s, 0)

def calc(one: int, four: int, input: list[int]) -> int:
    num = 0
    for s in input:
        l = s.bit_count()
        if l == 5: # can be 2, 3, or 5
            if (one & s) == one:  # Segment(1) & Segment(3) == Segment(1)
                num = num * 10 + 3
            elif (four & s).bit_count() == 3: # Segment(5) & Segment(4) results in 3 set bits.
                num = num * 10 + 5
            else: #else Segment(2)
                num = num * 10 + 2
        elif l == 6: # can be 0, 6, or 9
            if (four | s == s): # Segment(9) | Segment(4) == Segment(9)
                num = num * 10 + 9
            elif (one | s == s): # Segment(0) | Segment(1) == Segment(0) 
                num = num * 10
            else: # else Segment(6)
                num = num * 10 + 6
        else:
            num = num * 10 + lendict[l][0]
    return num

def part1(data):
    acc = 0
    for line in data:
        for output in line[1]:
            l = lendict[output.bit_count()][0]
            if l == 1 or l == 4 or l == 7 or l == 8:
                acc += 1
    return acc

def part2(data):
    acc = 0
    for line in data:
        one, four = 0, 0
        for input in line[0]:
            l = lendict[input.bit_count()][0]
            if l == 1:
                one = input
            elif l == 4:
                four = input
        acc += calc(one, four, line[1])
    return acc

data = [[list(map(toseg, side.split(' '))) for side in l.split(' | ')] for l in utils.get_input('d8').splitlines()]
print(f"part 1: {part1(data)}")
print(f"part 2: {part2(data)}")
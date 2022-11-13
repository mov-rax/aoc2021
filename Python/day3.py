import utils
import functools

def gamma(data: list[list[int]], col: int) -> int:
    ones: int = functools.reduce(lambda a,b: a + b[col], data, 0)
    return int(ones >= (len(data) // 2))

def total(f, data: list[list[int]]) -> int:
    result = 0
    for c in range(len(data[0])):
        result = (result << 1) | f(data, c)
    return result

def bitarraytoint(data: list[int]) -> int:
    result = 0
    for n in data:
        result = (result << 1) | n
    return result

def numcount(data: list[list[int]], c: int) -> tuple[int, int]:
    ones = functools.reduce(lambda a,b: a + b[c], data, 0)
    zeros = len(data) - ones
    return (ones, zeros)

def rating(f, data: list[list[int]]) -> int:
    temp = data
    c = 0
    while True:
        n = int(f(*numcount(temp, c)))
        temp = list(filter(lambda v: v[c] == n, temp))
        if len(temp) <= 1:
            return bitarraytoint(temp[0])
        c += 1  

def part1(data: list[list[int]]) -> int:
    return total(gamma, data) * total(lambda d,c: not gamma(d, c), data)

def part2(data: list[list[int]]) -> int:
    return rating(lambda o, z: o >= z, data) * rating(lambda o, z: z > o, data)

data = utils.get_input("d3")
pdata = list(map(lambda l: list(map(int, l)), data.splitlines()))
print(f"part 1: {part1(pdata)}")
print(f"part 2: {part2(pdata)}")
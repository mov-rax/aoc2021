import utils
import functools
import numpy

def gentable(data: str) -> list[int]:
    lines = map(lambda l: list(map(int, l)), data.splitlines())
    return list(lines)

def gamma(data: list[list[int]], col: int) -> int:
    ones: int = functools.reduce(lambda a,b: a + b[col], data, 0)
    return int(ones >= (len(data) // 2))

def total_gamma(data: list[list[int]]) -> int:
    result = 0
    for c in range(len(data[0])):
        g = gamma(data, c)
        result = (result << 1) | g
    return result
    
def total_epsilon(data: list[list[int]]) -> int:
    result = 0
    for c in range(len(data[0])):
        e = int(not gamma(data, c))
        result = (result << 1) | e
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

def oxygen_generator_rating(data: list[list[int]]) -> int:
    temp = data
    c = 0
    while True:
        ones, zeros = numcount(temp, c)
        n = int(ones >= zeros)
        temp = list(filter(lambda v: v[c] == n, temp))
        if len(temp) <= 1:
            return bitarraytoint(temp[0])
        c += 1

def co2_scrubber_rating(data: list[list[int]]) -> int:
    temp = data
    c = 0
    while True:
        ones, zeros = numcount(temp, c)
        n = int(zeros > ones)
        temp = list(filter(lambda v: v[c] == n, temp))
        if len(temp) <= 1:
            return bitarraytoint(temp[0])
        c += 1        

def part1(data: list[list[int]]) -> int:
    return total_gamma(data) * total_epsilon(data)

def part2(data: list[list[int]]) -> int:
    return oxygen_generator_rating(data) * co2_scrubber_rating(data)

data = utils.get_input("d3")
pdata = gentable(data)
print(f"part 1: {part1(pdata)}")
print(f"part 2: {part2(pdata)}")
import copy
import utils
import itertools

def part1(data : list[str]) -> int:
    gamma, epsilon = 0 ,0
    for col in range(len(data[0])):
        ones, zeros = 0, 0
        for row in range(len(data)):
            if data[row][col] == '1':
                ones += 1
            else:
                zeros += 1
        gamma = gamma << 1 | (ones > zeros)
        epsilon = epsilon << 1 | (ones <= zeros)
    return gamma * epsilon

def rating(bit, data : list[str]) -> int:
    idx = 0
    while len(data) != 1:
        ones, zeros = 0, 0
        for number in data:
            if number[idx] == '1':
                ones += 1
            else:
                zeros += 1
        if ones >= zeros:
            data = list(filter(lambda num: num[idx] == bit, data))
        else:
            data = list(filter(lambda num: not (num[idx] == bit), data))
        idx += 1
    return int(data[0], 2)

def part2(data : list[str]) -> int:
    oxygen_rating = rating('1', copy.copy(data))
    co2_rating = rating('0', copy.copy(data))
    return oxygen_rating * co2_rating
    

data = utils.get_input("d3").splitlines()
print(f"part 1: {part1(data)}")
print(f"part 2: {part2(data)}")
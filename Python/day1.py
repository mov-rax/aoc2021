import utils

def part1(vals : list[int]) -> int:
    inc = 0 
    for i in range(1, len(vals)):
        if vals[i] > vals[i-1]:
            inc += 1
    return inc

def part2(vals : list[int]) -> int:
    inc = 0
    for i in range(2, len(vals)-1):
        if sum(vals[i-2:i+1]) < sum(vals[i-1:i+2]):
            inc += 1
    return inc

data = utils.get_input("d1").splitlines()
nums = [int(x) for x in data]
print(f"part 1: {part1(nums)}")
print(f"part 2: {part2(nums)}")


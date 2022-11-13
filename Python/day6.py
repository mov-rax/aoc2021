import utils

memo = {}

def lanternfish(tick: int, days: int) -> int:
    """ every day the tick decrements by 1 

        after tick is 0, a new fish is spawned with tick=8
        after tick is 0, fish dies and new fish is spawned with tick=6
        if days run out, return 1
    """
    if (tick, days) in memo:
        return memo[(tick, days)]
    elif days == 0:
        return 1
    elif tick == 0:
        return lanternfish(8, days-1) + lanternfish(6, days-1)
    else:
        memo[(tick, days)] = lanternfish(tick-1, days-1)
        return memo[(tick, days)]

data = list(map(int, utils.get_input('d6').strip().split(',')))
part1 = sum((lanternfish(x, 80) for x in data))
part2 = sum((lanternfish(x, 256) for x in data))
print(f"part 1: {part1}")
print(f"part 2: {part2}")
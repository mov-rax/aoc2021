import utils
from enum import Enum

class Direction(Enum):
    FORWARD = 1
    UP = 2
    DOWN = 3

class Movement:

    def __init__(self, direction : Direction, magnitude : int):
        self.direction = direction
        self.magnitude = magnitude

    def __str__(self) -> str:
        return f"Movement({self.direction}, {self.magnitude})"

    def __repr__(self) -> str:
        return self.__str__()

    def from_str(s : str):
        match s.split(' '):
            case ["forward", mag]:
                return Movement(Direction.FORWARD, int(mag))
            case ["up", mag]:
                return Movement(Direction.UP, int(mag))
            case ["down", mag]:
                return Movement(Direction.DOWN, int(mag))
            case _:
                return None


class Submarine1:

    def __init__(self, depth = 0, horizontal = 0):
        self.depth = depth
        self.horizontal = horizontal

    def move(self, movement : Movement):
        match movement.direction:
            case Direction.FORWARD:
                self.horizontal += movement.magnitude
            case Direction.UP:
                self.depth -= movement.magnitude
            case Direction.DOWN:
                self.depth += movement.magnitude

class Submarine2:
    
    def __init__(self, depth = 0, horizontal = 0, aim = 0):
        self.depth = depth
        self.horizontal = horizontal
        self.aim = aim

    def move(self, movement: Movement):
        match movement.direction:
            case Direction.FORWARD:
                self.horizontal += movement.magnitude
                self.depth += movement.magnitude * self.aim
            case Direction.DOWN:
                self.aim += movement.magnitude
            case Direction.UP:
                self.aim -= movement.magnitude

def part1(vals : list[Movement]):
    sub = Submarine1()
    for movement in vals:
        sub.move(movement)
    return sub.depth * sub.horizontal

def part2(vals: list[Movement]):
    sub = Submarine2()
    for movement in vals:
        sub.move(movement)
    return sub.depth * sub.horizontal


data = utils.get_input("d2")
movements = [Movement.from_str(x) for x in data.splitlines()]
print(f"part 1: {part1(movements)}")
print(f"part 2: {part2(movements)}")
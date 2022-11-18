import utils
import functools as ft

opendict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

scoredict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

scoredict2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def together(itr, prev: list) -> tuple[None | int, None | int]:
    c = next(itr, None)
    match c:
        case opn if opn in ['(', '[', '<', '{']:
            prev.append(opendict[opn])
            return together(itr, prev)
        case close if close in [')', ']', '>', '}']:
            try:
                if prev.pop() == close:
                    return together(itr, prev)
            except:
                return (None, None)
            return (scoredict[close], None)
        case None:
            prev.reverse()
            return (None, ft.reduce(lambda a,v: 5*a + scoredict2[v], prev, 0))

def part1and2(data: list[str]) -> tuple[int, int]:
    result = [together(iter(x), []) for x in data]
    p1 = sum(x[0] if x[0]!=None else 0 for x in result)
    p2 = list(filter(lambda x:x!=None, (x[1] for x in result)))
    p2.sort()
    return (p1, p2[(len(p2)-1) // 2])

data = utils.get_input('d10').strip().splitlines()
p1, p2 = part1and2(data)
print(f"part 1: {p1}")
print(f"part 2: {p2}")
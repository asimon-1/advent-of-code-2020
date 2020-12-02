import re


def read_input(fn, cast_type=float):
    with open(fn, "r") as f:
        inp = f.readlines()
    return [cast_type(val) for val in inp]


def part_1(fn):
    inp = read_input(fn, cast_type=str)
    re_pattern = re.compile(
        r"^(?P<lower>\d+)-(?P<upper>\d+)\s(?P<char>\w): (?P<pw>\w+)$"
    )
    correct = 0
    for line in inp:
        match = re_pattern.search(line)
        lower = int(match.group("lower"))
        upper = int(match.group("upper"))
        char = match.group("char")
        pw = match.group("pw")
        count = pw.count(char)
        if lower <= count <= upper:
            correct += 1
    return correct


def part_2(fn):
    inp = read_input(fn, cast_type=str)
    re_pattern = re.compile(
        r"^(?P<lower>\d+)-(?P<upper>\d+)\s(?P<char>\w): (?P<pw>\w+)$"
    )
    correct = 0
    for line in inp:
        match = re_pattern.search(line)
        lower = int(match.group("lower")) - 1
        upper = int(match.group("upper")) - 1
        char = match.group("char")
        pw = match.group("pw")
        if (pw[lower] == char) ^ (pw[upper] == char):
            correct += 1
    return correct


if __name__ == "__main__":
    fn = "input/input.txt"
    print(f"Part 1 Answer for {fn}: {part_1(fn)}")
    print(f"Part 2 Answer for {fn}: {part_2(fn)}")

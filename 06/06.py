def read_input(fn, cast_type=float):
    with open(fn, "r") as f:
        inp = f.readlines()
    return [cast_type(val.strip()) for val in inp]

def part_1(fn):
    inp = read_input(fn, str)
    s = set()
    count = 0
    for line in inp:
        if not line:
            count += len(s)
            s.clear()
        else:
            [s.add(c) for c in line]
    count += len(s)
    return count

def part_2(fn):
    inp = read_input(fn, str)
    s = {c for c in "qwertyuiopasdfghjklzxcvbnm"}
    count = 0
    for line in inp:
        if not line:
            count += len(s)
            s = {c for c in "qwertyuiopasdfghjklzxcvbnm"}
        else:
            s = s.intersection({c for c in line})
    count += len(s)
    return count

if __name__ == "__main__":
    fn = "input/input.txt"
    print(f"Part 1 Answer for {fn}: {part_1(fn)}")
    print(f"Part 2 Answer for {fn}: {part_2(fn)}")
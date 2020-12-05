def read_input(fn, cast_type=float):
    with open(fn, "r") as f:
        inp = f.readlines()
    return [cast_type(val) for val in inp]


def part_1(fn):
    inp = read_input(fn, cast_type=str)
    highest_seat_id = 0
    for line in inp:
        seat = [0, 0]
        for ind, char in enumerate(line):
            if ind < 7:
                seat[0] += (2 ** (7 - ind - 1)) if char == "B" else 0
            else:
                seat[1] += (2 ** (3 - (ind - 7) - 1)) if char == "R" else 0
        highest_seat_id = max(highest_seat_id, 8 * seat[0] + seat[1])
    return highest_seat_id


def part_2(fn):
    inp = read_input(fn, cast_type=str)
    seat_id_list = [0] * 862
    for line in inp:
        seat = [0, 0]
        for ind, char in enumerate(line):
            if ind < 7:
                seat[0] += (2 ** (7 - ind - 1)) if char == "B" else 0
            else:
                seat[1] += (2 ** (3 - (ind - 7) - 1)) if char == "R" else 0
        seat_id_list[8 * seat[0] + seat[1]] = 1
    return [n for n, x in enumerate(seat_id_list) if not x][-1]


if __name__ == "__main__":
    fn = "input/input.txt"
    print(f"Part 1 Answer for {fn}: {part_1(fn)}")
    print(f"Part 2 Answer for {fn}: {part_2(fn)}")

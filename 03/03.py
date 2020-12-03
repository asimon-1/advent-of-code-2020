def read_input(fn, cast_type=float):
    with open(fn, "r") as f:
        inp = f.readlines()
    return [cast_type(val) for val in inp]


def cast_type(l):
    return_val = [1 if val == "#" else 0 if val == "." else -1 for val in l]
    try:
        return_val.remove(-1)
    except ValueError:
        pass
    return return_val


def traverse_slope(inp, index_increment, line_increment):
    index = 0
    count = 0
    wrap = len(inp[0])

    for line_ind, line in enumerate(inp):
        if not (line_ind % line_increment):
            count += line[index]
            index = (index + index_increment) % wrap
        else:
            continue
    return count


def part_1(fn):
    inp = read_input(fn, cast_type=cast_type)
    return traverse_slope(inp, 3, 1)


def part_2(fn):
    inp = read_input(fn, cast_type=cast_type)
    index_increment_list = [1, 3, 5, 7, 1]
    line_increment_list = [1, 1, 1, 1, 2]
    return_val = 1
    for index_increment, line_increment in zip(
        index_increment_list, line_increment_list
    ):
        return_val *= traverse_slope(inp, index_increment, line_increment)
    return return_val


if __name__ == "__main__":
    fn = "input/input.txt"
    print(f"Part 1 Answer for {fn}: {part_1(fn)}")
    print(f"Part 2 Answer for {fn}: {part_2(fn)}")

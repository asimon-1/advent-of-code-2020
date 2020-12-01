def read_input(fn, cast_type=float):
    with open(fn, "r") as f:
        inp = f.readlines()
    return [cast_type(val) for val in inp]


def find_sum(inp, sum_val, inp_val):
    j = sum_val - inp_val
    if j in inp:
        return inp_val * j
    else:
        return None


def part_1(fn):
    inp = read_input(fn)
    sum_val = 2020
    for inp_val in inp:
        return_val = find_sum(inp, sum_val, inp_val)
        if return_val:
            return return_val

def part_2(fn):
    inp = read_input(fn)
    sum_val = 2020
    for inp_val in inp:
        for sec_inp_val in inp:
            return_val = find_sum(inp, sum_val - inp_val, sec_inp_val)
            if return_val:
                return return_val * inp_val

if __name__ == "__main__":
    fn = "input/test.txt"
    print(f"Part 1 Answer for {fn}: {part_1(fn)}")
    print(f"Part 2 Answer for {fn}: {part_2(fn)}")

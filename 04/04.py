import re

def read_input(fn):
    with open(fn, "r") as f:
        inp = f.read()
    inp = re.sub(r"\n(?!\n)", " ", inp).splitlines()
    return [dict(x.split(":") for x in line.strip().split(" ")) for line in inp]

def validate(passport):
    if not 1920 <= int(passport["byr"]) <= 2002:
        return 0
    if not 2010 <= int(passport["iyr"]) <= 2020:
        return 0
    if not 2020 <= int(passport["eyr"]) <= 2030:
        return 0
    if "cm" in passport["hgt"]:
        if not 150 <= int(passport["hgt"].replace("cm", "")) <= 193:
            return 0
    elif "in" in passport["hgt"]:
        if not 59 <= int(passport["hgt"].replace("in", "")) <= 76:
            return 0
    else:
        return 0
    if not re.match(r"^#[0-9a-f]{6}$",passport["hcl"]):
        return 0
    if not re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", passport["ecl"]):
        return 0
    if not re.match(r"^\d{9}$", passport["pid"]):
        return 0
    return 1

def part_1(fn):
    inp = read_input(fn)
    valid = 0
    for line in inp:
        try:
            del line["cid"]
        except KeyError:
            pass
        if len(line.keys()) == 7:
            valid += 1
    return valid



def part_2(fn):
    inp = read_input(fn)
    valid = 0
    for line in inp:
        try:
            del line["cid"]
        except KeyError:
            pass
        if len(line.keys()) == 7:
            valid += validate(line)
    return valid


if __name__ == "__main__":
    fn = "input/input.txt"
    print(f"Part 1 Answer for {fn}: {part_1(fn)}")
    print(f"Part 2 Answer for {fn}: {part_2(fn)}")
def day15a(input: list[str]) -> int:
    strings = parse_input(input)
    sum = 0
    for string in strings:
        sum += compute_hash_value(string)
    return sum

def day15b(input: list[str]) -> int:
    initialization_steps = parse_input(input)

    boxes = [{} for _ in range(0, 256)]

    for step in initialization_steps:
        label = step.split("=")[0].rstrip("-")
        
        box_index = compute_hash_value(label)
        box = boxes[box_index]

        if step[-1] == "-":
            if label in box:
                del box[label]
        else:
            box[label] = int(step.split("=")[1])

    return compute_focusing_power(boxes)

def compute_focusing_power(boxes: list[tuple[list[str], dict[str, int]]]) -> int:
    focusing_power = 0
    for box_nr in range(1, 257):
        box = boxes[box_nr - 1]
        slot_nr = 1
        for focal_length in box.values():
            focusing_power += box_nr * slot_nr * focal_length
            slot_nr += 1
    return focusing_power

def compute_hash_value(string: str) -> int:
    hash_value = 0
    for char in string:
        hash_value = next_hash_value(hash_value, char)
    return hash_value

def next_hash_value(cur_hash_value: int, char: str) -> int:
    ascii_value = ord(char)
    return (cur_hash_value + ascii_value) * 17 % 256

def parse_input(input: list[str]) -> list[str]:
    return input[0].split(",")
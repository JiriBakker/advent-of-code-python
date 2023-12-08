from math import lcm

def day08a(input: list[str]) -> int:
    (instructions, nodes) = parse_input(input)
    return trace_path(instructions, nodes)

def day08b(input: list[str]) -> int:
    (instructions, nodes) = parse_input(input)
    loop_intervals = find_loop_intervals(instructions, nodes)
    return lcm(*loop_intervals)


class Node(object):
    def __init__(self, key: str, leftKey: str, rightKey: str):
        self.key = key
        self.leftKey = leftKey
        self.rightKey = rightKey

def trace_path(instructions: str, nodes: dict[str, Node]) -> int:
    cur_node = nodes["AAA"]
    instruction_index = 0
    path_length = 0
    while cur_node.key != "ZZZ":
        cur_node = nodes[cur_node.leftKey if instructions[instruction_index] == "L" else cur_node.rightKey]
        instruction_index = (instruction_index + 1) % len(instructions)
        path_length += 1

    return path_length

def find_loop_intervals(instructions: str, nodes: dict[str, Node]) -> list[int]:
    def is_start_node(key: str) -> bool:
        return key[2] == "A"

    def is_end_node(key: str) -> bool:
        return key[2] == "Z"

    cur_nodes: list[Node] = list(filter(lambda node: is_start_node(node.key), nodes.values()))
    nr_of_end_nodes = len(list(filter(lambda node: is_end_node(node.key), nodes.values())))

    path_length = 0
    end_nodes_seen = {}
    while True:
        cur_nodes = list(map(lambda node: nodes[node.leftKey] if instructions[path_length % len(instructions)] == "L" else nodes[node.rightKey], cur_nodes))
        path_length += 1

        for end_node in filter(lambda node: is_end_node(node.key), cur_nodes):
            if end_node.key not in end_nodes_seen:
                end_nodes_seen[end_node.key] = path_length
            
            if len(end_nodes_seen) == nr_of_end_nodes:
                return list(end_nodes_seen.values())

def parse_input(input: list[str]) -> tuple[str, dict[str, Node]]:
    nodes = {}
    instructions = input[0]
    for line in input[2:]:
        (key, _, leftKey, rightKey) = line.split(" ")
        nodes[key] = Node(key, leftKey.replace("(", "").replace(",", ""), rightKey.replace(")", ""))

    return (instructions, nodes)
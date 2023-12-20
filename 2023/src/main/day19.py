import sys
from typing import Callable


def day19a(input: list[str]) -> int:
    (workflows, ratings) = parse_input(input)
    print(f"{len(workflows)} workflows")

    in_workflow = workflows["in"]
    accepted_ratings: list[dict[str,int]] = []
    for rating in ratings:
        cur_workflow = in_workflow
        while True:
            evaluate_result = cur_workflow.evaluate(rating)
            print(f"{cur_workflow.name} -> {rating} ==== {evaluate_result}")
            if evaluate_result == "A":
                accepted_ratings.append(rating)
                break
            if evaluate_result == "R":
                break
            cur_workflow = workflows[evaluate_result]

    sum = 0
    for rating in accepted_ratings:
        sum += rating["x"] + rating["m"] + rating["a"] + rating["s"]

    return sum

def day19b(input: list[str]) -> int:
    return 0

class Workflow(object):
    def __init__(self, name: str):
        self.name = name
        self.rules: list[tuple[tuple[str,str,int], str]] = []

    def add_rule(self, part: str, comparator: str, compare_value: int, workflow_if_successful: str):
        self.rules.append(((part, comparator, compare_value), workflow_if_successful))

    def evaluate(self, parts: dict[str, int]) -> str:
        for ((part, comparator, compare_value), workflow_if_successful) in self.rules:
            if comparator == ">":
                if parts[part] > compare_value:
                    return workflow_if_successful
            else:
                if parts[part] < compare_value:
                    return workflow_if_successful
        raise
    
def parse_input(input: list[str]) -> tuple[dict[str, Workflow],list[dict[str,int]]]:
    print(input)
    workflows: dict[str, Workflow] = {}
    i = 0
    line = input[i]
    while len(line) > 0:
        (name, rest) = line.split("{")
        rules = rest.rstrip("}").split(",")

        workflow = Workflow(name)
        workflows[name] = workflow
        for rule in rules:
            rule_parts = rule.split(":")
            print(f"{rule_parts}")
            if len(rule_parts) != 2:
                workflow.add_rule("x", ">", -sys.maxsize, rule_parts[0])    
            else:
                part = rule_parts[0][0]
                workflow.add_rule(part, rule_parts[0][1], int(rule_parts[0][2:]), rule_parts[1])

        i += 1
        line = input[i]

    ratings: list[dict[str,int]] = []
    for line in input[i + 1:]:
        parts: dict[str, int] = {}
        for part in line[1:-1].split(","):
            (name, value) = part.split("=")
            parts[name] = int(value)
        ratings.append(parts)

    return (workflows, ratings)

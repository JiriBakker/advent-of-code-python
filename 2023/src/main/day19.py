from __future__ import annotations

def day19a(input: list[str]) -> int:
    (workflows, ratings) = parse_input(input)

    in_workflow = workflows["in"]
    accepted_ratings: list[dict[str,int]] = []
    for rating in ratings:
        cur_workflow = in_workflow
        while True:
            evaluate_result = cur_workflow.evaluate(rating)
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
    (workflows, _) = parse_input(input)

    in_workflow = workflows["in"]

    ratings: dict[str,tuple[int,int]] = {"a": (1, 4000), "s": (1, 4000), "m": (1, 4000), "x": (1, 4000)}
    accepted_ratings: list[dict[str,tuple[int,int]]] = []

    queue: list[tuple[Workflow,int,dict[str,tuple[int,int]]]] = [(in_workflow, 0, ratings)]
    while len(queue) > 0:
        (workflow, rule_index, ratings) = queue.pop(0)

        ((part, comparator, compare_value), workflow_if_successful) = workflow.rules[rule_index]
        if comparator == ">":
            ratings_success = dict(ratings)
            ratings_success[part] = (max(ratings[part][0], compare_value + 1), max(compare_value + 1, ratings[part][1]))
            if workflow_if_successful == "A":
                accepted_ratings.append(ratings_success)
            elif workflow_if_successful != "R":
                queue.append((workflows[workflow_if_successful], 0, ratings_success))

            ratings_fail = dict(ratings)
            ratings_fail[part] = (min(ratings[part][0], compare_value), min(compare_value, ratings[part][1]))
            queue.append((workflow, rule_index + 1, ratings_fail))
        elif comparator == "<":
            ratings_success = dict(ratings)
            ratings_success[part] = (min(ratings[part][0], compare_value - 1), min(compare_value - 1, ratings[part][1]))
            if workflow_if_successful == "A":
                accepted_ratings.append(ratings_success)
            elif workflow_if_successful != "R":
                queue.append((workflows[workflow_if_successful], 0, ratings_success))

            ratings_fail = dict(ratings)
            ratings_fail[part] = (max(ratings[part][0], compare_value), max(compare_value, ratings[part][1]))
            queue.append((workflow, rule_index + 1, ratings_fail))
        else:
            if workflow_if_successful == "A":
                accepted_ratings.append(ratings)
            elif workflow_if_successful != "R":
                queue.append((workflows[workflow_if_successful], 0, ratings))

    count = 0
    for accepted_rating in accepted_ratings:
        count += (accepted_rating["x"][1] - accepted_rating["x"][0] + 1) * (accepted_rating["m"][1] - accepted_rating["m"][0] + 1) * (accepted_rating["a"][1] - accepted_rating["a"][0] + 1) * (accepted_rating["s"][1] - accepted_rating["s"][0] + 1)

    return count

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
            elif comparator == "<":
                if parts[part] < compare_value:
                    return workflow_if_successful
            else:
                return workflow_if_successful
        raise
    
def parse_input(input: list[str]) -> tuple[dict[str, Workflow],list[dict[str,int]]]:
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
            if len(rule_parts) != 2:
                workflow.add_rule("", "", 0, rule_parts[0])    
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
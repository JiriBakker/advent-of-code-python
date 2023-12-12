def day12a(input: list[str]) -> int:
    records = parse_records(input)
    return sum(map(lambda record: find_arrangements(record[0], tuple(record[1])), records))

def day12b(input: list[str]) -> int:
    records = parse_records(input)
    records_times_five = map(lambda record: (record[0] + "?" + record[0] + "?" + record[0] + "?" + record[0] + "?" + record[0], record[1] + record[1] + record[1] + record[1] + record[1]), records)
    return sum(map(lambda record: find_arrangements(record[0], tuple(record[1])), records_times_five))

def parse_records(input: list[str]) -> list[tuple[list[str], list[int]]]:
    records = []
    for line in input:
        group_counts = list(map(lambda nr: int(nr), line.split(" ")[1].split(",")))
        conditions = line.split(" ")[0]
        records.append((conditions, group_counts))
    return records

result_cache = {}

def find_arrangements(conditions: str, group_counts: tuple[int]) -> int:
    cache_key = f"{conditions}_{group_counts}"
    if cache_key in result_cache:
        return result_cache[cache_key]
    
    def cache_result(result: int) -> int:
        result_cache[cache_key] = result
        return result

    if len(group_counts) == 0:
        return cache_result(1 if conditions.find("#") == -1 else 0)
    
    if len(conditions) == 0:
        return cache_result(0)
    
    if conditions[0] == ".":
        return cache_result(find_arrangements(conditions.lstrip("."), group_counts))

    cur_index = 0
    while cur_index < len(conditions) and conditions[cur_index] != ".":
        cur_index += 1

    continuous_group = conditions[:cur_index]

    valid_arrangement_count = 0
    for index in find_valid_sub_arrangements(continuous_group, group_counts[0]):
        valid_arrangement_count += find_arrangements(conditions[index + group_counts[0] + 1:], group_counts[1:])

    if continuous_group.find("#") == -1:
        valid_arrangement_count += find_arrangements(conditions[cur_index:], group_counts)

    return cache_result(valid_arrangement_count)

def find_valid_sub_arrangements(conditions: str, count: int) -> list[int]:
    if conditions.find("#") == -1:
        return list(range(0, len(conditions) - count + 1))
    
    index_first_hash = conditions.index("#")

    valid_sub_arrangements_start_indices = []
    for index in range(0, index_first_hash + 1):
        if index + count > len(conditions):
            break
        if index + count == len(conditions) or conditions[index + count] == "?":
            valid_sub_arrangements_start_indices.append(index)

    return valid_sub_arrangements_start_indices
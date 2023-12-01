def read_input(day: int) -> list[str]:
    with open(f"2023/input/day{str(day).zfill(2)}") as file:
        return [line.rstrip() for line in file]
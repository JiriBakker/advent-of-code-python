from main.util import max_of

def day02a(input: list[str]) -> int:
    games = parse_games(input)
    possible_games = filter(lambda game: is_game_possible(game), games)
    return sum(map(lambda game: game[0], possible_games))

def day02b(input: list[str]) -> int:
    games = parse_games(input)
    min_dice = map(lambda game: compute_min_dice(game), games)
    return sum(map(lambda min_die: min_die[0] * min_die[1] * min_die[2], min_dice))

def parse_games(input: list[str]) -> list[tuple[int, list[tuple[int, int, int]]]]:
    def parse_game(line: str) -> tuple[int, list[tuple[int, int, int]]]:
        sections = line.split(":")
        gameId = int(sections[0].split(" ")[1].rstrip(":"))

        reachSections = line[len(sections[0]) + 2:].split(";")
        reaches:list[tuple[int,int,int]] = []

        for reach in reachSections:
            tokens = reach.strip().split(" ")
            colorCounts = { "red": 0, "green": 0, "blue": 0 }
            for i in range(0, int(len(tokens) / 2)):
                count = int(tokens[i * 2])
                color = tokens[i * 2 + 1].rstrip(",").rstrip(";")
                colorCounts[color] = colorCounts[color] + count
            reaches.append((colorCounts["red"], colorCounts["green"], colorCounts["blue"]))

        return (gameId, reaches)
    
    return list(map(lambda line: parse_game(line), input))

def is_game_possible(game: tuple[int, list[tuple[int, int, int]]]) -> bool:
    for reach in game[1]:
        (red, green, blue) = reach
        if red > 12 or green > 13 or blue > 14:
            return False
        
    return True

def compute_min_dice(game: tuple[int, list[tuple[int, int, int]]]) -> list[int]:
    return [
        max_of(lambda reach: reach[0], game[1]), # red
        max_of(lambda reach: reach[1], game[1]), # green
        max_of(lambda reach: reach[2], game[1])  # blue
    ]
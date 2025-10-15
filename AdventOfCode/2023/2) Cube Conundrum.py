import io

from Utils.logger import logger

def parse_games(file):
    games = {}
    for line in file:
        first = line.strip().split(": ")
        id = int(first[0].split(" ")[1])
        shows_str = first[1].split("; ")
        shows = []
        for show in shows_str:
            cubes = show.split(", ")
            show_map = {}
            for cube in cubes:
                temp = cube.split(" ")
                count = int(temp[0])
                colour = temp[1]
                show_map[colour] = count
            shows.append(show_map)
        games[id] = shows
    return games




def possible_games(games, red=12, green=13, blue=14):
    output = []
    for id, shows in games.items():
        valid = True
        for show in shows:
            if show.get("red", 0) > red or show.get("green", 0) > green or show.get("blue", 0) > blue:
                valid = False
                break
        if valid:
            output.append(id)

    return sum(output)

def min_cubes(games):
    output = []
    for shows in games.values():
        red_max = 0
        green_max = 0
        blue_max = 0
        for show in shows:
            red_max = max(show.get("red", 0), red_max)
            green_max = max(show.get("green", 0), green_max)
            blue_max = max(show.get("blue", 0), blue_max)

        output.append(red_max*green_max*blue_max)

    return sum(output)

if __name__ == "__main__":
    filepath = input("Input File Path: ")

    file = io.StringIO("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""")

    try:
        file = open(filepath)
    except:
        pass

    games = parse_games(file)
    logger.print(games)

    logger.print(possible_games(games))
    logger.print(min_cubes(games))
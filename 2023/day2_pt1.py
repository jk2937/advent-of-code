puzzle_input = '''Game 1: 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green
Game 2: 16 blue, 9 red, 5 green; 8 red; 8 blue, 5 green, 12 red; 11 blue, 8 green, 17 red
Game 3: 8 green, 1 blue, 7 red; 12 red, 6 blue, 9 green; 2 blue, 1 red, 14 green; 9 green, 4 red; 2 red, 1 blue, 8 green
Game 4: 1 blue, 3 green; 2 green, 1 blue, 1 red; 1 red, 3 green
Game 5: 6 red, 1 blue; 1 green; 5 red, 2 green; 1 red, 1 blue, 3 green
Game 6: 3 green, 4 red, 1 blue; 2 blue, 5 green, 2 red; 12 green, 3 blue, 2 red; 4 blue, 1 green, 4 red; 11 green, 6 red; 5 green, 10 red, 3 blue
Game 7: 2 blue, 3 green, 16 red; 1 blue, 3 red; 2 green, 13 red; 18 red, 2 blue, 1 green; 3 red, 1 blue
Game 8: 4 red, 3 blue, 8 green; 2 red, 16 green; 2 red, 1 blue
Game 9: 4 green, 14 blue, 8 red; 17 blue, 3 red, 5 green; 2 green, 4 red, 6 blue; 7 red, 2 green, 18 blue; 3 red, 19 blue, 4 green; 4 green, 8 red, 6 blue
Game 10: 12 green, 7 red, 1 blue; 6 red, 12 green; 6 red, 7 green, 1 blue; 1 red, 1 blue, 18 green; 11 green, 1 blue
Game 11: 10 green, 3 red, 13 blue; 13 blue, 6 green, 8 red; 12 blue, 4 green, 8 red; 9 green, 9 red, 3 blue; 6 blue, 7 green, 6 red; 11 blue, 13 green
Game 12: 9 green, 2 blue; 4 green, 1 blue, 7 red; 2 green, 1 blue, 5 red
Game 13: 1 green; 7 blue, 1 red, 2 green; 8 blue, 2 green
Game 14: 8 red, 3 green; 1 red, 8 green; 1 blue, 10 green
Game 15: 1 blue, 6 green, 14 red; 3 red, 1 blue, 6 green; 4 green; 1 blue, 5 green, 2 red; 2 blue, 1 green, 6 red; 4 red, 8 green, 1 blue
Game 16: 1 green, 6 red, 8 blue; 1 green, 11 blue, 1 red; 7 blue, 3 green, 4 red; 2 green, 6 red, 12 blue
Game 17: 3 blue, 4 red, 4 green; 18 blue, 6 red, 11 green; 2 green, 6 red, 17 blue; 12 green, 3 blue, 5 red
Game 18: 3 green, 2 blue, 10 red; 7 green, 10 blue; 9 blue, 7 red, 14 green; 18 green, 10 blue, 11 red; 10 red, 2 blue, 16 green
Game 19: 6 red, 1 green, 18 blue; 2 red, 1 blue; 7 blue, 3 red, 2 green; 18 blue, 2 green, 1 red; 7 red, 10 blue
Game 20: 13 blue, 2 red; 2 green, 2 red; 1 green, 9 blue
Game 21: 4 blue, 1 red; 2 red, 4 blue, 1 green; 3 red; 4 green, 1 red, 1 blue; 3 green, 9 blue, 1 red
Game 22: 7 blue, 5 green, 14 red; 15 red, 9 blue, 11 green; 10 blue, 5 red, 11 green; 14 red, 10 blue, 13 green
Game 23: 10 red, 6 blue; 1 red, 4 blue, 3 green; 3 green, 2 blue; 5 red, 3 green; 3 green, 4 blue, 5 red; 3 green, 7 red, 6 blue
Game 24: 4 red, 8 green; 1 red, 10 green; 2 red, 1 green; 2 green, 1 blue; 4 red, 12 green; 3 green
Game 25: 5 red, 2 blue, 6 green; 4 red, 3 blue, 8 green; 11 green, 4 red, 1 blue
Game 26: 5 blue, 1 red; 18 blue, 4 green; 9 green, 3 red, 17 blue; 6 green, 10 blue, 1 red; 3 blue, 7 green; 4 blue, 3 red, 5 green
Game 27: 13 red, 2 blue; 7 blue, 2 green, 12 red; 1 green, 9 blue, 9 red; 4 red, 4 green, 8 blue; 13 red, 6 blue; 3 red, 9 blue, 3 green
Game 28: 1 blue, 12 green, 1 red; 1 blue, 12 green, 2 red; 2 red, 8 green, 1 blue; 5 green, 2 red; 1 blue, 9 green, 6 red; 1 blue, 13 green
Game 29: 5 blue, 5 red, 11 green; 15 blue, 5 red, 10 green; 2 red, 11 green, 19 blue; 19 blue, 3 green, 6 red
Game 30: 1 blue, 12 red, 1 green; 12 blue, 1 red, 2 green; 12 red, 5 green; 2 red, 2 green, 5 blue; 5 red, 2 green, 6 blue
Game 31: 20 green, 1 red, 16 blue; 3 green, 1 red, 7 blue; 6 red, 18 blue, 8 green
Game 32: 5 green; 1 blue, 2 red, 5 green; 1 blue, 2 red, 5 green; 2 green, 2 red
Game 33: 6 blue, 5 green; 6 blue, 3 red, 1 green; 4 green, 3 blue, 2 red; 1 red, 6 blue, 5 green; 1 blue, 2 red, 5 green; 4 red, 3 blue
Game 34: 12 red, 12 green; 12 red, 7 green; 1 blue, 12 red, 11 green; 7 red, 7 green, 2 blue
Game 35: 3 red, 3 blue, 1 green; 1 green, 5 red, 5 blue; 8 green, 2 red, 14 blue; 8 green; 6 blue, 3 red, 6 green; 1 red, 1 blue, 12 green
Game 36: 13 red, 5 blue; 13 blue, 10 green, 6 red; 10 red, 5 green, 10 blue; 10 blue, 8 green, 6 red; 1 green, 14 red, 2 blue; 8 green, 4 blue
Game 37: 6 green, 1 red; 1 blue, 4 green, 1 red; 1 red, 14 green; 1 red, 9 green; 1 green, 1 red; 9 green, 1 red
Game 38: 1 green, 4 blue, 17 red; 13 red, 9 blue, 12 green; 7 green, 11 blue
Game 39: 18 green, 9 blue, 2 red; 11 red, 1 blue, 4 green; 9 red, 4 green, 10 blue; 9 blue, 5 red, 2 green
Game 40: 3 green, 8 red; 2 green, 6 red; 1 green, 9 red, 4 blue; 1 blue, 6 red; 2 green, 2 blue, 3 red
Game 41: 3 red, 15 green, 3 blue; 19 green, 2 red, 5 blue; 8 blue, 7 green, 4 red; 3 blue, 4 red, 5 green; 1 blue; 6 blue, 15 green, 3 red
Game 42: 2 red, 18 blue, 6 green; 3 green, 2 blue, 8 red; 9 blue, 1 green, 5 red; 12 red, 3 blue, 8 green
Game 43: 3 blue, 1 green, 3 red; 8 blue, 3 green, 1 red; 3 red, 5 blue; 3 green, 3 red, 7 blue; 6 blue, 1 green, 2 red; 7 blue, 2 green, 5 red
Game 44: 2 green, 5 blue, 1 red; 9 red, 16 blue; 4 blue, 2 green, 12 red; 13 red, 5 blue, 10 green; 4 green, 3 blue, 11 red
Game 45: 6 blue, 3 red, 13 green; 10 green, 13 blue, 12 red; 7 red, 19 blue, 16 green; 15 blue, 4 red, 11 green; 1 red, 4 green
Game 46: 11 red, 2 green; 5 blue, 2 red, 2 green; 3 green, 8 red, 6 blue; 3 blue, 10 green, 8 red
Game 47: 6 green, 16 red; 4 blue, 4 red, 2 green; 3 blue, 1 green, 12 red; 2 red, 4 blue, 4 green; 2 blue, 16 red; 5 blue, 5 green, 5 red
Game 48: 8 red, 1 blue; 1 green, 2 blue, 6 red; 11 red, 6 green, 2 blue
Game 49: 5 green, 16 blue, 2 red; 2 red, 20 blue, 6 green; 1 red, 3 blue, 5 green; 7 green, 4 blue
Game 50: 9 red, 8 green; 11 green, 10 red, 1 blue; 9 red, 5 green; 1 blue, 12 green, 8 red; 1 blue, 5 green, 2 red; 6 green, 1 blue, 2 red
Game 51: 1 red, 4 blue; 1 red, 3 green, 3 blue; 1 green, 1 red, 2 blue
Game 52: 11 red, 4 blue; 1 green, 6 blue, 10 red; 8 blue, 13 red
Game 53: 6 green, 9 red; 4 blue, 13 red, 2 green; 10 red, 5 green, 3 blue; 11 red, 3 blue, 4 green
Game 54: 16 red, 9 blue, 8 green; 9 red, 1 blue; 12 green, 2 red, 13 blue; 5 blue, 14 green, 15 red; 3 green, 2 red, 2 blue
Game 55: 3 green, 4 blue, 5 red; 3 red, 9 green, 1 blue; 3 blue, 4 green, 5 red; 4 green, 3 blue, 7 red; 5 red, 2 blue; 2 blue, 8 red, 5 green
Game 56: 3 red, 5 green, 3 blue; 15 red, 3 green, 15 blue; 3 green, 1 blue, 10 red; 15 blue, 1 red, 2 green; 6 red, 16 blue, 6 green; 19 red, 16 blue
Game 57: 5 blue, 1 red, 5 green; 8 blue, 16 green; 13 green, 5 blue, 3 red; 1 blue, 1 red, 13 green; 12 green, 3 red, 4 blue; 8 blue, 3 red, 1 green
Game 58: 5 blue, 4 green; 7 blue, 1 red, 10 green; 1 red, 13 green, 4 blue; 7 blue, 12 green, 4 red; 4 red, 13 green, 5 blue; 2 green, 1 blue, 12 red
Game 59: 2 red, 11 blue, 6 green; 1 green, 8 blue, 3 red; 4 red, 6 blue
Game 60: 4 green, 1 red; 3 blue, 15 red, 2 green; 13 red, 16 blue, 2 green; 6 green, 13 blue, 10 red; 15 blue, 11 red, 5 green; 7 blue, 4 green
Game 61: 14 red, 2 green, 14 blue; 1 green, 15 red, 3 blue; 2 green, 8 blue
Game 62: 13 green, 13 blue; 1 red, 6 green, 1 blue; 13 blue, 16 green; 3 blue, 1 red, 2 green
Game 63: 10 blue, 3 red, 4 green; 15 red; 10 blue, 10 green, 14 red; 9 blue, 6 green; 3 blue, 7 green, 13 red
Game 64: 2 red, 4 green; 1 blue, 9 red; 1 green, 2 blue, 10 red; 9 red, 1 blue, 5 green; 6 green, 6 red
Game 65: 10 blue, 4 green; 4 green, 2 red, 9 blue; 11 red, 1 green, 10 blue; 14 green, 19 blue, 3 red; 12 red, 5 blue, 11 green; 14 blue, 12 green, 11 red
Game 66: 5 blue, 2 red; 5 blue, 1 green, 7 red; 14 red, 1 green, 2 blue; 8 red, 7 blue; 2 red, 4 blue, 1 green; 2 blue, 18 red
Game 67: 6 red, 1 blue; 5 green, 2 blue, 1 red; 2 red, 3 green, 3 blue; 8 green, 4 blue, 6 red
Game 68: 4 blue, 1 green; 12 blue, 2 red, 3 green; 2 green, 7 blue; 1 red, 19 blue, 3 green
Game 69: 6 green, 11 red, 2 blue; 1 blue, 7 green, 6 red; 1 blue, 8 red; 17 red, 3 blue, 5 green
Game 70: 2 green, 6 red, 4 blue; 2 green, 7 red, 1 blue; 11 blue, 1 green
Game 71: 10 blue, 9 red; 3 red, 10 blue; 1 red, 8 blue, 2 green; 7 blue, 4 green, 5 red; 6 red, 2 blue, 7 green; 5 red, 2 blue, 4 green
Game 72: 1 green, 12 blue, 8 red; 9 red, 3 blue; 2 red, 2 green, 10 blue
Game 73: 7 red, 3 green, 11 blue; 4 green, 7 blue; 6 blue, 13 green, 9 red; 11 green, 4 blue; 12 blue, 3 red, 2 green; 9 green
Game 74: 5 blue, 2 red; 6 red, 1 blue, 8 green; 6 green, 5 blue, 16 red; 1 green, 9 red, 3 blue; 12 green, 1 red, 1 blue; 2 blue, 7 green, 13 red
Game 75: 5 green, 20 red; 7 red, 6 green, 2 blue; 4 green, 2 blue; 2 blue, 1 green, 3 red; 2 blue, 2 green, 12 red; 6 red, 6 green
Game 76: 9 red, 12 green, 3 blue; 2 blue, 1 red, 6 green; 13 green, 2 blue; 2 red, 7 green, 3 blue; 7 red, 4 green, 2 blue; 2 red, 3 blue, 3 green
Game 77: 2 blue, 6 red; 4 red, 15 green, 1 blue; 7 green, 5 blue, 6 red; 4 red, 5 blue
Game 78: 5 blue, 3 red, 1 green; 2 green, 7 red, 3 blue; 3 blue, 5 red, 5 green
Game 79: 6 red, 9 blue, 1 green; 9 green, 8 red, 7 blue; 1 blue, 12 green, 13 red; 7 red, 14 blue, 2 green; 13 blue, 4 green, 9 red; 4 blue, 2 green
Game 80: 4 green, 2 blue; 5 green, 3 red, 8 blue; 9 blue, 11 red, 4 green; 2 blue, 3 green, 4 red; 5 red
Game 81: 8 red, 3 blue, 4 green; 13 blue, 8 red, 1 green; 6 blue, 1 green; 18 green, 6 red, 10 blue; 17 green, 8 blue, 3 red; 6 red, 5 green, 12 blue
Game 82: 3 red, 7 blue; 4 red, 6 blue, 14 green; 9 blue, 2 green, 3 red
Game 83: 1 blue, 2 red; 5 green, 16 red; 12 red, 1 green; 8 green, 8 red
Game 84: 3 red, 9 green, 1 blue; 3 red, 6 blue, 7 green; 5 red, 8 green, 8 blue; 5 red, 3 blue, 11 green; 3 green, 4 blue; 4 green, 1 blue, 2 red
Game 85: 4 red, 6 blue, 1 green; 7 red, 6 blue; 9 red, 1 green; 1 blue, 1 green, 10 red; 2 red, 2 blue, 1 green; 5 blue, 7 red
Game 86: 4 blue, 5 green, 6 red; 9 red, 3 blue; 5 green, 3 red, 10 blue; 3 green, 7 blue, 3 red; 4 red; 4 green, 1 blue, 8 red
Game 87: 3 red, 3 green; 3 blue, 1 green; 3 red, 3 green; 3 red, 1 blue, 3 green; 2 green, 1 red
Game 88: 1 red, 13 green, 3 blue; 17 blue, 14 green, 5 red; 3 red, 19 blue, 13 green; 7 green, 19 blue; 5 red, 13 green, 17 blue; 13 blue, 8 green, 2 red
Game 89: 3 blue, 4 red; 2 green, 15 red, 1 blue; 3 green, 3 blue, 13 red; 3 blue, 9 red, 2 green; 8 red
Game 90: 2 red, 2 green, 1 blue; 3 blue, 2 green; 1 blue, 2 green, 4 red; 3 blue
Game 91: 13 blue, 5 green, 4 red; 17 blue, 8 red, 11 green; 1 green, 6 red, 19 blue; 12 blue, 6 green; 7 green, 2 red
Game 92: 6 red, 4 green; 2 blue, 11 red; 4 green, 7 blue; 2 red, 12 blue, 2 green
Game 93: 3 blue, 2 red; 2 blue, 11 red, 1 green; 7 red, 1 green; 1 red, 2 blue; 13 red, 3 blue
Game 94: 2 blue, 1 red, 20 green; 1 red, 4 blue, 10 green; 1 red, 20 green, 13 blue; 20 green
Game 95: 6 blue, 1 green; 3 red, 11 green; 4 blue
Game 96: 4 red, 4 green, 3 blue; 4 green, 17 blue, 3 red; 3 red, 3 blue, 13 green; 8 red, 7 blue, 6 green
Game 97: 5 blue, 9 green; 4 green, 4 blue; 4 red, 19 green; 2 red, 3 green; 19 green, 3 blue, 4 red; 3 red, 10 green
Game 98: 4 blue, 10 red, 8 green; 2 red, 3 green; 5 red, 4 blue, 10 green
Game 99: 9 blue, 12 red; 9 blue, 11 red, 13 green; 9 blue, 1 red, 13 green; 4 blue, 12 green; 10 blue, 17 red, 8 green
Game 100: 8 red, 3 green; 4 green, 1 blue, 15 red; 10 red, 8 green, 1 blue'''

debug_enabled = True
debug_pause = False
def debug_print(*args):
    global debug_enabled
    if debug_enabled == False:
        return
    print("DEBUG -", *args)

    global debug_pause
    if debug_pause == True:
        input("DEBUG - Press enter to continue")

max_red = 12
max_green = 13
max_blue = 14

import re

regex_find_color = "(?<=)\d+(?=\s{}})" #  r"(\d+) red"
re.findall(regex_find_color.format("green"), puzzle_input.split("\n")[0])

false_game_ids = []
for line in puzzle_input.split("\n"):
  game_id = int( re.findall(regex_game_ids, line)[0] )
  red = re.findall( regex_find_color.format("red"), line )
  green = re.findall( regex_find_color.format("green"), line )
  blue = re.findall( regex_find_color.format("blue"), line )
  debug_print(f"Print line - {line}")
  debug_print(f"Print game_id - {game_id}")
  debug_print(f"Print red - {red}")
  debug_print(f"Print green - {green}")
  debug_print(f"Print blue - {blue}")
  for num in red:
    num = int(num)
    if num > max_red and game_id not in false_game_ids:
      false_game_ids.append(game_id)
  for num in green:
    num = int(num)
    if num > max_green and game_id not in false_game_ids:
      false_game_ids.append(game_id)
  for num in blue:
    num = int(num)
    if num > max_blue and game_id not in false_game_ids:
      false_game_ids.append(game_id)

print(false_game_ids)
print(len(false_game_ids))

true_game_ids = []
all_game_ids = re.findall( regex_game_ids, puzzle_input )
for item in all_game_ids:
  if int(item) not in false_game_ids:
    true_game_ids.append(item)

print(true_game_ids)
len(true_game_ids)

print(all_game_ids)
print(len(all_game_ids))

print(all_game_ids)
print(len(all_game_ids))



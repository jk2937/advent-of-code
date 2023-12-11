_str = open("puzzle_input_day3.txt", "r").read()
arr = _str.split("\n")

if arr[-1] == '':
    arr[-1].pop()

number_data = []
seek_dot = False
for y, line in enumerate(arr):
    for x, data in enumerate(line):
        if data.isdigit():
            if seek_dot:
                continue
            num = line[x:].split(".")[0]
            num_str_len = line[x:].find(".")
            number_data.append({"x": x, "y": y, "str_len": num_str_len, "num": num})
            seek_dot = True
            continue
        elif data == ".":
            seek_dot = False

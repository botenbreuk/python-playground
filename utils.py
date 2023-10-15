def read_grid(lines: list[str]):
    grid = []
    for line in lines:
        value = to_line_array(line)
        grid.append(value)
    return grid


def to_line_array(line: str):
    arr = []
    splitted = line.strip().split()
    for i in splitted:
        if i == '||':
            continue
        arr.append(i)
    return arr

def read_grid(lines: list[str]) -> list[list[str]]:
    grid: list[list[str]] = []
    for line in lines:
        value = __to_line_array(line)
        grid.append(value)
    return grid


def __to_line_array(line: str) -> list[str]:
    arr: list[str] = []
    splitted = line.strip().split()
    for i in splitted:
        if i == '||':
            continue
        arr.append(i)
    return arr

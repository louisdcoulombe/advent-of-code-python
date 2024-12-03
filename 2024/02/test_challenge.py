from main import parse_input, part1, part2

EXAMPLE = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()

def test_parse():
    matrix = parse_input(EXAMPLE)
    assert matrix[0] == [7, 6, 4, 2, 1]
    assert matrix[-1] == [1, 3, 6, 7, 9]


def test_part1():
    result = part1(EXAMPLE)
    assert result == 2

def test_part2():
    result = part2(EXAMPLE)
    assert result == 4

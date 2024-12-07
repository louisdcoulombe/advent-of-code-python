from main import parse_input, part1, part2

EXAMPLE = """

""".strip()

def test_parse():
    a, b = parse_input(EXAMPLE)
    assert a == [3, 4, 2, 1, 3, 3]
    assert b == [4, 3, 5, 3, 9, 3]


def test_part1():
    result = part1(EXAMPLE)
    assert result == 11

def test_part2():
    result = part2(EXAMPLE)
    assert result == 31

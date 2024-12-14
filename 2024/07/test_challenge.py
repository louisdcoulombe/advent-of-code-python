import pytest
from main import parse_input, part1, part2

EXAMPLE = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip()

def test_parse():
    d = parse_input(EXAMPLE)
    assert d[190] == [10, 19]


def test_part1():
    result = part1(EXAMPLE)
    assert result == 3749

def test_part2():
    result = part2(EXAMPLE)
    assert result == 31

if __name__ == '__main__':
    pytest.main(['-vv'])

import pytest
from main import parse_input, part1, part2

EXAMPLE = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()

def test_parse():
    matrix = parse_input(EXAMPLE)
    assert len(matrix) == 10
    assert len(matrix[0]) == 10


def test_part1():
    result = part1(EXAMPLE)
    assert result == 18

def test_part2():
    result = part2(EXAMPLE)
    assert result == 9

if __name__ == '__main__':
    pytest.main(['-vv'])

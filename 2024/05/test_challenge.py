import pytest
from main import parse_input, part1, part2

EXAMPLE = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip()

def test_parse():
    a, b = parse_input(EXAMPLE)
    print(a)
    print(b)


def test_part1():
    result = part1(EXAMPLE)
    assert result == 143

def test_part2():
    result = part2(EXAMPLE)
    assert result == 123

if __name__ == '__main__':
    import os
    file_path = os.path.realpath(__file__)
    pytest.main([file_path, '-rP'])

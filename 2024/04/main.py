from typing import List, Tuple, Optional
import pathlib
from argparse import ArgumentParser
import pyperclip


def parse_input(txt: str) -> List[List[str]]:
    matrix = []
    for line in txt.split("\n"):
        matrix.append(list(line))
    return matrix

DIRECTIONS = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
    ]

def location_inbound(m, r, c, x, y):
    if r + x < 0: return False
    if r + x >= len(m): return False
    if c + y < 0: return False
    if c + y >= len(m[0]): return False
    return True

def check_around(m, r, c, ev, directions):
    for d in directions:
        x, y = d
        if not location_inbound(m, r, c, x, y):
            continue

        rr = r + x
        cc = c + y
        if m[rr][cc] == ev:
            return True
    return False

def drill_down(matrix, row, col, direction):
    total = 0
    r = row
    c = col
    for letter in 'MAS':
        if not check_around(matrix, r, c, letter, [direction]):
            break

        # Found a letter
        r = r + direction[0]
        c = c + direction[1]
        print(letter, end='')

    # Went through the loop, means we finished the word
    else:
        total += 1

    return total


def part1(txt: str) -> int:
    matrix = parse_input(txt)
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # Must start with X
            v = matrix[row][col]
            if v != 'X':
                continue

            # Check around to see if we see other letters in the right order and direction
            direction = DIRECTIONS
            for d in direction:
                total += drill_down(matrix, row, col, d)
    return total


def part2(txt: str) -> int:
    print(txt)
    return 0 


def main(args):
    function = [part1, part2]
    current_dir = pathlib.Path(__file__).parent.resolve()
    with open(current_dir / "input.txt", "r", encoding="utf-8") as f:
        result = function[args.p](f.read())
        pyperclip.copy(result)
        print(result)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--p", type=int, default=0)
    main(parser.parse_args())

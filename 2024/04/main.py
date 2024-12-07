from typing import List, Tuple, Optional
import pathlib
from argparse import ArgumentParser
import pyperclip


def parse_input(txt: str) -> List[List[str]]:
    matrix = []
    for line in txt.split("\n"):
        matrix.append(list(line))
    return matrix

def check_around(m, r, c, ev, direction=None)  -> Optional[Tuple[int, int]]:
    directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
    ]
    for d in directions:
        x, y = d
        if r + x < 0: continue
        if r + x >= len(m): continue
        if c + y < 0: continue
        if c + y >= len(m[0]): continue
        if direction is not None and d != direction:
            continue
        
        rr = r + x
        cc = c + y
        if m[rr][cc] == ev:
            return d

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
            direction = None
            r, c = (row, col)
            for letter in 'MAS':
                d = check_around(matrix, r, c, letter, direction)
                if d is None:
                    break

                # Found a letter
                direction = d
                r += d[0]
                c += d[1]
                print(letter, end='')

            # Went through the loop, means we finished the word
            else:
                total += 1

            print('')
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

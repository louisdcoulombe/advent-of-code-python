import pathlib
from argparse import ArgumentParser
import pyperclip
from itertools import cycle


def parse_input(txt: str):
    matrix = []
    for line in txt.split("\n"):
        matrix.append([x for x in line])
    return matrix

directions = ['N', 'E', 'S', 'W']
turn = cycle(directions)
move = {
        'N': lambda row, col: (row-1, col),
        'E': lambda row, col: (row, col+1),
        'S': lambda row, col: (row+1, col),
        'W': lambda row, col: (row, col-1),
}

def find_start(matrix):
    for row, _ in enumerate(matrix):
        for col, _ in enumerate(matrix):
            if matrix[row][col] == '^':
                return row, col
    assert False

def part1(txt: str, second='X') -> int:
    matrix = parse_input(txt)
    def is_outside(r, c):
        return r >= len(matrix) or c >= len(matrix[0]) or r < 0 or c < 0
    
    row, col = find_start(matrix)
    dir = 'N'
    previous = []
    while True:

        if matrix[row][col] == 'X':
            matrix[row][col] = second
            previous.append((row, col))
        else:
            matrix[row][col] = 'X'
            previous = []

        trow, tcol = move[dir](row, col)
        if is_outside(trow, tcol):
            break

        
        # Check if next move is a block, then turn
        if matrix[trow][tcol] == '#':
            print('turn', row, col)
            dir = next(turn)
            continue

        # Actual  movement
        row, col = move[dir](row, col)

    for row in matrix:
        print(''.join(row))

    return sum([m.count('X') for m in matrix])


def part2(txt: str) -> int:
    total = 0 
    for i in range(len(txt)):
        lst = list(txt)
        if lst[i] == "\n" or lst[i] == '^' or lst[i] == '#':
            continue

        lst[i] = '#'
        try: 
            part1(''.join(lst), 'Z')
        except:
            total += 1

    return total


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

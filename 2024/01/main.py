import pathlib
from argparse import ArgumentParser
import pyperclip


def parse_input(txt: str):
    left, right = [], []
    for line in txt.split("\n"):
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    return left, right


def part1(txt: str) -> int:
    a, b = parse_input(txt)
    a.sort()
    b.sort()

    return sum([abs(x - y) for x, y in zip(a,b)])


def part2(txt: str) -> int:
    a, b = parse_input(txt)
    return sum([x * b.count(x) for x in a])

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

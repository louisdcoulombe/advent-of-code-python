import pathlib
from argparse import ArgumentParser
import pyperclip


def parse_input(txt: str):
    res = {}
    for line in txt.split("\n"):
        a, b = line.split(':')
        res[int(a)] = [int(x) for x in b.split()]
    return res


def part1(txt: str) -> int:
    print(txt)
    return 0


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

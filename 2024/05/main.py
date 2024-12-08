from collections import defaultdict
import pathlib
from argparse import ArgumentParser
from typing import DefaultDict
import pyperclip


def parse_input(txt: str):
    rules = DefaultDict(list)
    updates = []
    for line in txt.split("\n"):
        if '|' in line:
            a, b = line.split('|')
            rules[int(a)].append(int(b))
            continue
        elif ',' in line:
            updates.append(list(map(int, line.split(','))))

    return rules, updates


def part1(txt: str) -> int:
    rules, updates = parse_input(txt)
    middles = []
    for update in updates:
        # print('='*20)
        for idx, v in enumerate(update, 1):
            valid = True
            # print(v)
            for r in rules.get(v, []):
                if r in update[:idx]:
                    valid = False

            if not valid:
                break
        else:
            middles.append(update[int(len(update)/2)])

    # print(middles)
    return sum(middles)


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

from typing import List
import pathlib
from argparse import ArgumentParser
import pyperclip


def parse_input(txt: str) -> List[List[int]]:
    rows = []
    for line in txt.split("\n"):
        rows.append([int(x) for x in line.split()])
    return rows





def oppositeSigns(x: int, y: int) -> bool:
    return (y >= 0) if (x < 0) else (y < 0);

def part1(txt: str) -> int:
    matrix = parse_input(txt)

    total = 0
    for lvl in matrix:
        total += verify_level(lvl)
    return total

def verify_level(lvl):
    print(lvl)
    total = 0
    previous = None
    for l, r in zip(lvl[:-1], lvl[1:]):
        print(lvl[-1], lvl[1:])
        current = l - r
        print(f'{current} = {l} - {r}')
        if abs(current) < 1 or abs(current) > 3:
            print(f'1 < {current} > 3')
            break

        if not previous:
            previous = current
            continue
        
        if oppositeSigns(current, previous):
            print(f'{current} <> {previous}')
            break
        
        previous = current
            
    else:
        total += 1
        print(f'total={total}')
    return total



def part2(txt: str) -> int:
    matrix = parse_input(txt)
    total = 0
    for lvl in matrix:
        if not verify_level(lvl):
            for i in range(len(lvl)):
                sub = lvl[:i] + lvl[i+1:]
                if verify_level(sub):
                    total += 1
                    break
        else:
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

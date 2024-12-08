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

def parse_input2(txt: str):
    rules = DefaultDict(list)
    updates = []
    for line in txt.split("\n"):
        if '|' in line:
            a, b = line.split('|')
            rules[int(b)].append(int(a))
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

# def move_after(lst, from_idx, to_idx):
#    # [a b c d e f g] -> [a b d e c f g]
#     return lst[:from_idx] + lst[from_idx+

def swap(lst, idx_a, idx_b):
    lst[idx_a], lst[idx_b] = lst[idx_b], lst[idx_a]

def part2(txt: str) -> int:
    rules, updates = parse_input(txt)
    print(rules)
    middles = []
    invalids = []
    for update in updates:
        for idx, v in enumerate(update, 1):
            valid = True
            for r in rules.get(v, []):
                if r in update[:idx]:
                    valid = False
                    break

            if not valid:
                invalids.append(update)
                break

    print(invalids)
    def fix_invalid(ups):
        print('-'*20)
        print(ups)
        for i in range(len(ups)):
            current = ups[i]
            if current not in rules:
                continue
            print(f'{current}: {rules[current]}')
            for r in rules[current]:
                if r in ups[:i]:
                    # Put current after r
                    swap(ups, lst.index(r), i)
                    # ups.insert(ups.index(r)+1, current)
                    # del ups[i]
                    print(ups)
        return ups

    valids = list(map(fix_invalid, invalids))
    print('='*20)
    print(valids)

    total = 0
    for v in valids:
        total += v[int(len(v)/2)]
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

from itertools import zip_longest
import re
import pathlib
from argparse import ArgumentParser
import pyperclip



def part1(txt: str) -> int:
    print(txt)
    regex = re.compile(r'(mul\((\d{1,3}),(\d{1,3})\))')
    total = 0
    for g in  regex.finditer(txt):
        l, r = g.groups()[1:]
        total += int(l) * int(r)

    return total


def part2(txt: str) -> int:
    # Find the locationz where there is do()
    do_regex = re.compile(r'do\(\)')
    dont_regex = re.compile(r"don\'t\(\)")
    section = [(0, 'on')]
    for g in  do_regex.finditer(txt):
        section.append((g.span()[0], 'on'))

    for g in  dont_regex.finditer(txt):
        section.append((g.span()[-1], 'off'))

    section.sort(key=lambda x: x[0])
    print(section)
    


    total = 0
    started = None
    for i, s in enumerate(section):
        print(f'SECTION {i} >> ', end='')
        if s[1] == 'off' and started is not None:
            total += part1(txt[started:s[0]])
            started = None
            print('>> stopped')
            continue
        
        if s[1] == 'on' and started is not None:
            print(' already on')
            continue

        if s[1] == 'off':
            print(' already off')
            started = None
        else:
            print(' started!')
            started = s[0]

    if started:
        print(' fill the end')
        total += part1(txt[started:])

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

import json
from functools import cmp_to_key
from math import prod

from day13.part_one import compare
from utils import load_input


def solve():
    divider_packet1 = [[2]]
    divider_packet2 = [[6]]
    packets = [divider_packet1, divider_packet2] + \
              [json.loads(line) for line in load_input().splitlines() if line]

    packets.sort(key=cmp_to_key(compare))
    print(packets)
    print(prod(
        [
            index
            for index, packet in enumerate(packets, start=1)
            if packet == divider_packet1 or packet == divider_packet2
        ]
    ))


if __name__ == '__main__':
    solve()

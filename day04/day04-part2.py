import sys
import io

numoverlaps = 0

with open('day04\\input.txt') as f:
    for line in f:
        (grp1, grp2) = line.strip().split(',')
        (rng1_1, rng1_2) = grp1.split('-')
        (rng2_1, rng2_2) = grp2.split('-')

        set1 = set(range(int(rng1_1), int(rng1_2) + 1))
        set2 = set(range(int(rng2_1), int(rng2_2) + 1))

        if not set1.isdisjoint(set2):
            numoverlaps += 1

print(f'numoverlaps: {numoverlaps}')

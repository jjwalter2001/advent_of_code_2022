import sys
import io

priorities = 0

def score_item(ch):
    # If lowercase, then convert to 1-26
    if ord(ch) > 96:
        return ord(ch) - 96
    else:
        # if uppercase, convert to 27-52
        return ord(ch) - 65 + 27

# Iterate through the input, splitting each line in half
# Then find the common letter between both halves
# and convert it to the priority value
with open('day03\\input.txt') as f:
    for line in f:
        line = line.strip()

        first = line[0: int(len(line)/2)]
        second = line[int(len(line)/2): len(line)]

        common = set(first).intersection(second)

        for ch in common:
            priorities += score_item(ch)

print(priorities)

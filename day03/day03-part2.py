import sys
import io

priorities = 0
group = []

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
        group.append(line.strip())

        # If this is the third elf of the group, then
        # we can figure out the overlapping item
        if len(group) == 3:
            common = set(group[0]).intersection(group[1]).intersection(group[2])

            for ch in common:
                priorities += score_item(ch)

            # And reset the group for the next go-around
            group = []

print(priorities)

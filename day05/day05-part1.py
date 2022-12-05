import sys
import io

# This dictionary will be keyed on the stack number
# and contain a list which operates as a stack (i.e. push/pop)
stacks = {}
# This lookup table holds the column number of each stack in the input
pos = {1: 1, 2: 5, 3: 9, 4: 13, 5: 17, 6: 21, 7: 25, 8: 29, 9: 33}
blank = False


def move_crates(mvmt):
    # Split the move command by spaces and then grab the relevant components
    flds = mvmt.strip().split(' ')
    num_crates = int(flds[1])
    from_st = int(flds[3])
    to_st = int(flds[5])

    for x in range(1, num_crates + 1):
        # Sloppily using global variables here...
        stacks[to_st].append(stacks[from_st].pop())

    return None

with open('day05\\input.txt') as f:
    for line in f:
        if line == '\n':
            continue

        # The current stack definition is until we get to the blank line
        if line.startswith(' 1'):
            blank = True

            # Once we get here, we're done building the stacks, so
            # just need to reverse them to get them into proper order
            for st in stacks.keys():
                stacks[st].reverse()

            continue

        if not blank:
            # We can assume clean input and each stack is in specific columns...
            # If the stack has a value there, then add it to our list
            for st in pos.keys():
                if (line[pos[st]] != ' '):
                    if not st in stacks:
                        stacks[st] = list()
                    stacks[st].append(line[pos[st]])

        else:
            # Process a move command
            move_crates(line)


for x in range(1, 10):
    print(f'stack {x}: {" " if len(stacks[x])==0 else stacks[x].pop()}')

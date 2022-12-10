# Current CPU clock cycle number
cpucycle = 0
# Current X register value
xreg = 1

# This will be a dictionary that is keyed on the
# CPU  cycle number with the then current X register value
savedcycles = {}


# This just processes a single CPU cycle and decides whether
# we need to save the info
def process_cycle():
    global cpucycle
    global savedcycles
    global xreg

    cpucycle += 1

    if cpucycle in [20, 60, 100, 140, 180, 220]:
        savedcycles[cpucycle] = xreg
    


def execute_cmd(line):
    global cpucycle
    global xreg

    if line == 'noop':
        process_cycle()
    else:
        (cmd, val) = line.split(' ')
        process_cycle()
        process_cycle()
        xreg += int(val)


with open('day10\\input.txt') as f:
    cpucycle = 0
    for line in f:
        line = line.strip()
        execute_cmd(line)

# Iterate through the directories, calculating the size of each
final = 0
for d in savedcycles.keys():
    final += d * savedcycles[d]

print(final)

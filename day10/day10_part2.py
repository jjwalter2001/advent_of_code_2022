# Current CPU clock cycle number
cpucycle = 0
# Current X register value
xreg = 1


# This just processes a single CPU cycle and decides whether
# we need to save the info
def process_cycle():
    global cpucycle
    global savedcycles
    global xreg

    if cpucycle == 6:
        a=1

    pixloc = cpucycle % 40

    if pixloc in [xreg-1, xreg, xreg+1]:
        print('#', end='')
    else:
        print('.', end='')

    cpucycle += 1

    if cpucycle in [40, 80, 120, 160, 200, 240]:
        print('')


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


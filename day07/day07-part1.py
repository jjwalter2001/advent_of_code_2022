
# this string holds our current location in the hierarchy
# represented as a standard path - e.g. /fgtvzpl/ftqs
loc = ''
# This dictionary just holds our running size total for each
# directory we encounter
dirsizes = {}


def execute_cd(line, loc):
    # Two options here - either we cd into a new directory (append the directory name)
    # or we move back a level with the ..
    if line == "$ cd ..":
        return loc[0: loc.rindex('/')]
    else:
        newdir = line.split(' ')[2]
        if newdir == '/':
            return '/root'
        else:
            return f'{loc}/{newdir}' if not loc.endswith('/') else f'{loc}{newdir}'


def inc_counter(ds, loc, sz):
    if loc == '':
        return

    if loc not in ds.keys():
        ds[loc] = 0
    ds[loc] += sz
    inc_counter(ds, loc[0: loc.rindex('/')], sz)


with open('day07\\input.txt') as f:
    for line in f:
        line = line.strip()
        if line.startswith('$'):
            # This means a command was executed....
            # And the only command we really care about is the cd
            if line.startswith('$ cd'):
                loc = execute_cd(line, loc)
            elif line.startswith('$ ls'):
                # we can just ignore the ls commands
                continue
        elif line.startswith('dir'):
            # we can ignore dir listings
            continue
        else:
            # Otherwise we have a file with a size
            # Increment that directory counter - and each
            # of the parent directories
            (sz, fn) = line.split(' ')
            inc_counter(dirsizes, loc, int(sz))

# Iterate through the directories, calculating the size of each
finalsize = 0
for d in dirsizes.keys():
    if dirsizes[d] <= 100000:
        finalsize += dirsizes[d]

print(finalsize)

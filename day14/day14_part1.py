import numpy as np

CAVE_MAX_X = 600
CAVE_MAX_Y = 600

class Cave:
    class Grain:
        y = 500
        x = 0

        def move(self, cave):
            # Given my current location see if I can move in any of the approved directions
            # Returns:  True if we can move
            #           False if we cannot
            #           None if we drop off the bottom of the array
            # If dropping another level takes us off the array, then end
            if self.x+1 >= CAVE_MAX_X:
                return None
            # Try dropping down one spot
            if cave[self.x+1, self.y] == '.':
                self.x += 1
                return True
            # Now try down one and left one
            if cave[self.x+1, self.y-1] == '.':
                self.x += 1
                self.y -= 1
                return True
            # Now, down one and right one
            if cave[self.x+1, self.y+1] == '.':
                self.x += 1
                self.y += 1
                return True
            # Otherwise we've settled where we belong
            return False

    cave = np.full([CAVE_MAX_X, CAVE_MAX_Y], '.', dtype=str)
    numgrains = 0

    def display_cave(self):
        print(f'Number of grains: {self.numgrains}')
        for x in self.cave:
            for y in x:
                print(x[y], end='')
            print()

    def process_coords(self, start, stop):
        (y1, x1) = map(int, start.split(','))
        (y2, x2) = map(int, stop.split(','))

        if x1 < x2:
            for x in range(x1, x2+1):
                self.cave[x, y1] = 'X'
        if x1 > x2:
            for x in range(x2, x1+1):
                self.cave[x, y1] = 'X'
        if y1 < y2:
            for y in range(y1, y2+1):
                self.cave[x1, y] = 'X'
        if y1 > y2:
            for y in range(y2, y1+1):
                self.cave[x1, y] = 'X'

        return None

    def run_to_full(self):
        cave_is_full = False

        while not cave_is_full:
            if self.numgrains == 24:
                a = 1
            # Add new grain of sand
            grain = self.Grain()
            result = grain.move(self.cave)
            while result:
                # Iterate though until it comes to a rest -
                # unless it drops off the bottom of the array - in which
                # case we're done

                result = grain.move(self.cave)
                if result == None:
                    cave_is_full = True
            
            # Mark its final location
            if not cave_is_full:
                self.cave[grain.x, grain.y] = 'o'
                self.numgrains += 1
            #self.display_cave()

final = 0

input = open('day14/input.txt').readlines()

elf_cave = Cave()

# ctr is the line counter as we iterate through the input
ctr = 0
while ctr < len(input):
    coords = input[ctr].split(' -> ')
    for i in range(0, len(coords)-1):
        elf_cave.process_coords(coords[i], coords[i+1])

    ctr += 1

elf_cave.run_to_full()

print(f'Total number of grains in the cave: {elf_cave.numgrains}')

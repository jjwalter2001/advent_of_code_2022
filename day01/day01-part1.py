import sys
import io

maxtotal = 0
subtotal = 0

with open('input.txt') as f:
    for line in f:
        if line == "\n":
            if subtotal > maxtotal:
                maxtotal = subtotal
            subtotal = 0
        else:
            subtotal += int(line)

print(maxtotal)

import sys
import io

maxtotals = []
subtotal = 0

with open('input.txt') as f:
    for line in f:
        if line == "\n":
            if len(maxtotals) < 3:
                maxtotals.append(subtotal)
            elif any(i < subtotal for i in maxtotals):
                maxtotals.remove(min(maxtotals))
                maxtotals.append(subtotal)

            subtotal = 0
        else:
            subtotal += int(line)

print(maxtotals)
print(sum(maxtotals))
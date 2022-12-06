import sys
import io

f = open('day06\\input.txt')
signal = f.read()

# Find the first range of 14 unique characters
for x in range(0, len(signal)):
    if len(set(signal[x: x+14])) == 14:
        print(x + 14)


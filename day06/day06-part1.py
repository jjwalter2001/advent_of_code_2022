import sys
import io

f = open('day06\\input.txt')
signal = f.read()

# Find the first range of 4 unique characters
for x in range(0, len(signal)):
    if len(set(signal[x: x+4])) == 4:
        print(x + 4)


import ast
from functools import cmp_to_key

# This will recursively dig though the left and right lists - until
# either one list is empty or both values are integers
# It uses idx to keep track of how far into each list it is
def isin_order(left, right):
    # end cases
    if type(left) == int and type(right) == int:
        return None if left == right else -1 if left <= right else 1

    if type(left) == list and type(right) != list:
        right = [right]
    if type(left) != list and type(right) == list:
        left = [left]

    for idx in range(0, max(len(left), len(right))):
        if idx >= len(left):
            return -1
        if idx >= len(right):
            return 1
        ret = isin_order(left[idx], right[idx])
        if not ret is None:
            return ret

    return None

final = 0

input = open('day13/input.txt').readlines()

# ctr is the line counter as we iterate through the input
ctr = -1
# Put all of the packets in a list, then sort that list using the isin_order() function
# Seeding this list with the two divider packets
packets = [[[6]], [[2]]]

while ctr < len(input) - 1:
    ctr += 1
    if input[ctr] == '\n':
        continue
    packet = ast.literal_eval(input[ctr].strip())
    packets.append(packet)
   
sorted_p = sorted(packets,key=cmp_to_key(isin_order))

idx = 1
idx1 = 0
idx2 = 0
for packet in sorted_p:
    if packet == [[2]]:
        idx1 = idx
    if packet == [[6]]:
        idx2 = idx
    idx += 1
    
print(idx1 * idx2)

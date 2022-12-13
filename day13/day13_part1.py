import ast

# This will recursively dig though the left and right lists - until
# either one list is empty or both values are integers
# It uses idx to keep track of how far into each list it is
def isin_order(left, right):
    # end cases
    if type(left) == int and type(right) == int:
        return None if left == right else left <= right

    if type(left) == list and type(right) != list:
        right = [right]
    if type(left) != list and type(right) == list:
        left = [left]

    for idx in range(0, max(len(left), len(right))):
        if idx >= len(left):
            return True
        if idx >= len(right):
            return False
        ret = isin_order(left[idx], right[idx])
        if not ret is None:
            return ret

    return None

final = 0

input = open('day13/input.txt').readlines()

# ctr is the line counter as we iterate through the input
ctr = 0
# idx is the order in which we encounter each set of packets
idx = 0
while ctr < len(input):
    left = ast.literal_eval(input[ctr].strip())
    right = ast.literal_eval(input[ctr + 1].strip())
    idx += 1
    ctr += 3

    if isin_order(left, right):
        final += idx

print(final)

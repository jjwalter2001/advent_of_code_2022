
# This will be a dictionary that is keyed on the
# monkey number and contains a Monkey object
monkeys = {}

class Monkey:
    # This is the items the monkey currently has, where each
    # item is an integer representing the 'worry level'
    items = []

    # The divisor used for the test
    divisor = 0

    # This is the operation to perform when inspecting an item
    operator = ''
    # This is the operand used for that operation...where a -1
    # would represent the value of the original item
    operand = 0

    # After parsing, these will become the Monkey objects
    # that we throw to.  This initially gets set to the numeric
    # value of the monkey
    throw_to_true = None
    throw_to_false = None

    # Number of times this monkey inspected something
    inspection_cnt = 0

    def __init__(self, x, input):
        # When this gets called, f would have just proviede the 'Money x:' header line,
        # so we can just parse the next five lines to define the rest of the monkey...

        self.items = input[x].split(':')[1].split(',')
        self.items = [int(x.strip()) for x in self.items]
        operation = input[x+1].split('=')
        (_, self.operator, operand) = operation[1].strip().split(' ')
        self.operand = -1 if operand == 'old' else int(operand)

        self.divisor = int(input[x+2].split(' ')[3])

        self.throw_to_true = int(input[x+3].split(' ')[5])
        self.throw_to_false = int(input[x+4].split(' ')[5])

    def my_turn(self, scaling):
        # Make a copy of the item list to iterate through
        # so our loop doesn't get messed up with remove items
        for item in self.items[:]:
            self.inspect_item(item, scaling)
            self.items.remove(item)

    def set_catchers(self, monkeys):
        self.throw_to_true = monkeys[self.throw_to_true]
        self.throw_to_false = monkeys[self.throw_to_false]

    def inspect_item(self, item, scaling):
        self.inspection_cnt += 1
        # Worry level increases because of the inspection
        item = self.operation(item)
        # Then divide by three, dropping the remainder, because the item wasn't damaged
        # Removed for part 2
        # item = int(item / 3)
        # Use the scaling factor to keep the numeric value from getting out of control
        item = item % scaling
        # Now test it to see if it needs to be thrown...
        if self.test(item):
            self.throw_to_true.catch_item(item)
        else:
            self.throw_to_false.catch_item(item)
        
    def catch_item(self, item):
        self.items.append(item)
        
    def operation(self, item):
        operand = item if self.operand == -1 else self.operand

        if self.operator == '+':
            return item + operand
        elif self.operator == '-':
            return item - operand
        elif self.operator == '*':
            return item * operand
        elif self.operator == '/':
            return int(item / operand)

    def test(self, item):
        return not item % self.divisor
    

f = open('day11\\input.txt')
input = f.readlines()
input = [x.strip() for x in input]

x = 0
scaling = 1
while x < len(input):
    if input[x].startswith('Monkey'):
        monkey_num = int(input[x].split(' ')[1].split(':')[0])
        monkeys[monkey_num] = Monkey(x+1, input)
        scaling *= monkeys[monkey_num].divisor
    x += 1

# With the monkeys loaded, we need to go back and update each for the throwing
for monkey in monkeys.keys():
    monkeys[monkey].set_catchers(monkeys)

# Now, execute each of the rounds
for round in range(0, 10000):
    if round % 100 == 0:
        print(round)
    for monkey in range(0, len(monkeys)):
        monkeys[monkey].my_turn(scaling)

inspections = [monkeys[x].inspection_cnt for x in monkeys.keys()]
inspections.sort(reverse=True)
# Iterate through the directories, calculating the size of each
final = inspections[0] * inspections[1]

print(final)

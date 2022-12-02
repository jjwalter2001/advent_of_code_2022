import sys
import io

shapes = {'X': 1,
          'Y': 2,
          'Z': 3}

scores = { 'A': { 'X': 3,
                  'Y': 6,
                  'Z': 0},
           'B': { 'X': 0,
                  'Y': 3,
                  'Z': 6},
           'C': { 'X': 6,
                  'Y': 0,
                  'Z': 3}
         }

score = 0
with open('day02\\input.txt') as f:
    for line in f:
        (them, me) = line.strip().split(' ')

        score += shapes[me]

        score += scores[them][me]

print(score)

import sys
import io

# X = need to lose
# Y = draw
# Z = win

# This is to get my score from the shape I'd have to select
# in order to either win/lose/draw, based on the XYZ value
shapes = { 'X': { 'A': 3,
              'B': 1,
              'C': 2},
       'Y': { 'A': 1,
              'B': 2,
              'C': 3},
       'Z': { 'A': 2,
              'B': 3,
              'C': 1
            }
     }

# These are the scores I get for either win/lose/draw
scores = {'X': 0,
          'Y': 3,
          'Z': 6}


score = 0
with open('day02\\input.txt') as f:
    for line in f:
        (them, me) = line.strip().split(' ')

        score += scores[me]

        score += shapes[me][them]

print(score)

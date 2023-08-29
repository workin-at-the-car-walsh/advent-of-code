import os
import requests

"""
Advent of code
2022
Day 2

Rock (A)(X) Paper (B)(Y) Scissors (C)(Z)
score of selection 1, 2, 3
0 loss
3 draw
6 win

a, b = a + (result)

1+1 = 3
1+2 = 0
1+3 = 6

2+1 = 6
2+2 = 3
2+3 = 0

3+1 = 0
3+2 = 6
3+3 = 3
"""

input_link = "https://adventofcode.com/2022/day/2/input"
input_file = "puzzle_input_2022_2"

if not os.path.exists(os.getcwd() + "/" + input_file):

    print('downloading puzzle input')
    # inspect network tab in developer tools and find Cookie header
    # save "session=askljdnjad" as AOC environment variable
    token = os.environ.get("AOC")
    headers = {"Cookie": token}
    x = requests.get(input_link, headers=headers)

    puzzle_input = x.text

    with open(input_file, "w") as f:
        f.write(puzzle_input)
        f.close()

else:
    print("input file already exists, continuing")

with open(input_file, "r") as f:
    match_lines = f.readlines()
    f.close()

match_list = [x.split() for x in match_lines]

def map_to_numbers(x):
    opponent = ["A", "B", "C"]
    player = ["X", "Y", "Z"]
    return [opponent.index(x[0]) + 1, player.index(x[1]) + 1]

def calc_result(x):
    return [x[1], 3*(x[1]-x[0]+1)]

# m = map(map_to_numbers, test)

m = map(map_to_numbers, match_list)
num_list = list(m)

m1 = map(calc_result, num_list)
result_list = list(m1)

# edit result values for those that fall outside
# the general formula
match_scores = [0 + x[0] if x[1]==9 
                else 6 + x[0] if x[1]==-3
                else x[1] + x[0] 
                for x in result_list]

# solution answer
sum(match_scores)

"""
Part 2
"""

def calc_decision(x):
    # x[0] = opponent, x[1] = result
    return [int((x[1]/3)+x[0]-1), x[1]] # [player choice, result score(raw)]

def map_to_numbers_p2(x):
    # [opponent letter, result letter]
    # X = 0, Y = 3, Z = 6
    opponent = ["A", "B", "C"]
    match_result = ["X", "Y", "Z"]
    return [opponent.index(x[0]) + 1, match_result.index(x[1]) * 3]

#m2 = map(map_to_numbers_p2, test)
m2 = map(map_to_numbers_p2, match_list)
num_list_p2 = list(m2)

m3 = map(calc_decision, num_list_p2)
result_list_p2 = list(m3)
# list of player choice and result

# edit raw choice values for results that fall outside
# the standard formula
match_scores_p2 = [3 + x[1] if x[0]==0 
                    else 1 + x[1] if x[0]==4
                    else x[1] + x[0] 
                    for x in result_list_p2]

# solution answer
sum(match_scores_p2)

"""
Closing thoughts

There is definitely a better way to do this, I found through
a pen and notepad a formula that can get you to the correct result
score or required player choice 7/9 times. Which lead to the adjustment
of raw values in the very last transformation. Perhaps there is a 100%
accurate forumla or some way to do a vectorised algorithm that outputs the
correct result.

"""


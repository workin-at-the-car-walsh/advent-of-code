import requests
import os
import re

input_link = "https://adventofcode.com/2022/day/5/input"
input_file = "puzzle_input_2022_5"

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

"""
Advent of code 2022 day 5



"""
with open(input_file, "r") as f:
    lines = f.readlines()
    f.close()

raw_stacks = lines[:9]
raw_moves = lines[10:]

stacks = []
for i in range(1,10):
    stack = []
    indx = raw_stacks[8].find(str(i))
    stack = [char[indx] for char in raw_stacks[:8] if (char[indx] != ' ')][::-1]
    stacks.append(stack)

#for part 2
stacks2 = stacks

    
for move in raw_moves:
    integers = re.findall(r'\d+', move)
    m = [int(number) for number in integers[:3]]
    # move 4 from 9 to 1
    # pop 4 from 9, append to 1
    for i in range(1,m[0]+1):
        a = stacks[m[1]-1].pop()
        stacks[m[2]-1].append(a)

res = '' 
for stack in stacks:
    res += stack[-1]
#part 1 solution
print(res)

#part 2 solution
for move in raw_moves:
    integers = re.findall(r'\d+', move)
    m = [int(number) for number in integers[:3]]
    # move 4 from 9 to 1 -> [4, 9, 1]
    # pop 4 from 9, append to 1
    a = [stacks2[m[1]-1].pop() for i in range(1,m[0]+1)]
    stacks2[m[2]-1].extend(a[::-1])

res2 = '' 
for stack in stacks2:
    res2 += stack[-1]

#part 1 solution
print(res2)
import requests
import os

input_link = "https://adventofcode.com/2022/day/6/input"
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
    line = f.readlines()[0].strip("\n")
    f.close()

start_index = None

for idx in range(0, len(line)):
    if len(set([a for a in line[idx:idx+4]])) == 4:
        # print(set([a for a in line[idx:idx+4]]))
        start_index = idx+4
        break

print(start_index)

start_index2 = None

for idx in range(0, len(line)):
    if len(set([a for a in line[idx:idx+14]])) == 14:
        # print(set([a for a in line[idx:idx+4]]))
        start_index2 = idx+14
        break

print(start_index2)
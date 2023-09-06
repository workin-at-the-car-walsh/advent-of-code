import requests
import os

input_link = "https://adventofcode.com/2022/day/4/input"
input_file = "puzzle_input_2022_4"

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
Advent of code 2022 day 4

Find pairs where one completely overlaps the other

67-84,66-87

17, 17

"""
with open(input_file, "r") as f:
    lines = f.readlines()
    f.close()

count = 0
count2 = 0
for i in lines:
    pair = i.replace("\n", "").split(",")
    set1 = set(range(int(pair[0].split("-")[0]), int(pair[0].split("-")[1])+1))
    range2 = range(int(pair[1].split("-")[0]), int(pair[1].split("-")[1])+1)
    min_length = min([len(set1), len(range2)])
    #print(min_length)
    overlap = set1.intersection(range2)
    #print(len(overlap))
    if len(overlap) == min_length:
        count += 1
    if len(overlap) > 0:
        count2 += 1

#part 1 solution
print(count)

#part2 solution
print(count2)





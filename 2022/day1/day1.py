import requests
import os

"""
Calorie Counting
Advent of code y=2022 day=1
"""

input_link = "https://adventofcode.com/2022/day/1/input"
input_file = "puzzle_input.txt"

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
Each item contains number of calories
Each line represents an item
Each blank line seperates an elf
"""

class Elf:
    def __init__(self, items):
        self.inventory = []
        self.inventory = [int(i) for i in items]
    
    def total_calories(self):
        return sum(self.inventory)

elf_list = []

with open(input_file, "r") as f:
    item_list = f.readlines()
    f.close()

# using list comprehension Split list into lists by particular value
#test_list = item_list[:30]

size = len(item_list)
# list of indexes representing the blank lines index + 1
idx_list = [idx + 1 for idx, val in
			enumerate(item_list) if len(val) <= 1 ]

# zip creates a list of tuples representing the indexes to
# split the list with
res = [item_list[i: j] for i, j in
	zip([0] + idx_list, idx_list +
		([size] if idx_list[-1] != size else []))]

res1 = []
for elf in res:
    elf_items = []
    for item in elf:
        if item != "\n":
            elf_items.append(item.replace("\n", ""))
    res1.append(elf_items)

#print("The list after splitting by a value : " + str(res1))
elves = []
for elf_items in res1:
    elf = Elf(elf_items)
    elves.append(elf)

cal_totals = [x.total_calories() for x in elves]

most_cals = max(cal_totals)

print(most_cals)

"""
Part 2
"""
import heapq

top_three = heapq.nlargest(3, cal_totals)
print(sum(top_three))

"""
Closing thoughts

Probably overkill with the Elf class, as
this was my first AOC I thought the problems would build on
each other and we would need to extend day1 code throughout
I seem to be wron at the time of writing (day2)
"""


        




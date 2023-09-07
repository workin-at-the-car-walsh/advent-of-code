import requests
import os

input_link = "https://adventofcode.com/2022/day/7/input"
input_file = "puzzle_input_2022_7"

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
test = 'sample_commands'
with open(input_file, "r") as f:
    lines = f.readlines()
    f.close()

location = []
d_size = {}
d_name = {}
for line in lines:
    if line[0] == '$':
        # command
        if line[2] == 'c':
            #changing dir
            if line.strip("\n")[-2:] != "..":
                # add current dir to state
                location.append(line.strip("\n").split("cd ")[1])
            else:
                #remove current dir from lcoation
                location.pop()
            #print(location)
        elif line[2] == 'l':
            # list dir, nothing to do
            pass
    else:
        for idx, dir in enumerate(location):
            full_dir = "-".join(location[:idx+1])
            if full_dir not in d_size:
                d_size[full_dir] = []
            size = line.split(" ")[0]
            (d_size[full_dir].append(int(size)) if size != 'dir' else None)
"""
if a directory has a parent directory of the same name
it will return the wrong index
added enumerate to fix
"""


grand_total = 0
result_l = []
for dir, files in d_size.items():
    # print(dir)
    # print(files)
    total = sum(files)
    if total <= 100000:
        grand_total += total
    result_l.append([dir, total])

#answer part 1
print(grand_total)

required_space = 30000000
total_space = 70000000
space_to_free = required_space - (total_space - result_l[0][1])

print("space to free up is :")
print(space_to_free)

winner = ["blank", 10000000000]
candidates = []
for dir in result_l:
    if dir[1] > space_to_free:
        candidates.append(dir)
        if dir[1] < winner[1]:
            winner = dir
# answer part 2
print(winner)
# with open("res", "w") as f:
#     f.write(str(result_l))
#     f.close()

# # test total size
# t = []
# for line in lines:
#     c = line.split(" ")[0]
#     try:
#         n = int(c)
#         t.append(n)
#     except ValueError:
#         # Handle the case where the string is not a valid number
#         pass

# print(sum(t))
    
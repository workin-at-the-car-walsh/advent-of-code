import requests
import os

input_link = "https://adventofcode.com/2022/day/3/input"
input_file = "puzzle_input_2022_3"

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
Advent of Code
2022
Day 3
a->z : 1->26
A->Z : 27->52

ord : lower - 96
ord : upper - 38

"""


testfile = 'test'
with open(input_file, "r") as f:
    lines = f.readlines()
    f.close()

newlist = []
for i in lines:
    quotient, remainder = divmod(len(i), 2)
    newlist.append([i[:quotient],i[quotient:].replace("\n","")])

ele_list = []
for i in newlist:
    ele_list.append(list(set(i[0]).intersection(i[1]))[0])

pri_list = []
for i in ele_list:
    if i.isupper():
        pri_list.append(ord(i) - 38)
    else:
        pri_list.append(ord(i) - 96)

print(sum(pri_list))   

"""
part 2
"""
count = 0
groups = []
for group in range(0, len(lines),3):
    count += 1
    l = lines[group:group+3]
    groups.append(list(map(lambda x: x.replace('\n',''), l)))

badges = []
for group in groups:
    badges.append(list(set(group[0]).intersection(group[1], group[2]))[0])

pri_list_p2 = []
for i in badges:
    if i.isupper():
        pri_list_p2.append(ord(i) - 38)
    else:
        pri_list_p2.append(ord(i) - 96)

# solution answer
sum(pri_list_p2)

"""
Closing thoughts

A lot of list iteration, creating a lot of lists could get memory intensive

putting the loading of input data to a common function that can be
imported would neaten things up a bit

After day2 I looked at some online solutions and some of them inspired me
to not worry about the most efficient or least lines of code, as long as its
readable, works and easy to follow. Other solutions were kind of awesome and
made me want to keep practicing so I can learn from them
"""
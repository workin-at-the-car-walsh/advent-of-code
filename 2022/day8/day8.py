import requests
import os
import numpy as np

input_link = "https://adventofcode.com/2022/day/8/input"
input_file = "puzzle_input_2022_8"

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
test = 'test'
with open(input_file, "r") as f:
    lines = f.readlines()
    f.close()

grid = [list(line.strip("\n")) for line in lines]

#array representing grid
a = np.array(grid, dtype=int)
#zeros, representing trees not visible, init all
z = np.empty_like(a)

# will iterate over every single element
it = np.nditer([a, z], flags=['multi_index'], op_flags=['readwrite', 'allocate'])
for x, y in it:
    r_idx = it.multi_index[0]
    c_idx = it.multi_index[1]
    # check if row has a bigger tree
    # after = [row_index, col_idx+1:]
    # before = [row_index, :col_idx]
    before_row = np.copy(a[r_idx, :c_idx])
    after_row = np.copy(a[r_idx, c_idx+1:])
    brm = np.append(before_row, 0).max()
    arm = np.append(after_row, 0).max()
    del after_row
    del before_row
    # check if column has a bigger tree
    # after = [r_idx+1:, c_idx]
    # before = [:r_idx, c_idx]
    before_col = np.copy(a[r_idx+1:, c_idx])
    after_col = np.copy(a[:r_idx, c_idx])
    bcm = np.append(before_col, 0).max()
    acm = np.append(after_col, 0).max()
    del before_col
    del after_col

    if any(x > value for value in [brm,arm,bcm,acm]):
        y[...] = 1
    else:
        y[...] = 0
    del brm, arm, bcm, acm
    
        

z = it.operands[1]
z[0] = 1
z[-1] = 1
z[:, 0] = 1
z[:, -1] = 1
#print(z)
print(np.sum(z == 1))

"""
numpy has a lot of little tricks

no idea whether this is more powerful than
list operations if this problem was to scale

"""
z2 = np.empty_like(a)

winner = 0
it2 = np.nditer([a, z2], flags=['multi_index'], op_flags=['readwrite', 'allocate'])
for x, y in it2:
    r_idx = it2.multi_index[0]
    c_idx = it2.multi_index[1]
    # check if row has a bigger tree
    # after = [row_index, col_idx+1:]
    # before = [row_index, :col_idx]
    before_row = np.copy(a[r_idx, :c_idx])[::-1]
    br_score = 1
    for tree in before_row[:-1]:
        if tree < x:
            br_score += 1
        else:
            break
    after_row = np.copy(a[r_idx, c_idx+1:])
    ar_score = 1
    for tree in after_row[:-1]:
        if tree < x:
            ar_score += 1
        else:
            break
    del after_row
    del before_row
    # check if column has a bigger tree
    # after = [r_idx+1:, c_idx]
    # before = [:r_idx, c_idx]  # a[1:, 1][::-1]
    before_col = np.copy(a[:r_idx, c_idx])[::-1]
    bc_score = 1
    for tree in before_col[:-1]:
        if tree < x:
            bc_score += 1
        else:
            break
    after_col = np.copy(a[r_idx+1:, c_idx]) #np.copy(a[:r_idx, c_idx])
    ac_score = 1
    for tree in after_col[:-1]:
        if tree < x:
            ac_score += 1
        else:
            break
    del before_col
    del after_col
    score = br_score*ar_score*bc_score*ac_score
    y[...] = score
    
    if score > winner:
        winner = score
        print(br_score, ar_score, bc_score, ac_score)
        print(score)
        print(r_idx, c_idx)
    del score
    del br_score, ar_score, bc_score, ac_score

print(winner)

"""
the code doesnt remove the efge trees from consideration
but it is unlikely one of them will have
the best score so it doesnt matter for this problem
"""
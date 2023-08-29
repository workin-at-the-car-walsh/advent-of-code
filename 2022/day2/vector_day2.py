import numpy as np
input_file = "puzzle_input_2022_2"

with open(input_file, "r") as f:
    match_lines = f.readlines()
    f.close()

match_list = [x.split() for x in match_lines]

# opponent
y = np.array([[0],[0],[1]])

# score matrix
M = np.array([[3,0,6],[6,3,0],[0,6,3]])

# your choice
x = np.array([[1],[0],[0]])

# score of match
v = (y.T)*M*x
print(np.sum(np.argmax(y == 1, axis=0))) # score of choice
print(np.sum(v)) # score of match
f = lambda x: ('  BXCYAZAXBYCZCXAYBZ'.index(x[0]+x[2]),
               '  BXCXAXAYBYCYCZAZBZ'.index(x[0]+x[2]))

print(*[sum(x)//2 for x in zip(*map(f, open('puzzle_input_2022_2')))])
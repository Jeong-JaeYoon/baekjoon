table = [list(map(int, input().split())) for i in range(9)]

max_val = 0
max_row, max_col = 0, 0

for i in range(9):
    for j in range(9):
        if max_val <= table[i][j]:
            max_val = table[i][j]
            max_row = i + 1
            max_col = j + 1

print(max_val)
print(max_row, max_col)
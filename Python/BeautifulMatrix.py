matrix = []
for e in range(5):
    matrix.append(list(map(int, input().split())))
index_lin = 0
index_col = 0
found = False
while index_lin < 5:
    while index_col < 5:
        if matrix[index_lin][index_col] == 1:
            found = True
            break
        index_col += 1
    if found:
        break
    index_col = 0
    index_lin += 1
print(abs(index_col - 2) + abs(index_lin - 2))

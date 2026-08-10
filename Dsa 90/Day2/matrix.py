rows = 3
cols = 3

matrix = []

print("Enter matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Top Row
for j in range(cols):
    print(matrix[0][j], end=" ")

# Right Column
for i in range(1, rows):
    print(matrix[i][cols - 1], end=" ")

# Bottom Row
for j in range(cols - 2, -1, -1):
    print(matrix[rows - 1][j], end=" ")

# Left Column
for i in range(rows - 2, 0, -1):
    print(matrix[i][0], end=" ")
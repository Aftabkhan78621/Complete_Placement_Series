# # 1 2 3
# # 4 5 6
# # 7 8 9

# Row 1 = 6
# Row 2 = 15
# Row 3 = 24

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):

    row_sum = 0

    for j in range(cols):
        row_sum += matrix[i][j]

    print(f"Row {i + 1} = {row_sum}")

# tc = o(row*col)
#  sc = o(1)
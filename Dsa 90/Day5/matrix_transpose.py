matrix = [
    [1,2,3],
    [4,5,6],
    
]
rows = len(matrix)
cols = len(matrix[0])

for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=' ')
    print()
# ============================================================
# MATRIX PATTERN - Batch 1
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. MATRIX TRAVERSAL
# ============================================================

"""
THEORY (Interview Explanation)

Matrix Traversal sabse basic matrix problem hai. Isme matrix ke har
element ko systematically visit kiya jata hai. Hum nested loops ka use
karte hain jahan outer loop rows ko aur inner loop columns ko traverse
karta hai. Matrix ke lagbhag har question ki foundation traversal hi
hoti hai. Agar traversal strong hai to Row Sum, Column Sum, Diagonal,
Spiral aur Rotation jaise questions aasani se solve kiye ja sakte hain.
TCS Prime aur service-based interviews me ye sabse common matrix concept
hai.
"""

def matrix_traversal(matrix):

    for row in matrix:

        for value in row:

            print(value, end=" ")

        print()


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Matrix Traversal:")
matrix_traversal(matrix)


# Time  : O(rows × cols)
# Space : O(1)



# ============================================================
# 2. ROW SUM
# ============================================================

"""
THEORY (Interview Explanation)

Row Sum me matrix ki har row ke elements ka total nikalna hota hai.
Har row ko independently traverse karke uske elements ko add karte hain.
Ye problem nested loops aur matrix indexing ko samajhne ke liye puchi
jati hai. Interview me kabhi-kabhi maximum row sum ya minimum row sum
ka follow-up bhi pucha ja sakta hai. Isliye Row Sum matrix fundamentals
ka important part hai.
"""

def row_sum(matrix):

    result = []

    for row in matrix:

        total = 0

        for value in row:

            total += value

        result.append(total)

    return result


print()

print("Row Sum:")
print(row_sum(matrix))


# Time  : O(rows × cols)
# Space : O(rows)



# ============================================================
# 3. COLUMN SUM
# ============================================================

"""
THEORY (Interview Explanation)

Column Sum me har column ke sabhi elements ka sum calculate kiya jata
hai. Isme outer loop columns par aur inner loop rows par chalta hai.
Ye Row Sum ka reverse concept hai aur matrix indexing ko achhe se test
karta hai. Interview me is concept se Maximum Column Sum, Minimum Column
Sum aur Matrix Analysis jaise follow-up questions bhi ban sakte hain.
Ye TCS Prime aur service-based companies ka basic matrix question hai.
"""

def column_sum(matrix):

    rows = len(matrix)

    cols = len(matrix[0])

    result = []

    for col in range(cols):

        total = 0

        for row in range(rows):

            total += matrix[row][col]

        result.append(total)

    return result


print()

print("Column Sum:")
print(column_sum(matrix))


# ============================================================
# Expected Output
# ============================================================

# Matrix Traversal:
# 1 2 3
# 4 5 6
# 7 8 9

# Row Sum:
# [6, 15, 24]

# Column Sum:
# [12, 15, 18]


# ============================================================
# Complexity
# ============================================================

# Matrix Traversal
# Time  : O(m × n)
# Space : O(1)

# Row Sum
# Time  : O(m × n)
# Space : O(m)

# Column Sum
# Time  : O(m × n)
# Space : O(n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Matrix Traversal is the foundation of all matrix problems.
# ✔ Use nested loops for row-wise traversal.
# ✔ Row Sum → Traverse each row.
# ✔ Column Sum → Traverse each column.
# ✔ Frequently asked in TCS Prime & service-based interviews.

# ============================================================
# MATRIX PATTERN - Batch 1 COMPLETE ✅
# ============================================================


# ============================================================
# MATRIX PATTERN - Batch 2
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 4. PRIMARY DIAGONAL SUM
# ============================================================

"""
THEORY (Interview Explanation)

Primary Diagonal matrix ke top-left se bottom-right tak hoti hai.
Is diagonal ke elements ka row index aur column index same hota hai,
jaise matrix[i][i]. Isliye nested loops ki zarurat nahi hoti. Sirf
ek loop se diagonal traverse kar sakte hain. Ye matrix indexing ka
basic concept hai aur TCS Prime me frequently pucha jata hai. Isi
concept se trace of matrix aur diagonal traversal ke questions bhi
ban jate hain.
"""

def primary_diagonal_sum(matrix):

    total = 0

    for i in range(len(matrix)):

        total += matrix[i][i]

    return total


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Primary Diagonal Sum :")
print(primary_diagonal_sum(matrix))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 5. SECONDARY DIAGONAL SUM
# ============================================================

"""
THEORY (Interview Explanation)

Secondary Diagonal matrix ke top-right se bottom-left tak hoti hai.
Yaha row index i hota hai aur column index (n-i-1) hota hai.
Is formula ko yaad rakhna interview ke liye important hai.
Nested loops ki zarurat nahi hoti. Sirf ek loop se diagonal
elements ka sum nikal sakte hain.
"""

def secondary_diagonal_sum(matrix):

    n = len(matrix)

    total = 0

    for i in range(n):

        total += matrix[i][n-i-1]

    return total


print()

print("Secondary Diagonal Sum :")
print(secondary_diagonal_sum(matrix))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 6. TRANSPOSE MATRIX
# ============================================================

"""
THEORY (Interview Explanation)

Transpose ka matlab rows ko columns aur columns ko rows me convert
karna hota hai. Har element matrix[i][j] transpose matrix me
matrix[j][i] ban jata hai. Ye Matrix Manipulation ka sabse basic
question hai aur Rotation of Matrix ka base concept bhi hai.
Python me zip() se bhi transpose ho sakta hai, lekin interview
me generally loops se implementation expected hota hai.
"""

def transpose(matrix):

    rows = len(matrix)

    cols = len(matrix[0])

    result = [[0]*rows for _ in range(cols)]

    for i in range(rows):

        for j in range(cols):

            result[j][i] = matrix[i][j]

    return result


print()

print("Transpose Matrix :")

for row in transpose(matrix):

    print(row)


# ============================================================
# Expected Output
# ============================================================

# Primary Diagonal Sum :
# 15

# Secondary Diagonal Sum :
# 15

# Transpose Matrix :
# [1,4,7]
# [2,5,8]
# [3,6,9]


# ============================================================
# Complexity
# ============================================================

# Primary Diagonal
# Time  : O(n)
# Space : O(1)

# Secondary Diagonal
# Time  : O(n)
# Space : O(1)

# Transpose Matrix
# Time  : O(m × n)
# Space : O(m × n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Primary Diagonal  -> matrix[i][i]
# ✔ Secondary Diagonal -> matrix[i][n-i-1]
# ✔ Transpose -> matrix[j][i]
# ✔ Rotation of Matrix = Transpose + Reverse
# ✔ Very common in TCS Prime & service-based interviews.

# ============================================================
# MATRIX PATTERN - Batch 2 COMPLETE ✅
# ============================================================


# ============================================================
# MATRIX PATTERN - Batch 3
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 7. ROTATE MATRIX (90° Clockwise)
# ============================================================

"""
THEORY (Interview Explanation)

90° Matrix Rotation TCS Prime aur service-based companies ka ek popular
question hai. Rotation do steps me hota hai. Pehle matrix ka Transpose
karte hain jisse rows columns ban jati hain. Uske baad har row ko reverse
kar dete hain. In dono operations ke baad matrix 90 degree clockwise
rotate ho jati hai. Is approach ka fayda ye hai ki extra matrix banane ki
zarurat nahi padti. Interview me Rotation = Transpose + Reverse ye trick
yaad rakhna bahut important hai.
"""

def rotate_matrix(matrix):

    n = len(matrix)

    # Transpose
    for i in range(n):

        for j in range(i + 1, n):

            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse every row
    for row in matrix:

        row.reverse()

    return matrix


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Rotate Matrix :")

for row in rotate_matrix(matrix):

    print(row)


# Time  : O(n²)
# Space : O(1)



# ============================================================
# 8. SPIRAL MATRIX
# ============================================================

"""
THEORY (Interview Explanation)

Spiral Traversal me matrix ko clockwise spiral order me print karna hota
hai. Iske liye hum four boundaries maintain karte hain: top, bottom,
left aur right. Har iteration me pehle top row, fir right column, fir
bottom row aur last me left column traverse karte hain. Har traversal ke
baad boundary update kar dete hain. Jab boundaries cross kar jaye to
traversal complete ho jata hai. Ye Matrix Pattern ka sabse important
interview question hai.
"""

def spiral_matrix(matrix):

    result = []

    top = 0
    bottom = len(matrix) - 1

    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        for i in range(left, right + 1):

            result.append(matrix[top][i])

        top += 1

        for i in range(top, bottom + 1):

            result.append(matrix[i][right])

        right -= 1

        if top <= bottom:

            for i in range(right, left - 1, -1):

                result.append(matrix[bottom][i])

            bottom -= 1

        if left <= right:

            for i in range(bottom, top - 1, -1):

                result.append(matrix[i][left])

            left += 1

    return result


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print()

print("Spiral Traversal :")
print(spiral_matrix(matrix))


# ============================================================
# Expected Output
# ============================================================

# Rotate Matrix :
# [7,4,1]
# [8,5,2]
# [9,6,3]

# Spiral Traversal :
# [1,2,3,6,9,8,7,4,5]


# ============================================================
# Complexity
# ============================================================

# Rotate Matrix
# Time  : O(n²)
# Space : O(1)

# Spiral Matrix
# Time  : O(m × n)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ Rotate = Transpose + Reverse
# ✔ Spiral = Top + Right + Bottom + Left
# ✔ Maintain four boundaries.
# ✔ Update boundaries after every traversal.
# ✔ Very Frequently Asked in TCS Prime.

# ============================================================
# MATRIX PATTERN - Batch 3 COMPLETE ✅
# ============================================================


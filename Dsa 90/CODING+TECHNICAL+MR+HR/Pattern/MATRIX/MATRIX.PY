# ============================================================
# MATRIX PATTERN - Batch 1 (Traversal Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. MATRIX TRAVERSAL
# ============================================================

"""
THEORY (Interview Explanation)

Matrix Traversal Matrix Pattern ka sabse basic concept hai. Matrix ko
row by row traverse kiya jata hai aur har element ko ek baar visit
kiya jata hai. Nested loops use hote hain jahan outer loop rows aur
inner loop columns ko traverse karta hai. Row Sum, Column Sum,
Searching, Spiral, Rotation aur Matrix Multiplication jaise almost
saare matrix questions isi concept par based hote hain. TCS Prime me
ye sabse pehla matrix question hota hai.
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

print("Matrix Traversal :")
matrix_traversal(matrix)


# Time  : O(rows × cols)
# Space : O(1)



# ============================================================
# 2. ROW WISE TRAVERSAL
# ============================================================

"""
THEORY (Interview Explanation)

Row Wise Traversal me matrix ki ek complete row ko process kiya jata
hai aur fir next row par move karte hain. Ye matrix ka default
traversal pattern hai. Interview me Row Sum, Maximum Row Sum aur Row
Operations isi logic se solve hote hain.
"""

def row_wise_traversal(matrix):

    for i in range(len(matrix)):

        print("Row", i + 1, ":", end=" ")

        for j in range(len(matrix[0])):

            print(matrix[i][j], end=" ")

        print()


print()

print("Row Wise Traversal :")
row_wise_traversal(matrix)


# Time  : O(rows × cols)
# Space : O(1)



# ============================================================
# 3. COLUMN WISE TRAVERSAL
# ============================================================

"""
THEORY (Interview Explanation)

Column Wise Traversal me pehle ek complete column traverse kiya jata
hai aur uske baad next column par move karte hain. Isme outer loop
columns aur inner loop rows par chalta hai. Column Sum aur Column
Operations isi concept par based hote hain.
"""

def column_wise_traversal(matrix):

    rows = len(matrix)

    cols = len(matrix[0])

    for col in range(cols):

        print("Column", col + 1, ":", end=" ")

        for row in range(rows):

            print(matrix[row][col], end=" ")

        print()


print()

print("Column Wise Traversal :")
column_wise_traversal(matrix)


# Time  : O(rows × cols)
# Space : O(1)



# ============================================================
# 4. WAVE TRAVERSAL
# ============================================================

"""
THEORY (Interview Explanation)

Wave Traversal me first column top to bottom traverse hota hai,
second column bottom to top, third column top to bottom aur isi tarah
alternately traversal hota hai. Isse output wave pattern me aata hai.
Ye basic matrix traversal variation hai jo kabhi-kabhi TCS Prime aur
service-based interviews me pucha jata hai.
"""

def wave_traversal(matrix):

    rows = len(matrix)

    cols = len(matrix[0])

    result = []

    for col in range(cols):

        if col % 2 == 0:

            for row in range(rows):

                result.append(matrix[row][col])

        else:

            for row in range(rows - 1, -1, -1):

                result.append(matrix[row][col])

    return result


print()

print("Wave Traversal :")
print(wave_traversal(matrix))


# ============================================================
# Expected Output
# ============================================================

# Matrix Traversal :
# 1 2 3
# 4 5 6
# 7 8 9

# Row Wise Traversal :
# Row 1 : 1 2 3
# Row 2 : 4 5 6
# Row 3 : 7 8 9

# Column Wise Traversal :
# Column 1 : 1 4 7
# Column 2 : 2 5 8
# Column 3 : 3 6 9

# Wave Traversal :
# [1, 4, 7, 8, 5, 2, 3, 6, 9]


# ============================================================
# Complexity
# ============================================================

# Matrix Traversal
# Time  : O(m × n)
# Space : O(1)

# Row Wise Traversal
# Time  : O(m × n)
# Space : O(1)

# Column Wise Traversal
# Time  : O(m × n)
# Space : O(1)

# Wave Traversal
# Time  : O(m × n)
# Space : O(m × n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Matrix Traversal = Foundation of Matrix problems.
# ✔ Row Wise → Outer loop = Rows.
# ✔ Column Wise → Outer loop = Columns.
# ✔ Wave Traversal alternates traversal direction.
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# MATRIX - Batch 1 COMPLETE ✅
# ============================================================


# ============================================================
# MATRIX PATTERN - Batch 2 (Row + Column Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. ROW SUM
# ============================================================

"""
THEORY (Interview Explanation)

Row Sum Matrix ka sabse basic operation hai. Har row ke sabhi elements
ko add karke us row ka total nikalte hain. Iske liye outer loop rows
par aur inner loop columns par chalta hai. Isi concept se Maximum Row
Sum, Minimum Row Sum aur Average of Row jaise questions bante hain.
Ye TCS Prime aur service-based interviews ka common question hai.
"""

def row_sum(matrix):

    result = []

    for row in matrix:

        total = 0

        for value in row:

            total += value

        result.append(total)

    return result


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Row Sum :")
print(row_sum(matrix))


# Time  : O(m × n)
# Space : O(m)



# ============================================================
# 2. MAXIMUM ROW SUM
# ============================================================

"""
THEORY (Interview Explanation)

Maximum Row Sum me us row ko find karna hota hai jiska total sabse
zyada ho. Har row ka sum calculate karte hain aur maximum sum track
karte rehte hain. Interview me kabhi row number bhi pucha jata hai,
isliye maximum row index maintain karna useful hota hai.
"""

def maximum_row_sum(matrix):

    maximum = float("-inf")

    row_index = -1

    for i, row in enumerate(matrix):

        total = sum(row)

        if total > maximum:

            maximum = total

            row_index = i

    return maximum, row_index


print()

print("Maximum Row Sum :")
print(maximum_row_sum(matrix))


# Time  : O(m × n)
# Space : O(1)



# ============================================================
# 3. COLUMN SUM
# ============================================================

"""
THEORY (Interview Explanation)

Column Sum me har column ke elements ka total calculate kiya jata hai.
Outer loop columns par aur inner loop rows par chalta hai. Ye Row Sum
ka reverse concept hai aur matrix indexing ko test karta hai. Ye basic
matrix interview question hai.
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

print("Column Sum :")
print(column_sum(matrix))


# Time  : O(m × n)
# Space : O(n)



# ============================================================
# 4. MAXIMUM COLUMN SUM
# ============================================================

"""
THEORY (Interview Explanation)

Maximum Column Sum me sabse zyada sum wale column ko find karna hota
hai. Har column ka sum calculate karte hain aur maximum value aur
column index maintain karte hain. Ye Column Sum ka extension hai aur
service-based companies me kabhi-kabhi pucha jata hai.
"""

def maximum_column_sum(matrix):

    rows = len(matrix)

    cols = len(matrix[0])

    maximum = float("-inf")

    column_index = -1

    for col in range(cols):

        total = 0

        for row in range(rows):

            total += matrix[row][col]

        if total > maximum:

            maximum = total

            column_index = col

    return maximum, column_index


print()

print("Maximum Column Sum :")
print(maximum_column_sum(matrix))


# ============================================================
# Expected Output
# ============================================================

# Row Sum :
# [6, 15, 24]

# Maximum Row Sum :
# (24, 2)

# Column Sum :
# [12, 15, 18]

# Maximum Column Sum :
# (18, 2)


# ============================================================
# Complexity
# ============================================================

# Row Sum
# Time  : O(m × n)
# Space : O(m)

# Maximum Row Sum
# Time  : O(m × n)
# Space : O(1)

# Column Sum
# Time  : O(m × n)
# Space : O(n)

# Maximum Column Sum
# Time  : O(m × n)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ Row Sum → Traverse each row.
# ✔ Column Sum → Traverse each column.
# ✔ Track maximum sum and corresponding index.
# ✔ Matrix indexing is the key concept.
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# MATRIX - Batch 2 COMPLETE ✅
# ============================================================

# ============================================================
# MATRIX PATTERN - Batch 3 (Diagonal Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. PRIMARY DIAGONAL SUM
# ============================================================

"""
THEORY (Interview Explanation)

Primary Diagonal matrix ke top-left se bottom-right tak hoti hai.
Primary diagonal ke liye row aur column index same hote hain,
matlab matrix[i][i]. Isi wajah se nested loops ki zarurat nahi hoti.
Sirf ek loop se diagonal traverse kar sakte hain. Ye matrix indexing
ka basic concept hai aur TCS Prime me frequently pucha jata hai.
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
# 2. SECONDARY DIAGONAL SUM
# ============================================================

"""
THEORY (Interview Explanation)

Secondary Diagonal matrix ke top-right se bottom-left tak hoti hai.
Isme row index i hota hai aur column index (n-i-1) hota hai.
Ye formula interview ke liye bahut important hai. Sirf ek loop se
diagonal sum calculate kiya ja sakta hai. Ye Primary Diagonal ka
reverse concept hai.
"""

def secondary_diagonal_sum(matrix):

    n = len(matrix)

    total = 0

    for i in range(n):

        total += matrix[i][n - i - 1]

    return total


print()

print("Secondary Diagonal Sum :")
print(secondary_diagonal_sum(matrix))


# Time  : O(n)
# Space : O(1)



# ============================================================
# 3. DIFFERENCE OF DIAGONALS
# ============================================================

"""
THEORY (Interview Explanation)

Difference of Diagonals me Primary Diagonal Sum aur Secondary Diagonal
Sum ka absolute difference nikalte hain. Is problem me dono diagonals
ko ek hi loop me calculate kiya ja sakta hai. Interview me matrix
indexing aur diagonal concepts ko test karne ke liye ye question
bahut common hai.
"""

def diagonal_difference(matrix):

    n = len(matrix)

    primary = 0
    secondary = 0

    for i in range(n):

        primary += matrix[i][i]

        secondary += matrix[i][n - i - 1]

    return abs(primary - secondary)


print()

print("Difference of Diagonals :")
print(diagonal_difference(matrix))


# ============================================================
# Expected Output
# ============================================================

# Primary Diagonal Sum :
# 15

# Secondary Diagonal Sum :
# 15

# Difference of Diagonals :
# 0


# ============================================================
# Complexity
# ============================================================

# Primary Diagonal Sum
# Time  : O(n)
# Space : O(1)

# Secondary Diagonal Sum
# Time  : O(n)
# Space : O(1)

# Difference of Diagonals
# Time  : O(n)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ Primary Diagonal  -> matrix[i][i]
# ✔ Secondary Diagonal -> matrix[i][n-i-1]
# ✔ Difference = |Primary - Secondary|
# ✔ Only one loop is required.
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# MATRIX - Batch 3 COMPLETE ✅
# ============================================================

# ============================================================
# MATRIX PATTERN - Batch 4 (Boundary Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. BOUNDARY TRAVERSAL
# ============================================================

"""
THEORY (Interview Explanation)

Boundary Traversal me matrix ke sirf outer boundary elements print kiye
jate hain. Traversal ka order hota hai: Top Row → Right Column →
Bottom Row → Left Column. Corners ko sirf ek baar print karna hota hai,
isliye loops ko carefully design kiya jata hai. Ye Matrix Traversal ka
important variation hai aur TCS Prime me basic level par pucha ja sakta
hai. Is problem se matrix indexing aur boundary conditions dono test
hote hain.
"""

def boundary_traversal(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    # Top Row
    for j in range(cols):
        result.append(matrix[0][j])

    # Right Column
    for i in range(1, rows):
        result.append(matrix[i][cols - 1])

    # Bottom Row
    if rows > 1:
        for j in range(cols - 2, -1, -1):
            result.append(matrix[rows - 1][j])

    # Left Column
    if cols > 1:
        for i in range(rows - 2, 0, -1):
            result.append(matrix[i][0])

    return result


matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

print("Boundary Traversal :")
print(boundary_traversal(matrix))


# ============================================================
# Expected Output
# ============================================================

# Boundary Traversal :
# [1,2,3,4,8,12,16,15,14,13,9,5]


# ============================================================
# Complexity
# ============================================================

# Boundary Traversal
# Time  : O(m + n)
# Space : O(m + n)


# ============================================================
# Interview Points
# ============================================================

# ✔ Traverse in this order:
#   Top → Right → Bottom → Left
# ✔ Corner elements should not repeat.
# ✔ Check single row and single column edge cases.
# ✔ Matrix indexing is the key concept.
# ✔ Occasionally Asked in TCS Prime & Service-Based Companies.

# ============================================================
# MATRIX - Batch 4 COMPLETE ✅
# ============================================================


# ============================================================
# MATRIX PATTERN - Batch 5 (Transpose Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. MATRIX TRANSPOSE
# ============================================================

"""
THEORY (Interview Explanation)

Matrix Transpose ka matlab rows ko columns aur columns ko rows me
convert karna hota hai. Agar original matrix me element matrix[i][j]
hai to transpose matrix me wahi element matrix[j][i] ban jata hai.
Ye Matrix Manipulation ka sabse basic concept hai aur Rotation of
Matrix ka foundation bhi hai. Interview me generally nested loops se
transpose implement karne ko bola jata hai.
"""

def matrix_transpose(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    transpose = [[0] * rows for _ in range(cols)]

    for i in range(rows):

        for j in range(cols):

            transpose[j][i] = matrix[i][j]

    return transpose


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Matrix Transpose :")

for row in matrix_transpose(matrix):

    print(row)


# Time  : O(m × n)
# Space : O(m × n)



# ============================================================
# 2. IN-PLACE TRANSPOSE
# ============================================================

"""
THEORY (Interview Explanation)

In-Place Transpose sirf square matrix ke liye possible hota hai.
Isme extra matrix nahi banate. Sirf upper triangle aur lower triangle
ke elements ko swap kar dete hain. Is approach me extra space O(1)
lagti hai. Ye TCS Prime aur service-based companies ka important
matrix interview question hai.
"""

def inplace_transpose(matrix):

    n = len(matrix)

    for i in range(n):

        for j in range(i + 1, n):

            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print()

print("In-Place Transpose :")

for row in inplace_transpose(matrix2):

    print(row)


# Time  : O(n²)
# Space : O(1)



# ============================================================
# 3. SYMMETRIC MATRIX CHECK
# ============================================================

"""
THEORY (Interview Explanation)

Symmetric Matrix wo hoti hai jo transpose ke baad bhi same rahe.
Mathematically A == Aᵀ. Iske liye sirf upper triangle ko lower triangle
se compare karna kaafi hota hai. Agar kisi bhi position par mismatch
milta hai to matrix symmetric nahi hai. Ye transpose concept ka direct
application hai.
"""

def symmetric_matrix(matrix):

    n = len(matrix)

    for i in range(n):

        for j in range(i + 1, n):

            if matrix[i][j] != matrix[j][i]:

                return False

    return True


matrix3 = [
    [1,2,3],
    [2,4,5],
    [3,5,6]
]

print()

print("Symmetric Matrix :")
print(symmetric_matrix(matrix3))


# ============================================================
# Expected Output
# ============================================================

# Matrix Transpose :
# [1,4,7]
# [2,5,8]
# [3,6,9]

# In-Place Transpose :
# [1,4,7]
# [2,5,8]
# [3,6,9]

# Symmetric Matrix :
# True


# ============================================================
# Complexity
# ============================================================

# Matrix Transpose
# Time  : O(m × n)
# Space : O(m × n)

# In-Place Transpose
# Time  : O(n²)
# Space : O(1)

# Symmetric Matrix
# Time  : O(n²)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ Transpose → matrix[j][i]
# ✔ In-Place Transpose works only for square matrices.
# ✔ Symmetric Matrix ⇒ A == Aᵀ
# ✔ Rotation = Transpose + Reverse
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# MATRIX - Batch 5 COMPLETE ✅
# ============================================================


# ============================================================
# MATRIX PATTERN - Batch 6 (Rotation Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. ROTATE MATRIX 90° CLOCKWISE
# ============================================================

"""
THEORY (Interview Explanation)

90° Clockwise Rotation Matrix ka sabse important rotation question hai.
Iska easiest approach hai pehle matrix ka transpose banana aur uske
baad har row ko reverse kar dena. Interview me ye trick bahut important
hai. TCS Prime aur service-based companies me direct pucha ja sakta hai.
Formula yaad rakho:

Transpose → Reverse Every Row
"""

def rotate_clockwise(matrix):

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

print("Rotate 90° Clockwise :")

for row in rotate_clockwise(matrix):

    print(row)


# Time  : O(n²)
# Space : O(1)



# ============================================================
# 2. ROTATE MATRIX 90° ANTI-CLOCKWISE
# ============================================================

"""
THEORY (Interview Explanation)

90° Anti-Clockwise Rotation bhi transpose par based hoti hai. Difference
sirf itna hai ki transpose ke baad columns reverse karte hain. Isko
easily transpose ke baad row swapping se implement kar sakte hain.
Formula yaad rakho:

Transpose → Reverse Every Column

Ye Clockwise Rotation ka reverse concept hai.
"""

def rotate_anticlockwise(matrix):

    n = len(matrix)

    # Transpose
    for i in range(n):

        for j in range(i + 1, n):

            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse every column
    for col in range(n):

        top = 0
        bottom = n - 1

        while top < bottom:

            matrix[top][col], matrix[bottom][col] = \
            matrix[bottom][col], matrix[top][col]

            top += 1
            bottom -= 1

    return matrix


matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print()

print("Rotate 90° Anti-Clockwise :")

for row in rotate_anticlockwise(matrix2):

    print(row)


# ============================================================
# Expected Output
# ============================================================

# Rotate 90° Clockwise :
# [7,4,1]
# [8,5,2]
# [9,6,3]

# Rotate 90° Anti-Clockwise :
# [3,6,9]
# [2,5,8]
# [1,4,7]


# ============================================================
# Complexity
# ============================================================

# Rotate 90° Clockwise
# Time  : O(n²)
# Space : O(1)

# Rotate 90° Anti-Clockwise
# Time  : O(n²)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ Clockwise = Transpose + Reverse Rows
# ✔ Anti-Clockwise = Transpose + Reverse Columns
# ✔ Works only for square matrices.
# ✔ In-place solution uses O(1) extra space.
# ✔ One of the most frequently asked Matrix problems in
#   TCS Prime & Service-Based Companies.

# ============================================================
# MATRIX - Batch 6 COMPLETE ✅
# ============================================================

# ============================================================
# MATRIX PATTERN - Batch 7 (Searching Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. LINEAR SEARCH IN MATRIX
# ============================================================

"""
THEORY (Interview Explanation)

Linear Search Matrix ka sabse basic searching algorithm hai. Matrix ke
har element ko ek-ek karke traverse karte hain aur target value se
compare karte hain. Agar match mil jaye to uska row aur column index
return kar dete hain. Agar pura matrix traverse ho jaye aur element na
mile to (-1, -1) return karte hain. Ye Matrix Traversal ka direct
application hai aur TCS Prime me frequently pucha jata hai.
"""

def linear_search(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):

        for j in range(cols):

            if matrix[i][j] == target:

                return (i, j)

    return (-1, -1)


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Linear Search :")
print(linear_search(matrix, 8))


# Time  : O(m × n)
# Space : O(1)



# ============================================================
# 2. SEARCH IN SORTED MATRIX
# ============================================================

"""
THEORY (Interview Explanation)

Sorted Matrix me har row aur har column ascending order me sorted hota
hai. Sabse efficient approach Top-Right Corner se start karna hai.
Agar current element target se bada hai to left move karte hain.
Agar current element target se chhota hai to neeche move karte hain.
Is approach me har row aur column maximum ek baar visit hota hai.
Ye TCS Prime ka important searching question hai.
"""

def search_sorted_matrix(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    while row < rows and col >= 0:

        if matrix[row][col] == target:

            return (row, col)

        elif matrix[row][col] > target:

            col -= 1

        else:

            row += 1

    return (-1, -1)


sorted_matrix = [
    [1,4,7,11],
    [2,5,8,12],
    [3,6,9,16],
    [10,13,14,17]
]

print()

print("Search in Sorted Matrix :")
print(search_sorted_matrix(sorted_matrix, 9))


# ============================================================
# Expected Output
# ============================================================

# Linear Search :
# (2, 1)

# Search in Sorted Matrix :
# (2, 2)


# ============================================================
# Complexity
# ============================================================

# Linear Search
# Time  : O(m × n)
# Space : O(1)

# Search in Sorted Matrix
# Time  : O(m + n)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ Linear Search checks every element.
# ✔ Sorted Matrix starts from Top-Right Corner.
# ✔ Greater → Move Left.
# ✔ Smaller → Move Down.
# ✔ Sorted Matrix Search is a very common TCS Prime question.

# ============================================================
# MATRIX - Batch 7 COMPLETE ✅
# ============================================================


# ============================================================
# MATRIX PATTERN - Batch 8 (Spiral Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. SPIRAL TRAVERSAL
# ============================================================

"""
THEORY (Interview Explanation)

Spiral Traversal Matrix ka sabse popular traversal pattern hai. Matrix
ko outer layer se inner layer ki taraf clockwise direction me traverse
kiya jata hai. Iske liye four boundaries maintain karte hain:
Top, Bottom, Left aur Right. Har traversal ke baad boundary update
hoti hai. Jab Top > Bottom ya Left > Right ho jaye to traversal stop
kar dete hain. Ye indexing aur boundary handling ko test karta hai aur
TCS Prime me frequently pucha jata hai.
"""

def spiral_traversal(matrix):

    result = []

    top = 0
    bottom = len(matrix) - 1

    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # Top Row
        for i in range(left, right + 1):
            result.append(matrix[top][i])

        top += 1

        # Right Column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])

        right -= 1

        # Bottom Row
        if top <= bottom:

            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])

            bottom -= 1

        # Left Column
        if left <= right:

            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])

            left += 1

    return result


matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

print("Spiral Traversal :")
print(spiral_traversal(matrix))


# ============================================================
# Expected Output
# ============================================================

# Spiral Traversal :
# [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]


# ============================================================
# Complexity
# ============================================================

# Spiral Traversal
# Time  : O(m × n)
# Space : O(m × n)    # Result list


# ============================================================
# Interview Points
# ============================================================

# ✔ Maintain four boundaries:
#   Top, Bottom, Left, Right.
# ✔ Traverse in order:
#   Top → Right → Bottom → Left.
# ✔ Update boundaries after every traversal.
# ✔ Stop when Top > Bottom or Left > Right.
# ✔ One of the most frequently asked Matrix questions in
#   TCS Prime & Service-Based Companies.

# ============================================================
# MATRIX - Batch 8 COMPLETE ✅
# ============================================================

# ============================================================
# MATRIX PATTERN - Batch 9 (Matrix Operations)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. MATRIX ADDITION
# ============================================================

"""
THEORY (Interview Explanation)

Matrix Addition me dono matrices ka size same hona chahiye. Har
position ke corresponding elements ko add karke naya matrix banaya
jata hai. Agar A[i][j] aur B[i][j] given hain to answer matrix ka
element A[i][j] + B[i][j] hoga. Nested loops use hote hain kyunki
har element ko ek baar process karna padta hai. Ye Matrix Basics ka
sabse common operation hai aur TCS Prime me frequently pucha jata hai.
"""

def matrix_addition(A, B):

    rows = len(A)
    cols = len(A[0])

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):

        for j in range(cols):

            result[i][j] = A[i][j] + B[i][j]

    return result


A = [
    [1,2],
    [3,4]
]

B = [
    [5,6],
    [7,8]
]

print("Matrix Addition :")

for row in matrix_addition(A, B):

    print(row)


# Time  : O(m × n)
# Space : O(m × n)



# ============================================================
# 2. MATRIX MULTIPLICATION
# ============================================================

"""
THEORY (Interview Explanation)

Matrix Multiplication me pehli matrix ke rows aur doosri matrix ke
columns multiply hote hain. Har answer cell ke liye ek row aur ek
column ka dot product calculate kiya jata hai. Isliye teen nested
loops use hote hain. Formula:

Result[i][j] += A[i][k] × B[k][j]

Ye Matrix Operations ka sabse important question hai aur interviews me
basic implementation pucha ja sakta hai.
"""

def matrix_multiplication(A, B):

    rows = len(A)
    cols = len(B[0])
    common = len(B)

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):

        for j in range(cols):

            for k in range(common):

                result[i][j] += A[i][k] * B[k][j]

    return result


A = [
    [1,2],
    [3,4]
]

B = [
    [5,6],
    [7,8]
]

print()

print("Matrix Multiplication :")

for row in matrix_multiplication(A, B):

    print(row)


# ============================================================
# Expected Output
# ============================================================

# Matrix Addition :
# [6, 8]
# [10, 12]

# Matrix Multiplication :
# [19, 22]
# [43, 50]


# ============================================================
# Complexity
# ============================================================

# Matrix Addition
# Time  : O(m × n)
# Space : O(m × n)

# Matrix Multiplication
# Time  : O(n³)
# Space : O(m × p)


# ============================================================
# Interview Points
# ============================================================

# ✔ Addition requires same matrix dimensions.
# ✔ Multiplication:
#   Columns of A = Rows of B.
# ✔ Multiplication uses three nested loops.
# ✔ Formula:
#   Result[i][j] += A[i][k] * B[k][j]
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# MATRIX - Batch 9 COMPLETE ✅
# ============================================================

# ============================================================
# MATRIX PATTERN - Batch 10 (Miscellaneous Pattern)
# Companies:
# TCS Prime | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ============================================================
# 1. MAXIMUM ELEMENT IN MATRIX
# ============================================================

"""
THEORY (Interview Explanation)

Maximum Element matrix ka sabse bada value hota hai. Matrix ke har
element ko traverse karke current maximum se compare karte hain.
Agar current element bada ho to maximum update kar dete hain.
Ye Matrix Traversal ka direct application hai aur interview me basic
logic aur nested loops check karne ke liye pucha jata hai.
"""

def maximum_element(matrix):

    maximum = matrix[0][0]

    for row in matrix:

        for value in row:

            if value > maximum:

                maximum = value

    return maximum


matrix = [
    [5,8,2],
    [10,3,7],
    [1,15,6]
]

print("Maximum Element :")
print(maximum_element(matrix))


# Time  : O(m × n)
# Space : O(1)



# ============================================================
# 2. MINIMUM ELEMENT IN MATRIX
# ============================================================

"""
THEORY (Interview Explanation)

Minimum Element matrix ka sabse chhota value hota hai. Har element ko
nested loops se traverse karke current minimum se compare karte hain.
Agar current value chhoti ho to minimum update kar dete hain.
Ye Maximum Element ka reverse concept hai aur service-based companies
me frequently pucha jata hai.
"""

def minimum_element(matrix):

    minimum = matrix[0][0]

    for row in matrix:

        for value in row:

            if value < minimum:

                minimum = value

    return minimum


print()

print("Minimum Element :")
print(minimum_element(matrix))


# ============================================================
# Expected Output
# ============================================================

# Maximum Element :
# 15

# Minimum Element :
# 1


# ============================================================
# Complexity
# ============================================================

# Maximum Element
# Time  : O(m × n)
# Space : O(1)

# Minimum Element
# Time  : O(m × n)
# Space : O(1)


# ============================================================
# Interview Points
# ============================================================

# ✔ Traverse every matrix element once.
# ✔ Keep updating current maximum/minimum.
# ✔ Nested loops are sufficient.
# ✔ Foundation for many matrix optimization problems.
# ✔ Frequently Asked in TCS Prime & Service-Based Companies.

# ============================================================
# MATRIX PATTERN COMPLETE ✅
# ============================================================


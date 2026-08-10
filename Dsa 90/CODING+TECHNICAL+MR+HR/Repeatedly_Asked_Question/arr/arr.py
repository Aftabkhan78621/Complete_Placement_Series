# ============================================================
# 84. Sort Array Ascending
# Pattern : Sorting
# Time  : O(n²)
# Space : O(1)
# ============================================================

def sort_ascending(arr):

    n = len(arr)

    for i in range(n - 1):

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ============================================================
# 85. Sort Array Descending
# Pattern : Sorting
# Time  : O(n²)
# Space : O(1)
# ============================================================

def sort_descending(arr):

    n = len(arr)

    for i in range(n - 1):

        for j in range(n - i - 1):

            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ============================================================
# Driver Code
# ============================================================

arr = [12, 5, 18, 2, 9, 25]

print("Original Array :", arr)

print("Ascending :", sort_ascending(arr.copy()))

print("Descending :", sort_descending(arr.copy()))


# ============================================================
# Output
# ============================================================

# Original Array : [12, 5, 18, 2, 9, 25]
# Ascending : [2, 5, 9, 12, 18, 25]
# Descending : [25, 18, 12, 9, 5, 2]



# ============================================================
# ARRAY PATTERN (Service-Based Companies)
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(1)
# ============================================================


# ------------------------------------------------------------
# 108. Move Zeros to Start
# ------------------------------------------------------------
# Example:
# [1,0,2,0,3,4]
#
# Output:
# [0,0,1,2,3,4]
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def move_zeros_to_start(arr):

    index = len(arr) - 1

    for i in range(len(arr)-1, -1, -1):

        if arr[i] != 0:
            arr[index] = arr[i]
            index -= 1

    while index >= 0:
        arr[index] = 0
        index -= 1

    return arr


# ------------------------------------------------------------
# 113. Compare Two Arrays
# ------------------------------------------------------------
# Example:
# [1,2,3]
# [1,2,3]
#
# Output:
# True
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def compare_arrays(arr1, arr2):

    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):

        if arr1[i] != arr2[i]:
            return False

    return True


# ------------------------------------------------------------
# 115. Find Index Without index()
# ------------------------------------------------------------
# Example:
# [10,20,30,40]
#
# Target:
# 30
#
# Output:
# 2
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def find_index(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1


# ------------------------------------------------------------
# 116. Insert Element At Position
# ------------------------------------------------------------
# Example:
# [10,20,30,40]
#
# Position = 2
#
# Value = 25
#
# Output:
# [10,20,25,30,40]
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def insert_element(arr, position, value):

    arr.append(0)

    for i in range(len(arr)-1, position, -1):

        arr[i] = arr[i-1]

    arr[position] = value

    return arr


# ------------------------------------------------------------
# 117. Delete Element From Position
# ------------------------------------------------------------
# Example:
# [10,20,30,40,50]
#
# Position = 2
#
# Output:
# [10,20,40,50]
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def delete_element(arr, position):

    for i in range(position, len(arr)-1):

        arr[i] = arr[i+1]

    arr.pop()

    return arr


# ============================================================
# Driver Code
# ============================================================

arr1 = [1,0,2,0,3,4]

print("Move Zeros To Start :")
print(move_zeros_to_start(arr1))


arr2 = [1,2,3]
arr3 = [1,2,3]

print("\nCompare Arrays :")
print(compare_arrays(arr2, arr3))


arr4 = [10,20,30,40]

print("\nFind Index :")
print(find_index(arr4,30))


arr5 = [10,20,30,40]

print("\nInsert Element :")
print(insert_element(arr5,2,25))


arr6 = [10,20,30,40,50]

print("\nDelete Element :")
print(delete_element(arr6,2))


# ============================================================
# Expected Output
# ============================================================

# Move Zeros To Start :
# [0, 0, 1, 2, 3, 4]

# Compare Arrays :
# True

# Find Index :
# 2

# Insert Element :
# [10, 20, 25, 30, 40]

# Delete Element :
# [10, 20, 40, 50]

# ============================================================
# Complexity
# ============================================================

# Move Zeros To Start      O(n)   O(1)
# Compare Arrays           O(n)   O(1)
# Find Index               O(n)   O(1)
# Insert Element           O(n)   O(1)
# Delete Element           O(n)   O(1)

# ============================================================
# Frequently Asked:
#
# ✅ TCS
# ✅ Infosys
# ✅ Accenture
# ✅ Capgemini
# ✅ Cognizant
# ✅ IBM
# ✅ Deloitte
# ✅ Wipro
# ✅ HCL
# ✅ Cyntexa
# ============================================================

# ============================================================
# ARRAY PATTERN (Service-Based Companies)
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Filter Applied:
# Only High-Probability & Unique Questions
# ============================================================


# ------------------------------------------------------------
# 127. Filter Numbers Greater Than N
# ------------------------------------------------------------
# Example:
# [10,25,5,40,18]
#
# N = 20
#
# Output:
# [25,40]
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def filter_greater_than_n(arr, n):

    result = []

    for num in arr:

        if num > n:
            result.append(num)

    return result


# ------------------------------------------------------------
# 139. Remove Negative Numbers
# ------------------------------------------------------------
# Example:
# [-5,10,-2,7,3,-8]
#
# Output:
# [10,7,3]
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def remove_negative_numbers(arr):

    result = []

    for num in arr:

        if num >= 0:
            result.append(num)

    return result


# ============================================================
# Driver Code
# ============================================================

arr1 = [10,25,5,40,18]

print("Filter Numbers Greater Than 20 :")
print(filter_greater_than_n(arr1, 20))


arr2 = [-5,10,-2,7,3,-8]

print("\nRemove Negative Numbers :")
print(remove_negative_numbers(arr2))


# ============================================================
# Expected Output
# ============================================================

# Filter Numbers Greater Than 20 :
# [25, 40]

# Remove Negative Numbers :
# [10, 7, 3]


# ============================================================
# Complexity
# ============================================================

# Filter Numbers > N         O(n)   O(n)
# Remove Negative Numbers    O(n)   O(n)
# ============================================================
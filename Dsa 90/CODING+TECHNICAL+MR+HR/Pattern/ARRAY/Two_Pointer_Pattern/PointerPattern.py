# ============================================================
# TWO POINTER PATTERN - Batch 1
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(1)
# ============================================================


# ------------------------------------------------------------
# 1. Reverse Array
# ------------------------------------------------------------
# Example:
# [10,20,30,40,50]
#
# Output:
# [50,40,30,20,10]
#
# Idea:
# Two pointers (Left & Right)
# Swap both values and move towards center.
# ------------------------------------------------------------

def reverse_array(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr


# ------------------------------------------------------------
# 2. Move Zeros To End
# ------------------------------------------------------------
# Example:
# [0,1,0,3,12]
#
# Output:
# [1,3,12,0,0]
#
# Idea:
# First pointer keeps position of non-zero element.
# Second pointer traverses array.
# ------------------------------------------------------------

def move_zeros(arr):

    left = 0

    for right in range(len(arr)):

        if arr[right] != 0:

            arr[left], arr[right] = arr[right], arr[left]

            left += 1

    return arr


# ------------------------------------------------------------
# 3. Move Negative Numbers To Beginning
# ------------------------------------------------------------
# Example:
# [5,-2,7,-9,3,-1]
#
# Output:
# [-2,-9,-1,5,7,3]
#
# Idea:
# Left pointer stores position for negatives.
# Right pointer traverses array.
# ------------------------------------------------------------

def move_negatives(arr):

    left = 0

    for right in range(len(arr)):

        if arr[right] < 0:

            arr[left], arr[right] = arr[right], arr[left]

            left += 1

    return arr


# ============================================================
# Driver Code
# ============================================================

arr1 = [10,20,30,40,50]
print("Reverse Array :")
print(reverse_array(arr1))

print()

arr2 = [0,1,0,3,12]
print("Move Zeros To End :")
print(move_zeros(arr2))

print()

arr3 = [5,-2,7,-9,3,-1]
print("Move Negatives :")
print(move_negatives(arr3))


# ============================================================
# Expected Output
# ============================================================

# Reverse Array :
# [50, 40, 30, 20, 10]

# Move Zeros To End :
# [1, 3, 12, 0, 0]

# Move Negatives :
# [-2, -9, -1, 5, 7, 3]


# ============================================================
# Complexity
# ============================================================

# Reverse Array        O(n)   O(1)

# Move Zeros           O(n)   O(1)

# Move Negatives       O(n)   O(1)

# ============================================================


# ============================================================
# TWO POINTER PATTERN - Batch 2
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(1)
# ============================================================


# ------------------------------------------------------------
# 4. Move Even Numbers Left & Odd Numbers Right
# ------------------------------------------------------------
# Example:
# [1,2,3,4,5,6]
#
# Output:
# [6,2,4,3,5,1]
# (Order may vary)
# ------------------------------------------------------------

def move_even_odd(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        while left < right and arr[left] % 2 == 0:
            left += 1

        while left < right and arr[right] % 2 != 0:
            right -= 1

        arr[left], arr[right] = arr[right], arr[left]

    return arr


# ------------------------------------------------------------
# 5. Remove Duplicates (Sorted Array)
# ------------------------------------------------------------
# Example:
# [1,1,2,2,3,4,4]
#
# Output:
# [1,2,3,4]
# ------------------------------------------------------------

def remove_duplicates(arr):

    if not arr:
        return []

    left = 0

    for right in range(1, len(arr)):

        if arr[right] != arr[left]:

            left += 1
            arr[left] = arr[right]

    return arr[:left+1]


# ------------------------------------------------------------
# 6. Remove Element
# ------------------------------------------------------------
# Example:
# [3,2,2,3,4]
#
# Remove = 3
#
# Output:
# [2,2,4]
# ------------------------------------------------------------

def remove_element(arr, value):

    left = 0

    for right in range(len(arr)):

        if arr[right] != value:

            arr[left] = arr[right]

            left += 1

    return arr[:left]


# ============================================================
# Driver Code
# ============================================================

arr1 = [1,2,3,4,5,6]

print("Move Even/Odd :")
print(move_even_odd(arr1))

print()

arr2 = [1,1,2,2,3,4,4]

print("Remove Duplicates :")
print(remove_duplicates(arr2))

print()

arr3 = [3,2,2,3,4]

print("Remove Element :")
print(remove_element(arr3,3))


# ============================================================
# Expected Output
# ============================================================

# Move Even/Odd :
# [6,2,4,3,5,1]

# Remove Duplicates :
# [1,2,3,4]

# Remove Element :
# [2,2,4]


# ============================================================
# Complexity
# ============================================================

# Move Even/Odd          O(n)   O(1)

# Remove Duplicates      O(n)   O(1)

# Remove Element         O(n)   O(1)

# ============================================================

# ============================================================
# TWO POINTER PATTERN - Batch 3
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(1)
# ============================================================


# ------------------------------------------------------------
# 7. Merge Two Sorted Arrays
# ------------------------------------------------------------
# Example:
# [1,3,5]
# [2,4,6]
#
# Output:
# [1,2,3,4,5,6]
# ------------------------------------------------------------

def merge_sorted_arrays(arr1, arr2):

    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


# ------------------------------------------------------------
# 8. Two Sum (Sorted Array)
# ------------------------------------------------------------
# Example:
# [2,7,11,15]
#
# Target = 9
#
# Output:
# [0,1]
# ------------------------------------------------------------

def two_sum_sorted(arr, target):

    left = 0
    right = len(arr) - 1

    while left < right:

        total = arr[left] + arr[right]

        if total == target:
            return [left, right]

        elif total < target:
            left += 1

        else:
            right -= 1

    return [-1, -1]


# ------------------------------------------------------------
# 9. Pair Sum (Unsorted Array)
# ------------------------------------------------------------
# Example:
# [8,7,2,5,3,1]
#
# Target = 10
#
# Output:
# (8,2)
#
# Note:
# Service-based companies generally expect
# HashSet solution for unsorted arrays.
# ------------------------------------------------------------

def pair_sum(arr, target):

    seen = set()

    for num in arr:

        diff = target - num

        if diff in seen:
            return (diff, num)

        seen.add(num)

    return None


# ============================================================
# Driver Code
# ============================================================

arr1 = [1,3,5]
arr2 = [2,4,6]

print("Merge Sorted Arrays :")
print(merge_sorted_arrays(arr1, arr2))

print()

arr3 = [2,7,11,15]

print("Two Sum (Sorted) :")
print(two_sum_sorted(arr3, 9))

print()

arr4 = [8,7,2,5,3,1]

print("Pair Sum :")
print(pair_sum(arr4, 10))


# ============================================================
# Expected Output
# ============================================================

# Merge Sorted Arrays :
# [1,2,3,4,5,6]

# Two Sum (Sorted) :
# [0,1]

# Pair Sum :
# (8,2)


# ============================================================
# Complexity
# ============================================================

# Merge Sorted Arrays     O(n+m)   O(n+m)

# Two Sum (Sorted)        O(n)     O(1)

# Pair Sum                O(n)     O(n)

# ============================================================


# ============================================================
# TWO POINTER PATTERN - Batch 4 (Final)
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(n) / O(1)
# ============================================================


# ------------------------------------------------------------
# 10. Squares of Sorted Array
# ------------------------------------------------------------
# Example:
# [-7,-3,2,3,11]
#
# Output:
# [4,9,9,49,121]
#
# Idea:
# Compare absolute values from both ends.
# Larger square goes at the end.
# ------------------------------------------------------------

def sorted_squares(arr):

    n = len(arr)

    result = [0] * n

    left = 0
    right = n - 1
    index = n - 1

    while left <= right:

        if abs(arr[left]) > abs(arr[right]):

            result[index] = arr[left] * arr[left]
            left += 1

        else:

            result[index] = arr[right] * arr[right]
            right -= 1

        index -= 1

    return result


# ------------------------------------------------------------
# 11. Dutch National Flag
# (Sort 0s, 1s and 2s)
# ------------------------------------------------------------
# Example:
# [2,0,2,1,1,0]
#
# Output:
# [0,0,1,1,2,2]
#
# Idea:
# Three pointers:
# low, mid, high
# ------------------------------------------------------------

def sort_colors(arr):

    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:

        if arr[mid] == 0:

            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:

            mid += 1

        else:

            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


# ------------------------------------------------------------
# 12. Container With Most Water
# ------------------------------------------------------------
# Example:
# [1,8,6,2,5,4,8,3,7]
#
# Output:
# 49
#
# Idea:
# Move pointer having smaller height.
# ------------------------------------------------------------

def max_area(height):

    left = 0
    right = len(height) - 1

    maximum = 0

    while left < right:

        width = right - left

        area = min(height[left], height[right]) * width

        maximum = max(maximum, area)

        if height[left] < height[right]:

            left += 1

        else:

            right -= 1

    return maximum


# ============================================================
# Driver Code
# ============================================================

arr1 = [-7,-3,2,3,11]

print("Sorted Squares :")
print(sorted_squares(arr1))

print()

arr2 = [2,0,2,1,1,0]

print("Dutch National Flag :")
print(sort_colors(arr2))

print()

arr3 = [1,8,6,2,5,4,8,3,7]

print("Container With Most Water :")
print(max_area(arr3))


# ============================================================
# Expected Output
# ============================================================

# Sorted Squares :
# [4,9,9,49,121]

# Dutch National Flag :
# [0,0,1,1,2,2]

# Container With Most Water :
# 49


# ============================================================
# Complexity
# ============================================================

# Sorted Squares              O(n)     O(n)

# Dutch National Flag         O(n)     O(1)

# Container Most Water        O(n)     O(1)


# ============================================================
# Frequently Asked
# ============================================================

# ✅ TCS
# ✅ Infosys
# ✅ Accenture
# ✅ Capgemini
# ✅ Cognizant
# ✅ IBM
# ✅ Deloitte
# ✅ Wipro
# ✅ HCL
# ✅ LTIMindtree
# ✅ Hexaware
# ✅ Cyntexa

# ============================================================
# TWO POINTER PATTERN COMPLETE ✅
# ============================================================
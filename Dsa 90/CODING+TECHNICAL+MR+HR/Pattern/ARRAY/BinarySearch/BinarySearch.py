# ============================================================
# BINARY SEARCH PATTERN - Batch 1
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(log n)
# Space: O(1)
# ============================================================


# ------------------------------------------------------------
# 1. Binary Search
# ------------------------------------------------------------
# Example:
# [2,4,6,8,10,12]
# Target = 8
#
# Output:
# 3
# ------------------------------------------------------------

def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# ------------------------------------------------------------
# 2. First Occurrence
# ------------------------------------------------------------
# Example:
# [2,4,4,4,6,8]
#
# Target = 4
#
# Output:
# 1
# ------------------------------------------------------------

def first_occurrence(arr, target):

    left = 0
    right = len(arr) - 1

    answer = -1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:

            answer = mid
            right = mid - 1

        elif arr[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return answer


# ------------------------------------------------------------
# 3. Last Occurrence
# ------------------------------------------------------------
# Example:
# [2,4,4,4,6,8]
#
# Target = 4
#
# Output:
# 3
# ------------------------------------------------------------

def last_occurrence(arr, target):

    left = 0
    right = len(arr) - 1

    answer = -1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:

            answer = mid
            left = mid + 1

        elif arr[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return answer


# ------------------------------------------------------------
# 4. Count Occurrence
# ------------------------------------------------------------
# Example:
# [2,4,4,4,6,8]
#
# Target = 4
#
# Output:
# 3
# ------------------------------------------------------------

def count_occurrence(arr, target):

    first = first_occurrence(arr, target)

    if first == -1:
        return 0

    last = last_occurrence(arr, target)

    return last - first + 1


# ============================================================
# Driver Code
# ============================================================

arr1 = [2,4,6,8,10,12]

print("Binary Search :")
print(binary_search(arr1,8))

print()

arr2 = [2,4,4,4,6,8]

print("First Occurrence :")
print(first_occurrence(arr2,4))

print()

print("Last Occurrence :")
print(last_occurrence(arr2,4))

print()

print("Count Occurrence :")
print(count_occurrence(arr2,4))


# ============================================================
# Expected Output
# ============================================================

# Binary Search :
# 3

# First Occurrence :
# 1

# Last Occurrence :
# 3

# Count Occurrence :
# 3


# ============================================================
# Complexity
# ============================================================

# Binary Search          O(log n)   O(1)

# First Occurrence       O(log n)   O(1)

# Last Occurrence        O(log n)   O(1)

# Count Occurrence       O(log n)   O(1)

# ============================================================

# ============================================================
# BINARY SEARCH PATTERN - Batch 2
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(log n)
# Space: O(1)
# ============================================================


# ------------------------------------------------------------
# 5. Lower Bound
# ------------------------------------------------------------
# Smallest index such that arr[index] >= target
#
# Example:
# [1,2,4,4,5,7]
# Target = 4
#
# Output:
# 2
# ------------------------------------------------------------

def lower_bound(arr, target):

    left = 0
    right = len(arr) - 1

    answer = len(arr)

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] >= target:

            answer = mid
            right = mid - 1

        else:

            left = mid + 1

    return answer


# ------------------------------------------------------------
# 6. Upper Bound
# ------------------------------------------------------------
# Smallest index such that arr[index] > target
#
# Example:
# [1,2,4,4,5,7]
# Target = 4
#
# Output:
# 4
# ------------------------------------------------------------

def upper_bound(arr, target):

    left = 0
    right = len(arr) - 1

    answer = len(arr)

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] > target:

            answer = mid
            right = mid - 1

        else:

            left = mid + 1

    return answer


# ------------------------------------------------------------
# 7. Floor
# ------------------------------------------------------------
# Largest value <= target
#
# Example:
# [2,4,6,8,10]
# Target = 7
#
# Output:
# 6
# ------------------------------------------------------------

def floor_value(arr, target):

    left = 0
    right = len(arr) - 1

    answer = -1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] <= target:

            answer = arr[mid]
            left = mid + 1

        else:

            right = mid - 1

    return answer


# ------------------------------------------------------------
# 8. Ceil
# ------------------------------------------------------------
# Smallest value >= target
#
# Example:
# [2,4,6,8,10]
# Target = 7
#
# Output:
# 8
# ------------------------------------------------------------

def ceil_value(arr, target):

    left = 0
    right = len(arr) - 1

    answer = -1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] >= target:

            answer = arr[mid]
            right = mid - 1

        else:

            left = mid + 1

    return answer


# ============================================================
# Driver Code
# ============================================================

arr1 = [1,2,4,4,5,7]

print("Lower Bound :")
print(lower_bound(arr1,4))

print()

print("Upper Bound :")
print(upper_bound(arr1,4))

print()

arr2 = [2,4,6,8,10]

print("Floor :")
print(floor_value(arr2,7))

print()

print("Ceil :")
print(ceil_value(arr2,7))



# similarity
'''
1.bs same
2.fo arr[mid] == t: ans = mid r = m - 1  and ll same like bs
3.ls arr[mid] == t ans = mid l = m + 1 and all same like bs
4.count o if first == -1 return 0 otherwise return lo - fo + 1
5.lower bound ans = len(arr) arr[m] >=target:ans = m nd r = m - 1 else : l = m+ 1
6.upper bound a[m] > t: ans = mid r = m - 1 else l = m + 1
7.flor vale <= ta: ans = mid ans = len(arr) l = m + 1 else r m -1
8.ciel value >= target : ans = mid r = m - 1 
'''

# ============================================================
# Expected Output
# ============================================================

# Lower Bound :
# 2

# Upper Bound :
# 4

# Floor :
# 6

# Ceil :
# 8


# ============================================================
# Complexity
# ============================================================

# Lower Bound        O(log n)   O(1)

# Upper Bound        O(log n)   O(1)

# Floor              O(log n)   O(1)

# Ceil               O(log n)   O(1)

# ============================================================

# ============================================================
# BINARY SEARCH PATTERN - Batch 3
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(log n)
# Space: O(1)
# ============================================================


# ------------------------------------------------------------
# 9. Search Insert Position
# ------------------------------------------------------------
# Example:
# [1,3,5,6]
# Target = 2
#
# Output:
# 1
# ------------------------------------------------------------

def search_insert(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return left


# ------------------------------------------------------------
# 10. Peak Element
# ------------------------------------------------------------
# Example:
# [1,2,3,1]
#
# Output:
# 2
# (Index of Peak)
# ------------------------------------------------------------

def peak_element(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:

            left = mid + 1

        else:

            right = mid

    return left


# ------------------------------------------------------------
# 11. Square Root (Integer)
# ------------------------------------------------------------
# Example:
# 28
#
# Output:
# 5
# ------------------------------------------------------------

def square_root(n):

    left = 0
    right = n

    answer = 0

    while left <= right:

        mid = left + (right - left) // 2

        if mid * mid <= n:

            answer = mid
            left = mid + 1

        else:

            right = mid - 1

    return answer


# ============================================================
# Driver Code
# ============================================================

arr1 = [1,3,5,6]

print("Search Insert Position :")
print(search_insert(arr1,2))

print()

arr2 = [1,2,3,1]

print("Peak Element Index :")
print(peak_element(arr2))

print()

print("Square Root :")
print(square_root(28))


# ============================================================
# Expected Output
# ============================================================

# Search Insert Position :
# 1

# Peak Element Index :
# 2

# Square Root :
# 5


# ============================================================
# Complexity
# ============================================================

# Search Insert Position      O(log n)   O(1)

# Peak Element                O(log n)   O(1)

# Square Root                 O(log n)   O(1)

# ============================================================

# ============================================================
# BINARY SEARCH PATTERN - Batch 4 (Bonus)
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(log n)
# Space: O(1)
# ============================================================


# ------------------------------------------------------------
# 12. Search in Rotated Sorted Array
# ------------------------------------------------------------
# Example:
# [4,5,6,7,0,1,2]
# Target = 0
#
# Output:
# 4
# ------------------------------------------------------------

def search_rotated(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        # Left Half Sorted
        if arr[left] <= arr[mid]:

            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right Half Sorted
        else:

            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# ------------------------------------------------------------
# 13. Minimum in Rotated Sorted Array
# ------------------------------------------------------------
# Example:
# [4,5,6,7,0,1,2]
#
# Output:
# 0
# ------------------------------------------------------------

def minimum_rotated(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        mid = left + (right - left) // 2

        if arr[mid] > arr[right]:

            left = mid + 1

        else:

            right = mid

    return arr[left]


# ------------------------------------------------------------
# 14. Single Element in Sorted Array
# ------------------------------------------------------------
# Example:
# [1,1,2,3,3,4,4]
#
# Output:
# 2
# ------------------------------------------------------------

def single_element(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        mid = left + (right - left) // 2

        if mid % 2 == 1:
            mid -= 1

        if arr[mid] == arr[mid + 1]:

            left = mid + 2

        else:

            right = mid

    return arr[left]


# ------------------------------------------------------------
# 15. Binary Search on Answer
# (Minimum Speed Example)
# ------------------------------------------------------------
# Example:
# piles = [3,6,7,11]
# hours = 8
#
# Output:
# 4
# ------------------------------------------------------------

def minimum_speed(piles, hours):

    def possible(speed):

        total = 0

        for pile in piles:

            total += (pile + speed - 1) // speed

        return total <= hours

    left = 1
    right = max(piles)

    answer = right

    while left <= right:

        mid = left + (right - left) // 2

        if possible(mid):

            answer = mid
            right = mid - 1

        else:

            left = mid + 1

    return answer


# ============================================================
# Driver Code
# ============================================================

arr1 = [4,5,6,7,0,1,2]

print("Search Rotated Array :")
print(search_rotated(arr1,0))

print()

print("Minimum In Rotated Array :")
print(minimum_rotated(arr1))

print()

arr2 = [1,1,2,3,3,4,4]

print("Single Element :")
print(single_element(arr2))

print()

piles = [3,6,7,11]

print("Binary Search On Answer :")
print(minimum_speed(piles,8))


# ============================================================
# Expected Output
# ============================================================

# Search Rotated Array :
# 4

# Minimum In Rotated Array :
# 0

# Single Element :
# 2

# Binary Search On Answer :
# 4


# ============================================================
# Complexity
# ============================================================

# Search Rotated Array          O(log n)     O(1)

# Minimum Rotated Array         O(log n)     O(1)

# Single Element                O(log n)     O(1)

# Binary Search On Answer       O(n log m)   O(1)
# m = maximum value in array

# ============================================================
# BINARY SEARCH PATTERN COMPLETE ✅
# ============================================================


# ==========================================
# Batch 1 - Traversal Pattern
# ==========================================

# ------------------------------------------
# 1. Check Array Sorted
# Time: O(n)
# Space: O(1)
# ------------------------------------------

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


# ------------------------------------------
# 2. Maximum Consecutive 1s
# Time: O(n)
# Space: O(1)
# ------------------------------------------

def max_consecutive_ones(arr):
    count = 0
    maximum = 0

    for num in arr:
        if num == 1:
            count += 1
            maximum = max(maximum, count)
        else:
            count = 0

    return maximum


# ------------------------------------------
# 3. Move Zeros to End
# Time: O(n)
# Space: O(1)
# ------------------------------------------

def move_zeros(arr):

    index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1

    return arr


# ------------------------------------------
# 4. Running Sum
# Time: O(n)
# Space: O(1)
# ------------------------------------------

def running_sum(arr):

    for i in range(1, len(arr)):
        arr[i] += arr[i-1]

    return arr


# ------------------------------------------
# 5. Prefix Sum
# Time: O(n)
# Space: O(n)
# ------------------------------------------

def prefix_sum(arr):

    prefix = [0] * len(arr)

    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix


# ==========================================
# Driver Code
# ==========================================

arr1 = [1,2,3,4,5]
print("Sorted :", is_sorted(arr1))

arr2 = [1,1,0,1,1,1]
print("Maximum Consecutive 1s :", max_consecutive_ones(arr2))

arr3 = [0,1,0,3,12]
print("Move Zeros :", move_zeros(arr3))

arr4 = [1,2,3,4]
print("Running Sum :", running_sum(arr4.copy()))

arr5 = [2,4,6,8]
print("Prefix Sum :", prefix_sum(arr5))


# ==========================================
# Output
# ==========================================
#
# Sorted : True
# Maximum Consecutive 1s : 3
# Move Zeros : [1, 3, 12, 0, 0]
# Running Sum : [1, 3, 6, 10]
# Prefix Sum : [2, 6, 12, 20]
#
# ==========================================

# ============================================================
# Batch 2 - Traversal Pattern
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(1) / O(n)
# ============================================================


# ------------------------------------------------------------
# 6. Find Duplicate
# ------------------------------------------------------------
# Problem:
# Find the duplicate element.
#
# Example:
# [1,3,4,2,2]
#
# Output:
# 2
#
# Approach:
# Use HashSet
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def find_duplicate(arr):

    seen = set()

    for num in arr:

        if num in seen:
            return num

        seen.add(num)

    return -1


# ------------------------------------------------------------
# 7. Missing and Repeating Number
# ------------------------------------------------------------
# Problem:
# One number is missing and one number is repeated.
#
# Example:
# [1,2,2,4,5]
#
# Missing = 3
# Repeating = 2
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def missing_repeating(arr):

    n = len(arr)

    seen = set()

    repeating = -1

    for num in arr:

        if num in seen:
            repeating = num
        else:
            seen.add(num)

    missing = -1

    for i in range(1, n + 1):

        if i not in seen:
            missing = i
            break

    return missing, repeating


# ------------------------------------------------------------
# 8. Frequency Count
# ------------------------------------------------------------
# Problem:
# Count frequency of every element.
#
# Example:
# [1,2,2,3,3,3]
#
# Output:
# {1:1,2:2,3:3}
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def frequency_count(arr):

    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    return frequency


# ------------------------------------------------------------
# 9. Count Unique Elements
# ------------------------------------------------------------
# Problem:
# Count elements occurring only once.
#
# Example:
# [1,2,2,3,4,4]
#
# Output:
# 2
#
# Unique Elements:
# 1
# 3
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def count_unique(arr):

    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    count = 0

    for value in frequency.values():

        if value == 1:
            count += 1

    return count


# ------------------------------------------------------------
# 10. Largest Odd Element
# ------------------------------------------------------------
# Problem:
# Find largest odd number.
#
# Example:
# [12,5,19,8,17]
#
# Output:
# 19
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def largest_odd(arr):

    largest = float("-inf")

    for num in arr:

        if num % 2 != 0 and num > largest:
            largest = num

    if largest == float("-inf"):
        return -1

    return largest


# ============================================================
# Driver Code
# ============================================================

arr1 = [1,3,4,2,2]

arr2 = [1,2,2,4,5]

arr3 = [1,2,2,3,3,3]

arr4 = [1,2,2,3,4,4]

arr5 = [12,5,19,8,17]


print("Duplicate :", find_duplicate(arr1))

print("Missing & Repeating :", missing_repeating(arr2))

print("Frequency Count :", frequency_count(arr3))

print("Unique Count :", count_unique(arr4))

print("Largest Odd :", largest_odd(arr5))


# ============================================================
# Expected Output
# ============================================================
#
# Duplicate : 2
#
# Missing & Repeating : (3, 2)
#
# Frequency Count : {1:1, 2:2, 3:3}
#
# Unique Count : 2
#
# Largest Odd : 19
#
# ============================================================
# Complexity
# ============================================================
#
# Find Duplicate            O(n)  O(n)
# Missing & Repeating       O(n)  O(n)
# Frequency Count           O(n)  O(n)
# Count Unique              O(n)  O(n)
# Largest Odd               O(n)  O(1)
#
# Frequently Asked:
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
# Batch 3 - Traversal Pattern (Final)
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(1)
# ============================================================


# ------------------------------------------------------------
# 11. Largest Even Element
# ------------------------------------------------------------
# Problem:
# Find the largest even element.
#
# Example:
# [11,8,15,20,7]
#
# Output:
# 20
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def largest_even(arr):

    largest = float("-inf")

    for num in arr:

        if num % 2 == 0 and num > largest:
            largest = num

    if largest == float("-inf"):
        return -1

    return largest


# ------------------------------------------------------------
# 12. Stock Buy & Sell (Single Transaction)
# ------------------------------------------------------------
# Problem:
# Buy once and sell once to maximize profit.
#
# Example:
# [7,1,5,3,6,4]
#
# Output:
# 5
#
# Buy = 1
# Sell = 6
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def max_profit(prices):

    minimum_price = prices[0]
    maximum_profit = 0

    for price in prices:

        if price < minimum_price:
            minimum_price = price

        profit = price - minimum_price

        if profit > maximum_profit:
            maximum_profit = profit

    return maximum_profit


# ------------------------------------------------------------
# 13. Find Peak Element (Linear Search)
# ------------------------------------------------------------
# Problem:
# Peak Element is greater than its neighbours.
#
# Example:
# [1,2,5,3,1]
#
# Output:
# 5
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def peak_element(arr):

    n = len(arr)

    # First Element
    if n == 1:
        return arr[0]

    if arr[0] > arr[1]:
        return arr[0]

    # Middle Elements
    for i in range(1, n-1):

        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return arr[i]

    # Last Element
    if arr[n-1] > arr[n-2]:
        return arr[n-1]

    return -1


# ------------------------------------------------------------
# 14. Third Largest Element
# ------------------------------------------------------------
# Problem:
# Find third largest unique element.
#
# Example:
# [10,40,20,30,50]
#
# Output:
# 30
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def third_largest(arr):

    first = float("-inf")
    second = float("-inf")
    third = float("-inf")

    for num in arr:

        if num > first:

            third = second
            second = first
            first = num

        elif num > second and num != first:

            third = second
            second = num

        elif num > third and num != second and num != first:

            third = num

    if third == float("-inf"):
        return -1

    return third


# ------------------------------------------------------------
# 15. Bonus - Smallest Positive Element
# ------------------------------------------------------------
# Problem:
# Find the smallest positive element.
#
# Example:
# [-5,-2,4,8,1]
#
# Output:
# 1
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def smallest_positive(arr):

    smallest = float("inf")

    for num in arr:

        if num > 0 and num < smallest:
            smallest = num

    if smallest == float("inf"):
        return -1

    return smallest


# ============================================================
# Driver Code
# ============================================================

arr1 = [11,8,15,20,7]

prices = [7,1,5,3,6,4]

arr3 = [1,2,5,3,1]

arr4 = [10,40,20,30,50]

arr5 = [-5,-2,4,8,1]


print("Largest Even :", largest_even(arr1))

print("Maximum Profit :", max_profit(prices))

print("Peak Element :", peak_element(arr3))

print("Third Largest :", third_largest(arr4))

print("Smallest Positive :", smallest_positive(arr5))


# ============================================================
# Expected Output
# ============================================================
#
# Largest Even : 20
#
# Maximum Profit : 5
#
# Peak Element : 5
#
# Third Largest : 30
#
# Smallest Positive : 1
#
# ============================================================
# Complexity
# ============================================================
#
# Largest Even          O(n)  O(1)
# Stock Buy & Sell      O(n)  O(1)
# Peak Element          O(n)  O(1)
# Third Largest         O(n)  O(1)
# Smallest Positive     O(n)  O(1)
#
# Frequently Asked:
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
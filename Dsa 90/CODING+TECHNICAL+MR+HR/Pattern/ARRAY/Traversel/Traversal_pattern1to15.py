# ==========================================
# TRAVERSAL PATTERN (Service-Based Companies)
# Companies: TCS | Infosys | Accenture | Capgemini | Cognizant | IBM | Deloitte | Cyntexa
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==========================================

# Example Input
arr = [12, 45, 7, 89, 34, 89, 5]

# --------------------------------------------------
# 1. Linear Search
# --------------------------------------------------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i          # Return first occurrence index
    return -1                 # Element not found


# --------------------------------------------------
# 2. Maximum Element
# --------------------------------------------------
def maximum_element(arr):
    maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num

    return maximum


# --------------------------------------------------
# 3. Minimum Element
# --------------------------------------------------
def minimum_element(arr):
    minimum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num

    return minimum


# --------------------------------------------------
# 4. Second Largest Element
# (Handles Duplicate Values)
# --------------------------------------------------
def second_largest(arr):
    first = float('-inf')
    second = float('-inf')

    for num in arr:

        if num > first:
            second = first
            first = num

        elif num > second and num != first:
            second = num

    if second == float('-inf'):
        return "Second Largest Doesn't Exist"

    return second


# --------------------------------------------------
# 5. Second Smallest Element
# (Handles Duplicate Values)
# --------------------------------------------------
def second_smallest(arr):
    first = float('inf')
    second = float('inf')

    for num in arr:

        if num < first:
            second = first
            first = num

        elif num < second and num != first:
            second = num

    if second == float('inf'):
        return "Second Smallest Doesn't Exist"

    return second


# --------------------------------------------------
# Driver Code
# --------------------------------------------------
target = 89

print("Array :", arr)

print("Linear Search :", linear_search(arr, target))
print("Maximum Element :", maximum_element(arr))
print("Minimum Element :", minimum_element(arr))
print("Second Largest :", second_largest(arr))
print("Second Smallest :", second_smallest(arr))


# ============================================================
# TRAVERSAL PATTERN (Service-Based Companies)
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Difficulty : Easy
# Pattern    : Traversal
# Time       : O(n)
# Space      : O(1)
# ============================================================

arr = [12, 45, 7, 89, 34, 5]

# ------------------------------------------------------------
# 6. Largest Difference
# ------------------------------------------------------------
# Problem:
# Find the largest difference between maximum and minimum element.
#
# Why?
# Used in salary analysis, stock prices, marks comparison, etc.
#
# Approach:
# Find maximum and minimum in one traversal.
# Difference = Maximum - Minimum
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def largest_difference(arr):

    maximum = arr[0]
    minimum = arr[0]

    for num in arr:

        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    return maximum - minimum


# ------------------------------------------------------------
# 7. Count Even Numbers
# ------------------------------------------------------------
# Problem:
# Count total even numbers in an array.
#
# Why?
# Used in filtering datasets and number analysis.
#
# Even Number:
# Number divisible by 2.
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def count_even(arr):

    count = 0

    for num in arr:

        if num % 2 == 0:
            count += 1

    return count


# ------------------------------------------------------------
# 8. Count Odd Numbers
# ------------------------------------------------------------
# Problem:
# Count total odd numbers.
#
# Why?
# Used in statistics and data processing.
#
# Odd Number:
# Number NOT divisible by 2.
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def count_odd(arr):

    count = 0

    for num in arr:

        if num % 2 != 0:
            count += 1

    return count


# ------------------------------------------------------------
# 9. Sum of Array
# ------------------------------------------------------------
# Problem:
# Find total sum of all elements.
#
# Why?
# Used in average, statistics, reports, finance.
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def array_sum(arr):

    total = 0

    for num in arr:
        total += num

    return total


# ------------------------------------------------------------
# 10. Average of Array
# ------------------------------------------------------------
# Problem:
# Find average of all numbers.
#
# Formula:
# Average = Sum / Number of Elements
#
# Why?
# Used in marks, salary, analytics.
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def average(arr):

    total = 0

    for num in arr:
        total += num

    return total / len(arr)


# ------------------------------------------------------------
# 11. Missing Number
# ------------------------------------------------------------
# Problem:
# Array contains numbers from 1 to n.
# One number is missing.
#
# Example:
# [1,2,3,5]
#
# Missing = 4
#
# Optimized Idea:
#
# Expected Sum = n*(n+1)//2
#
# Actual Sum = Sum of Array
#
# Missing = Expected - Actual
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def missing_number(arr):

    n = len(arr) + 1

    expected_sum = n * (n + 1) // 2
    
    actual_sum = 0

    for num in arr:
        actual_sum += num

    return expected_sum - actual_sum


# ------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------

print("Array :", arr)

print("Largest Difference :", largest_difference(arr))
print("Count Even :", count_even(arr))
print("Count Odd :", count_odd(arr))
print("Sum of Array :", array_sum(arr))
print("Average :", average(arr))

missing_arr = [1, 2, 3, 5, 6]

print("Missing Number Array :", missing_arr)
print("Missing Number :", missing_number(missing_arr))


# ============================================================
# Expected Output
# ============================================================
#
# Array : [12, 45, 7, 89, 34, 5]
#
# Largest Difference : 84
#
# Count Even : 2
#
# Count Odd : 4
#
# Sum of Array : 192
#
# Average : 32.0
#
# Missing Number Array : [1, 2, 3, 5, 6]
#
# Missing Number : 4
#
# ============================================================
# Interview Complexity
# ============================================================
#
# Largest Difference -> O(n), O(1)
# Count Even         -> O(n), O(1)
# Count Odd          -> O(n), O(1)
# Sum of Array       -> O(n), O(1)
# Average            -> O(n), O(1)
# Missing Number     -> O(n), O(1)
#
# Frequently Asked In:
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
# TRAVERSAL PATTERN (Service-Based Companies)
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time Complexity : O(n)
# Space Complexity: O(1) / O(n)
# ============================================================


# ------------------------------------------------------------
# 12. First Non-Repeating Element
# ------------------------------------------------------------
# Problem:
# Find the first element that appears only once.
#
# Example:
# [4,5,1,2,0,4,1,2]
#
# Output:
# 5
#
# Why?
# Used in log analysis, unique user detection,
# first unique transaction, etc.
#
# Approach:
# 1. Count frequency of every element.
# 2. Traverse again.
# 3. First frequency == 1 is answer.
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def first_non_repeating(arr):

    frequency = {}

    # Count Frequency
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    # Find First Unique
    for num in arr:
        if frequency[num] == 1:
            return num

    return -1


# ------------------------------------------------------------
# 13. Majority Element
# ------------------------------------------------------------
# Problem:
# Find element appearing more than n//2 times.
#
# Example:
# [2,2,1,2,3,2,2]
#
# Output:
# 2
#
# Optimized:
# Boyer Moore Voting Algorithm
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def majority_element(arr):

    candidate = None
    count = 0

    # Find Candidate
    for num in arr:

        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    # Verify Candidate
    frequency = 0

    for num in arr:
        if num == candidate:
            frequency += 1

    if frequency > len(arr) // 2:
        return candidate

    return -1


# ------------------------------------------------------------
# 14. Leaders in Array
# ------------------------------------------------------------
# Problem:
# Leader means every element greater than all
# elements on its right.
#
# Example:
# [16,17,4,3,5,2]
#
# Output:
# [17,5,2]
#
# Approach:
# Traverse from Right
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def leaders_in_array(arr):

    leaders = []

    maximum = arr[-1]

    leaders.append(maximum)

    for i in range(len(arr)-2, -1, -1):

        if arr[i] > maximum:
            maximum = arr[i]
            leaders.append(maximum)

    leaders.reverse()

    return leaders


# ------------------------------------------------------------
# 15. Equilibrium Index
# ------------------------------------------------------------
# Problem:
# Left Sum == Right Sum
#
# Example:
# [1,3,5,2,2]
#
# Output:
# 2
#
# Left Sum = 4
# Right Sum = 4
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def equilibrium_index(arr):

    total_sum = sum(arr)

    left_sum = 0

    for i in range(len(arr)):

        total_sum -= arr[i]

        if left_sum == total_sum:
            return i

        left_sum += arr[i]

    return -1


# ============================================================
# Driver Code
# ============================================================

arr1 = [4,5,1,2,0,4,1,2]

arr2 = [2,2,1,2,3,2,2]

arr3 = [16,17,4,3,5,2]

arr4 = [1,3,5,2,2]


print("First Non-Repeating :", first_non_repeating(arr1))

print("Majority Element :", majority_element(arr2))

print("Leaders in Array :", leaders_in_array(arr3))

print("Equilibrium Index :", equilibrium_index(arr4))


# ============================================================
# Expected Output
# ============================================================
#
# First Non-Repeating : 5
#
# Majority Element : 2
#
# Leaders in Array : [17, 5, 2]
#
# Equilibrium Index : 2
#
# ============================================================
# Interview Complexity
# ============================================================
#
# First Non-Repeating
# Time  : O(n)
# Space : O(n)
#
# Majority Element
# Time  : O(n)
# Space : O(1)
#
# Leaders in Array
# Time  : O(n)
# Space : O(n)
#
# Equilibrium Index
# Time  : O(n)
# Space : O(1)
#
# Frequently Asked In:
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
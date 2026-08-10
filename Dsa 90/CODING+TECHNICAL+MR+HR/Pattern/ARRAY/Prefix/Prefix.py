# ============================================================
# PREFIX SUM PATTERN - Batch 1
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# ============================================================


# ------------------------------------------------------------
# 1. Running Sum
# ------------------------------------------------------------
# Example:
# [1,2,3,4]
#
# Output:
# [1,3,6,10]
# ------------------------------------------------------------

def running_sum(arr):

    result = []

    total = 0

    for num in arr:

        total += num

        result.append(total)

    return result


# ------------------------------------------------------------
# 2. Prefix Sum Array
# ------------------------------------------------------------
# Example:
# [2,4,6,8]
#
# Output:
# [2,6,12,20]
# ------------------------------------------------------------

def prefix_sum(arr):

    prefix = [0] * len(arr)

    prefix[0] = arr[0]

    for i in range(1, len(arr)):

        prefix[i] = prefix[i-1] + arr[i]

    return prefix


# ------------------------------------------------------------
# 3. Range Sum Query
# ------------------------------------------------------------
# Example:
# Array = [2,4,6,8,10]
#
# Left = 1
# Right = 3
#
# Output:
# 18
# ------------------------------------------------------------

def range_sum_query(arr, left, right):

    prefix = prefix_sum(arr)

    if left == 0:
        return prefix[right]

    return prefix[right] - prefix[left-1]


# ============================================================
# Driver Code
# ============================================================

arr1 = [1,2,3,4]

print("Running Sum :")
print(running_sum(arr1))

print()

arr2 = [2,4,6,8]

print("Prefix Sum :")
print(prefix_sum(arr2))

print()

arr3 = [2,4,6,8,10]

print("Range Sum Query :")
print(range_sum_query(arr3,1,3))


# ============================================================
# Expected Output
# ============================================================

# Running Sum :
# [1,3,6,10]

# Prefix Sum :
# [2,6,12,20]

# Range Sum Query :
# 18


# ============================================================
# Complexity
# ============================================================

# Running Sum          O(n)   O(n)

# Prefix Sum           O(n)   O(n)

# Range Sum Query      O(n)*  O(n)
#
# *After Prefix Array is built,
# each query runs in O(1).
# ============================================================

# ============================================================
# PREFIX SUM PATTERN - Batch 2
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# ============================================================


# ------------------------------------------------------------
# 4. Pivot Index
# ------------------------------------------------------------
# Example:
# [1,7,3,6,5,6]
#
# Output:
# 3
#
# Left Sum  = Right Sum
# ------------------------------------------------------------

def pivot_index(arr):

    total = sum(arr)

    left_sum = 0

    for i in range(len(arr)):

        right_sum = total - left_sum - arr[i]

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1


# ------------------------------------------------------------
# 5. Product of Array Except Self
# ------------------------------------------------------------
# Example:
# [1,2,3,4]
#
# Output:
# [24,12,8,6]
#
# Without Division
# ------------------------------------------------------------

def product_except_self(arr):

    n = len(arr)

    answer = [1] * n

    prefix = 1

    for i in range(n):

        answer[i] = prefix
        prefix *= arr[i]

    suffix = 1

    for i in range(n - 1, -1, -1):

        answer[i] *= suffix
        suffix *= arr[i]

    return answer


# ------------------------------------------------------------
# 6. Subarray Sum Equals K
# ------------------------------------------------------------
# Example:
# [1,1,1]
#
# K = 2
#
# Output:
# 2
#
# Prefix Sum + HashMap
# ------------------------------------------------------------

def subarray_sum_k(arr, k):

    prefix_sum = 0

    count = 0

    frequency = {0: 1}

    for num in arr:

        prefix_sum += num

        if prefix_sum - k in frequency:
            count += frequency[prefix_sum - k]

        frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

    return count


# ============================================================
# Driver Code
# ============================================================

arr1 = [1,7,3,6,5,6]

print("Pivot Index :")
print(pivot_index(arr1))

print()

arr2 = [1,2,3,4]

print("Product Except Self :")
print(product_except_self(arr2))

print()

arr3 = [1,1,1]

print("Subarray Sum = K :")
print(subarray_sum_k(arr3,2))


# ============================================================
# Expected Output
# ============================================================

# Pivot Index :
# 3

# Product Except Self :
# [24,12,8,6]

# Subarray Sum = K :
# 2


# ============================================================
# Complexity
# ============================================================

# Pivot Index            O(n)   O(1)

# Product Except Self    O(n)   O(1)

# Subarray Sum = K       O(n)   O(n)

# ============================================================

# ============================================================
# PREFIX SUM PATTERN - Batch 3 (Final)
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# ============================================================


# ------------------------------------------------------------
# 7. Difference Array
# ------------------------------------------------------------
# Example:
# Array = [10,20,30,40]
#
# Output:
# [10,10,10,10]
#
# Difference[i] = arr[i] - arr[i-1]
# ------------------------------------------------------------

def difference_array(arr):

    if not arr:
        return []

    diff = [0] * len(arr)

    diff[0] = arr[0]

    for i in range(1, len(arr)):

        diff[i] = arr[i] - arr[i-1]

    return diff


# ------------------------------------------------------------
# 8. Range Update Using Difference Array
# ------------------------------------------------------------
# Example:
# n = 5
#
# Update:
# (1,3,+2)
#
# Output:
# [0,2,2,2,0]
# ------------------------------------------------------------

def range_update(n, updates):

    diff = [0] * (n + 1)

    for left, right, value in updates:

        diff[left] += value

        if right + 1 < len(diff):
            diff[right + 1] -= value

    result = [0] * n

    current = 0

    for i in range(n):

        current += diff[i]

        result[i] = current

    return result


# ============================================================
# Driver Code
# ============================================================

arr = [10,20,30,40]

print("Difference Array :")
print(difference_array(arr))

print()

updates = [
    (1,3,2)
]

print("Range Update :")
print(range_update(5, updates))


# ============================================================
# Expected Output
# ============================================================

# Difference Array :
# [10,10,10,10]

# Range Update :
# [0,2,2,2,0]


# ============================================================
# Complexity
# ============================================================

# Difference Array      O(n)   O(n)

# Range Update          O(n+m) O(n)
# n = array size
# m = number of updates

# ============================================================
# PREFIX SUM PATTERN COMPLETE ✅
# ============================================================
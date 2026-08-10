# ============================================================
# SLIDING WINDOW PATTERN - Batch 1
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(1)
# ============================================================


# ------------------------------------------------------------
# 1. Maximum Sum of Size K
# ------------------------------------------------------------
# Example:
# Array = [2,1,5,1,3,2]
# K = 3
#
# Output:
# 9
#
# Window:
# [2,1,5] = 8
# [1,5,1] = 7
# [5,1,3] = 9  <-- Maximum
# [1,3,2] = 6
# ------------------------------------------------------------

def maximum_sum_k(arr, k):

    window_sum = sum(arr[:k])
    maximum = window_sum

    for i in range(k, len(arr)):

        window_sum += arr[i]
        window_sum -= arr[i-k]

        maximum = max(maximum, window_sum)

    return maximum


# ------------------------------------------------------------
# 2. Minimum Sum Window of Size K
# ------------------------------------------------------------
# Example:
# Array = [2,1,5,1,3,2]
# K = 3
#
# Output:
# 6
#
# Window:
# [1,3,2]
# ------------------------------------------------------------

def minimum_sum_k(arr, k):

    window_sum = sum(arr[:k])
    minimum = window_sum

    for i in range(k, len(arr)):

        window_sum += arr[i]
        window_sum -= arr[i-k]

        minimum = min(minimum, window_sum)

    return minimum


# ------------------------------------------------------------
# 3. Maximum Average Subarray of Size K
# ------------------------------------------------------------
# Example:
# Array = [1,12,-5,-6,50,3]
# K = 4
#
# Output:
# 12.75
# ------------------------------------------------------------

def maximum_average(arr, k):

    window_sum = sum(arr[:k])
    maximum = window_sum

    for i in range(k, len(arr)):

        window_sum += arr[i]
        window_sum -= arr[i-k]

        maximum = max(maximum, window_sum)

    return maximum / k


# ============================================================
# Driver Code
# ============================================================

arr1 = [2,1,5,1,3,2]

print("Maximum Sum of K :")
print(maximum_sum_k(arr1,3))

print()

print("Minimum Sum of K :")
print(minimum_sum_k(arr1,3))

print()

arr2 = [1,12,-5,-6,50,3]

print("Maximum Average :")
print(maximum_average(arr2,4))


# ============================================================
# Expected Output
# ============================================================

# Maximum Sum of K :
# 9

# Minimum Sum of K :
# 6

# Maximum Average :
# 12.75


# ============================================================
# Complexity
# ============================================================

# Maximum Sum of K      O(n)   O(1)

# Minimum Sum of K      O(n)   O(1)

# Maximum Average       O(n)   O(1)

# ============================================================

# ============================================================
# SLIDING WINDOW PATTERN - Batch 2
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(k)
# ============================================================


# ------------------------------------------------------------
# 4. First Negative Number in Every Window of Size K
# ------------------------------------------------------------
# Example:
# Array = [12,-1,-7,8,-15,30,16,28]
# K = 3
#
# Output:
# [-1,-1,-7,-15,-15,0]
# ------------------------------------------------------------

from collections import deque

def first_negative(arr, k):

    negatives = deque()
    result = []

    for i in range(len(arr)):

        if arr[i] < 0:
            negatives.append(i)

        while negatives and negatives[0] <= i - k:
            negatives.popleft()

        if i >= k - 1:

            if negatives:
                result.append(arr[negatives[0]])
            else:
                result.append(0)

    return result


# ------------------------------------------------------------
# 5. Count Distinct Elements in Every Window
# ------------------------------------------------------------
# Example:
# Array = [1,2,1,3,4,2,3]
# K = 4
#
# Output:
# [3,4,4,3]
# ------------------------------------------------------------

def count_distinct(arr, k):

    frequency = {}
    result = []

    for i in range(k):
        frequency[arr[i]] = frequency.get(arr[i], 0) + 1

    result.append(len(frequency))

    for i in range(k, len(arr)):

        left = arr[i-k]

        frequency[left] -= 1

        if frequency[left] == 0:
            del frequency[left]

        frequency[arr[i]] = frequency.get(arr[i], 0) + 1

        result.append(len(frequency))

    return result


# ------------------------------------------------------------
# 6. Maximum Consecutive Ones
# ------------------------------------------------------------
# Example:
# Array = [1,1,0,1,1,1]
#
# Output:
# 3
# ------------------------------------------------------------

def maximum_consecutive_ones(arr):

    maximum = 0
    count = 0

    for num in arr:

        if num == 1:
            count += 1
            maximum = max(maximum, count)
        else:
            count = 0

    return maximum


# ============================================================
# Driver Code
# ============================================================

arr1 = [12,-1,-7,8,-15,30,16,28]

print("First Negative In Every Window :")
print(first_negative(arr1,3))

print()

arr2 = [1,2,1,3,4,2,3]

print("Count Distinct In Every Window :")
print(count_distinct(arr2,4))

print()

arr3 = [1,1,0,1,1,1]

print("Maximum Consecutive Ones :")
print(maximum_consecutive_ones(arr3))


# ============================================================
# Expected Output
# ============================================================

# First Negative In Every Window :
# [-1, -1, -7, -15, -15, 0]

# Count Distinct In Every Window :
# [3, 4, 4, 3]

# Maximum Consecutive Ones :
# 3


# ============================================================
# Complexity
# ============================================================

# First Negative Window      O(n)   O(k)

# Count Distinct Window      O(n)   O(k)

# Maximum Consecutive Ones   O(n)   O(1)

# ============================================================


# ============================================================
# SLIDING WINDOW PATTERN - Batch 3
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# ============================================================


# ------------------------------------------------------------
# 7. Longest Subarray With Sum K (Positive Numbers)
# ------------------------------------------------------------
# Example:
# Array = [1,2,1,1,1,3,2]
# K = 5
#
# Output:
# 4
# ------------------------------------------------------------

def longest_subarray_sum_k(arr, k):

    left = 0
    window_sum = 0
    maximum = 0

    for right in range(len(arr)):

        window_sum += arr[right]

        while window_sum > k:

            window_sum -= arr[left]
            left += 1

        if window_sum == k:
            maximum = max(maximum, right - left + 1)

    return maximum


# ------------------------------------------------------------
# 8. Smallest Window With Sum >= K
# ------------------------------------------------------------
# Example:
# Array = [2,3,1,2,4,3]
# K = 7
#
# Output:
# 2
# ------------------------------------------------------------

def smallest_window(arr, k):

    left = 0
    window_sum = 0
    minimum = float("inf")

    for right in range(len(arr)):

        window_sum += arr[right]

        while window_sum >= k:

            minimum = min(minimum, right - left + 1)

            window_sum -= arr[left]
            left += 1

    return minimum if minimum != float("inf") else 0


# ------------------------------------------------------------
# 9. Fruits Into Basket
# ------------------------------------------------------------
# Example:
# [1,2,1,2,3]
#
# Output:
# 4
# ------------------------------------------------------------

def fruits_into_basket(arr):

    left = 0
    frequency = {}
    maximum = 0

    for right in range(len(arr)):

        frequency[arr[right]] = frequency.get(arr[right], 0) + 1

        while len(frequency) > 2:

            frequency[arr[left]] -= 1

            if frequency[arr[left]] == 0:
                del frequency[arr[left]]

            left += 1

        maximum = max(maximum, right - left + 1)

    return maximum


# ============================================================
# Driver Code
# ============================================================

arr1 = [1,2,1,1,1,3,2]

print("Longest Subarray Sum K :")
print(longest_subarray_sum_k(arr1,5))

print()

arr2 = [2,3,1,2,4,3]

print("Smallest Window >= K :")
print(smallest_window(arr2,7))

print()

arr3 = [1,2,1,2,3]

print("Fruits Into Basket :")
print(fruits_into_basket(arr3))


# ============================================================
# Expected Output
# ============================================================

# Longest Subarray Sum K :
# 4

# Smallest Window >= K :
# 2

# Fruits Into Basket :
# 4


# ============================================================
# Complexity
# ============================================================

# Longest Subarray Sum K      O(n)   O(1)
# Smallest Window >= K        O(n)   O(1)
# Fruits Into Basket          O(n)   O(1)

# ============================================================


# ============================================================
# SLIDING WINDOW PATTERN - Batch 4 (Final)
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(n)
# ============================================================


# ------------------------------------------------------------
# 10. Longest Unique Substring (Longest Unique Window)
# ------------------------------------------------------------
# Example:
# String = "abcabcbb"
#
# Output:
# 3
#
# Explanation:
# Longest Unique Substring = "abc"
# Length = 3
#
# Idea:
# Expand window using right pointer.
# If duplicate character appears,
# shrink window from left until unique.
# ------------------------------------------------------------

def longest_unique_window(s):

    left = 0
    maximum = 0

    frequency = {}

    for right in range(len(s)):

        frequency[s[right]] = frequency.get(s[right], 0) + 1

        while frequency[s[right]] > 1:

            frequency[s[left]] -= 1

            if frequency[s[left]] == 0:
                del frequency[s[left]]

            left += 1

        maximum = max(maximum, right - left + 1)

    return maximum


# ============================================================
# Driver Code
# ============================================================

s1 = "abcabcbb"

print("Longest Unique Window :")


# Minimum Size Subarray Sum
# Longest Repeating Character Replacement
# Permutation in String
# Find All Anagrams in a String
# Maximum Number of Vowels in Substring of Size K
# Substrings of Size K With K Distinct Characters
# Longest Substring With At Most K Distinct Characters
# Longest Substring Without Repeating Characters (same pattern, different variation)
# Sliding Window Maximum (Deque based)


# ============================================================
# SLIDING WINDOW PATTERN - Bonus Batch
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# ============================================================


# ------------------------------------------------------------
# 11. Maximum Number of Vowels in Substring of Size K
# ------------------------------------------------------------
# Example:
# String = "abciiidef"
# K = 3
#
# Output:
# 3
# ------------------------------------------------------------

def max_vowels(s, k):

    vowels = {'a','e','i','o','u'}

    count = 0

    for i in range(k):

        if s[i] in vowels:
            count += 1

    maximum = count

    for i in range(k, len(s)):

        if s[i-k] in vowels:
            count -= 1

        if s[i] in vowels:
            count += 1

        maximum = max(maximum, count)

    return maximum


# ------------------------------------------------------------
# 12. Find All Anagrams
# ------------------------------------------------------------
# Example:
# s = "cbaebabacd"
# p = "abc"
#
# Output:
# [0,6]
# ------------------------------------------------------------

def find_anagrams(s, p):

    from collections import Counter

    result = []

    k = len(p)

    target = Counter(p)

    window = Counter(s[:k])

    if window == target:
        result.append(0)

    for i in range(k, len(s)):

        window[s[i-k]] -= 1

        if window[s[i-k]] == 0:
            del window[s[i-k]]

        window[s[i]] += 1

        if window == target:
            result.append(i-k+1)

    return result


# ------------------------------------------------------------
# 13. Permutation in String
# ------------------------------------------------------------
# Example:
# s1 = "ab"
# s2 = "eidbaooo"
#
# Output:
# True
# ------------------------------------------------------------

def check_permutation(s1, s2):

    from collections import Counter

    k = len(s1)

    target = Counter(s1)

    window = Counter(s2[:k])

    if window == target:
        return True

    for i in range(k, len(s2)):

        window[s2[i-k]] -= 1

        if window[s2[i-k]] == 0:
            del window[s2[i-k]]

        window[s2[i]] += 1

        if window == target:
            return True

    return False


# ------------------------------------------------------------
# 14. Longest Substring With At Most K Distinct Characters
# ------------------------------------------------------------
# Example:
# String = "eceba"
# K = 2
#
# Output:
# 3
# ------------------------------------------------------------

def longest_k_distinct(s, k):

    left = 0

    frequency = {}

    maximum = 0

    for right in range(len(s)):

        frequency[s[right]] = frequency.get(s[right],0) + 1

        while len(frequency) > k:

            frequency[s[left]] -= 1

            if frequency[s[left]] == 0:
                del frequency[s[left]]

            left += 1

        maximum = max(maximum, right-left+1)

    return maximum


# ============================================================
# Driver Code
# ============================================================

print("Maximum Vowels :")
print(max_vowels("abciiidef",3))

print()

print("Find All Anagrams :")
print(find_anagrams("cbaebabacd","abc"))

print()

print("Permutation In String :")
print(check_permutation("ab","eidbaooo"))

print()

print("Longest K Distinct Characters :")
print(longest_k_distinct("eceba",2))


# ============================================================
# Expected Output
# ============================================================

# Maximum Vowels :
# 3

# Find All Anagrams :
# [0, 6]

# Permutation In String :
# True

# Longest K Distinct Characters :
# 3


# ============================================================
# Complexity
# ============================================================

# Maximum Vowels                 O(n)   O(1)

# Find All Anagrams              O(n)   O(26)

# Permutation In String          O(n)   O(26)

# Longest K Distinct             O(n)   O(k)


# ============================================================
# Frequently Asked
# ============================================================

# ✅ Infosys
# ✅ Accenture
# ✅ Capgemini
# ✅ Cognizant
# ✅ IBM
# ✅ Deloitte
# ✅ TCS Digital
# ✅ LTIMindtree
# ✅ Hexaware
# ✅ Cyntexa

# ============================================================
# SLIDING WINDOW PATTERN COMPLETE ✅
# ============================================================
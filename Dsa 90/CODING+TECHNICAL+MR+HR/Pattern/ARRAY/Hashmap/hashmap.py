# ============================================================
# HASHMAP PATTERN - Batch 1
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(n)
# ============================================================


# ------------------------------------------------------------
# 1. Frequency Count
# ------------------------------------------------------------
# Example:
# [1,2,2,3,1,2]
#
# Output:
# {1:2, 2:3, 3:1}
# ------------------------------------------------------------

def frequency_count(arr):

    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    return frequency


# ------------------------------------------------------------
# 2. Contains Duplicate
# ------------------------------------------------------------
# Example:
# [1,2,3,1]
#
# Output:
# True
# ------------------------------------------------------------

def contains_duplicate(arr):

    visited = set()

    for num in arr:

        if num in visited:
            return True

        visited.add(num)

    return False


# ------------------------------------------------------------
# 3. Find Unique Elements
# ------------------------------------------------------------
# Example:
# [1,2,2,3,4,4,5]
#
# Output:
# [1,3,5]
# ------------------------------------------------------------

def unique_elements(arr):

    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    result = []

    for num in arr:

        if frequency[num] == 1:
            result.append(num)

    return result


# ------------------------------------------------------------
# 4. First Repeating Element
# ------------------------------------------------------------
# Example:
# [10,5,3,4,3,5,6]
#
# Output:
# 5
# ------------------------------------------------------------

def first_repeating(arr):

    visited = set()

    first = None

    for i in range(len(arr)-1, -1, -1):

        if arr[i] in visited:
            first = arr[i]

        visited.add(arr[i])

    return first


# ============================================================
# Driver Code
# ============================================================

arr1 = [1,2,2,3,1,2]

print("Frequency Count :")
print(frequency_count(arr1))

print()

arr2 = [1,2,3,1]

print("Contains Duplicate :")
print(contains_duplicate(arr2))

print()

arr3 = [1,2,2,3,4,4,5]

print("Unique Elements :")
print(unique_elements(arr3))

print()

arr4 = [10,5,3,4,3,5,6]

print("First Repeating Element :")
print(first_repeating(arr4))


# ============================================================
# Expected Output
# ============================================================

# Frequency Count :
# {1: 2, 2: 3, 3: 1}

# Contains Duplicate :
# True

# Unique Elements :
# [1, 3, 5]

# First Repeating Element :
# 5


# ============================================================
# Complexity
# ============================================================

# Frequency Count          O(n)   O(n)
# Contains Duplicate       O(n)   O(n)
# Unique Elements          O(n)   O(n)
# First Repeating          O(n)   O(n)

# ============================================================

# ============================================================
# HASHMAP PATTERN - Batch 2 (Final)
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(n)
# ============================================================


# ------------------------------------------------------------
# 5. First Non-Repeating Element
# ------------------------------------------------------------
# Example:
# [9,4,9,6,7,4]
#
# Output:
# 6
# ------------------------------------------------------------

def first_non_repeating(arr):

    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    for num in arr:

        if frequency[num] == 1:
            return num

    return -1


# ------------------------------------------------------------
# 6. Majority Element
# ------------------------------------------------------------
# Example:
# [2,2,1,2,3,2,2]
#
# Output:
# 2
#
# Boyer-Moore Voting Algorithm
# ------------------------------------------------------------

def majority_element(arr):

    candidate = None
    count = 0

    for num in arr:

        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# ------------------------------------------------------------
# 7. Two Sum (Unsorted Array)
# ------------------------------------------------------------
# Example:
# [2,7,11,15]
#
# Target = 9
#
# Output:
# [0,1]
# ------------------------------------------------------------

def two_sum(arr, target):

    hashmap = {}

    for i in range(len(arr)):

        diff = target - arr[i]

        if diff in hashmap:
            return [hashmap[diff], i]

        hashmap[arr[i]] = i

    return [-1,-1]


# ------------------------------------------------------------
# 8. Maximum Frequency Element
# ------------------------------------------------------------
# Example:
# [1,2,2,3,3,3,4]
#
# Output:
# 3
# ------------------------------------------------------------

def maximum_frequency(arr):

    frequency = {}

    maximum = 0
    answer = -1

    for num in arr:

        frequency[num] = frequency.get(num,0) + 1

        if frequency[num] > maximum:

            maximum = frequency[num]
            answer = num

    return answer


# ============================================================
# Driver Code
# ============================================================

arr1 = [9,4,9,6,7,4]

print("First Non-Repeating :")
print(first_non_repeating(arr1))

print()

arr2 = [2,2,1,2,3,2,2]

print("Majority Element :")
print(majority_element(arr2))

print()

arr3 = [2,7,11,15]

print("Two Sum :")
print(two_sum(arr3,9))

print()

arr4 = [1,2,2,3,3,3,4]

print("Maximum Frequency :")
print(maximum_frequency(arr4))


# ============================================================
# Expected Output
# ============================================================

# First Non-Repeating :
# 6

# Majority Element :
# 2

# Two Sum :
# [0,1]

# Maximum Frequency :
# 3


# ============================================================
# Complexity
# ============================================================

# First Non-Repeating      O(n)   O(n)

# Majority Element         O(n)   O(1)

# Two Sum                 O(n)   O(n)

# Maximum Frequency       O(n)   O(n)

# ============================================================
# HASHMAP PATTERN COMPLETE ✅
# ============================================================


# ============================================================
# HASHMAP PATTERN - Bonus Batch
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(n)
# ============================================================


# ------------------------------------------------------------
# 9. Valid Anagram
# ------------------------------------------------------------

def valid_anagram(s1, s2):

    if len(s1) != len(s2):
        return False

    frequency = {}

    for ch in s1:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in s2:

        if ch not in frequency:
            return False

        frequency[ch] -= 1

        if frequency[ch] == 0:
            del frequency[ch]

    return len(frequency) == 0


# ------------------------------------------------------------
# 10. Intersection of Two Arrays
# ------------------------------------------------------------

def intersection(arr1, arr2):

    visited = set(arr1)

    result = []

    for num in arr2:

        if num in visited:

            result.append(num)

            visited.remove(num)

    return result


# ------------------------------------------------------------
# 11. Union of Two Arrays
# ------------------------------------------------------------

def union(arr1, arr2):

    return list(set(arr1) | set(arr2))


# ------------------------------------------------------------
# 12. Missing Number
# ------------------------------------------------------------

def missing_number(arr):

    n = len(arr)

    total = n * (n + 1) // 2

    return total - sum(arr)


# ------------------------------------------------------------
# 13. Missing & Repeating Number
# ------------------------------------------------------------

def missing_repeating(arr):

    visited = set()

    repeat = -1

    for num in arr:

        if num in visited:
            repeat = num

        visited.add(num)

    missing = -1

    for i in range(1, len(arr)+1):

        if i not in visited:
            missing = i
            break

    return (missing, repeat)


# ------------------------------------------------------------
# 14. Count Distinct Elements
# ------------------------------------------------------------

def count_distinct(arr):

    return len(set(arr))


# ------------------------------------------------------------
# 15. Count Pairs With Given Sum
# ------------------------------------------------------------

def count_pairs(arr, target):

    frequency = {}

    count = 0

    for num in arr:

        diff = target - num

        count += frequency.get(diff, 0)

        frequency[num] = frequency.get(num, 0) + 1

    return count


# ============================================================
# Driver Code
# ============================================================

print(valid_anagram("listen","silent"))

print(intersection([1,2,3,4],[3,4,5]))

print(union([1,2,3],[3,4,5]))

print(missing_number([3,0,1]))

print(missing_repeating([4,3,6,2,1,1]))

print(count_distinct([1,2,2,3,4,4]))

print(count_pairs([1,5,7,-1,5],6))


# ============================================================
# Expected Output
# ============================================================

# True
# [3,4]
# [1,2,3,4,5]
# 2
# (5,1)
# 4
# 3

# ============================================================
# Complexity
# ============================================================

# Valid Anagram              O(n)   O(n)
# Intersection               O(n)   O(n)
# Union                      O(n)   O(n)
# Missing Number             O(n)   O(1)
# Missing & Repeating        O(n)   O(n)
# Count Distinct             O(n)   O(n)
# Count Pairs                O(n)   O(n)

# ============================================================

# ============================================================
# HASHMAP PATTERN - Final Bonus Batch
# ============================================================


# ------------------------------------------------------------
# 16. Longest Consecutive Sequence
# ------------------------------------------------------------

def longest_consecutive(arr):

    numbers = set(arr)

    longest = 0

    for num in numbers:

        if num - 1 not in numbers:

            length = 1

            while num + length in numbers:
                length += 1

            longest = max(longest, length)

    return longest


# ------------------------------------------------------------
# 17. Zero Sum Subarray Exists
# ------------------------------------------------------------

def zero_sum_subarray(arr):

    prefix = 0

    visited = set()

    for num in arr:

        prefix += num

        if prefix == 0 or prefix in visited:
            return True

        visited.add(prefix)

    return False


# ------------------------------------------------------------
# 18. Longest Zero Sum Subarray
# ------------------------------------------------------------

def longest_zero_sum(arr):

    hashmap = {}

    prefix = 0

    maximum = 0

    for i in range(len(arr)):

        prefix += arr[i]

        if prefix == 0:
            maximum = i + 1

        if prefix in hashmap:

            maximum = max(maximum, i - hashmap[prefix])

        else:

            hashmap[prefix] = i

    return maximum


# ------------------------------------------------------------
# 19. Character With Maximum Frequency
# ------------------------------------------------------------

def max_frequency_character(s):

    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch,0) + 1

    answer = ""
    maximum = 0

    for ch in frequency:

        if frequency[ch] > maximum:

            maximum = frequency[ch]
            answer = ch

    return answer


# ------------------------------------------------------------
# 20. Remove Duplicates From String
# ------------------------------------------------------------

def remove_duplicate_string(s):

    visited = set()

    result = ""

    for ch in s:

        if ch not in visited:

            visited.add(ch)

            result += ch

    return result


# ============================================================
# Driver Code
# ============================================================

print(longest_consecutive([100,4,200,1,3,2]))

print(zero_sum_subarray([4,2,-3,1,6]))

print(longest_zero_sum([15,-2,2,-8,1,7,10,23]))

print(max_frequency_character("programming"))

print(remove_duplicate_string("programming"))


# ============================================================
# Expected Output
# ============================================================

# 4
# True
# 5
# g
# progamin

# ============================================================
# HASHMAP PATTERN COMPLETE ✅
# ============================================================

# ============================================================
# HASHMAP PATTERN - Final High Frequency Batch
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Time : O(n)
# Space: O(n)
# ============================================================


# ------------------------------------------------------------
# 21. Array Subset Check
# ------------------------------------------------------------

def is_subset(arr1, arr2):

    return set(arr2).issubset(set(arr1))


# ------------------------------------------------------------
# 22. Array Equality
# ------------------------------------------------------------

from collections import Counter

def array_equal(arr1, arr2):

    return Counter(arr1) == Counter(arr2)


# ------------------------------------------------------------
# 23. Largest Subarray With Equal 0s and 1s
# ------------------------------------------------------------

def largest_equal_zero_one(arr):

    prefix = 0

    hashmap = {0: -1}

    maximum = 0

    for i in range(len(arr)):

        if arr[i] == 0:
            prefix -= 1
        else:
            prefix += 1

        if prefix in hashmap:

            maximum = max(maximum, i - hashmap[prefix])

        else:

            hashmap[prefix] = i

    return maximum


# ------------------------------------------------------------
# 24. Longest Subarray With Sum K
# ------------------------------------------------------------

def longest_subarray_sum_k(arr, k):

    prefix = 0

    hashmap = {}

    maximum = 0

    for i in range(len(arr)):

        prefix += arr[i]

        if prefix == k:
            maximum = i + 1

        if prefix - k in hashmap:

            maximum = max(maximum, i - hashmap[prefix-k])

        if prefix not in hashmap:

            hashmap[prefix] = i

    return maximum


# ------------------------------------------------------------
# 25. Pair With Given Difference
# ------------------------------------------------------------

def pair_difference(arr, diff):

    numbers = set(arr)

    for num in arr:

        if num + diff in numbers:
            return (num, num + diff)

    return None


# ------------------------------------------------------------
# 26. Isomorphic Strings
# ------------------------------------------------------------

def isomorphic(s, t):

    if len(s) != len(t):
        return False

    map1 = {}
    map2 = {}

    for a, b in zip(s, t):

        if a in map1 and map1[a] != b:
            return False

        if b in map2 and map2[b] != a:
            return False

        map1[a] = b
        map2[b] = a

    return True


# ------------------------------------------------------------
# 27. Happy Number
# ------------------------------------------------------------

def happy_number(n):

    visited = set()

    while n != 1 and n not in visited:

        visited.add(n)

        total = 0

        while n:

            digit = n % 10
            total += digit * digit
            n //= 10

        n = total

    return n == 1


# ------------------------------------------------------------
# 28. Ransom Note
# ------------------------------------------------------------

def ransom_note(note, magazine):

    frequency = {}

    for ch in magazine:

        frequency[ch] = frequency.get(ch,0) + 1

    for ch in note:

        if frequency.get(ch,0) == 0:
            return False

        frequency[ch] -= 1

    return True


# ------------------------------------------------------------
# 29. Sort Characters By Frequency
# ------------------------------------------------------------

def frequency_sort(s):

    frequency = Counter(s)

    result = ""

    for ch, count in sorted(frequency.items(),
                            key=lambda x: x[1],
                            reverse=True):

        result += ch * count

    return result


# ============================================================
# Driver Code
# ============================================================

print(is_subset([1,2,3,4,5],[2,4]))

print(array_equal([1,2,2],[2,1,2]))

print(largest_equal_zero_one([0,0,1,0,1,1,0]))

print(longest_subarray_sum_k([10,5,2,7,1,9],15))

print(pair_difference([5,20,3,2,50,80],78))

print(isomorphic("egg","add"))

print(happy_number(19))

print(ransom_note("aa","aab"))

print(frequency_sort("tree"))


# ============================================================
# Expected Output
# ============================================================

# True
# True
# 6
# 4
# (2,80)
# True
# True
# True
# eetr

# ============================================================
# HASHMAP PATTERN COMPLETE ✅
# ============================================================
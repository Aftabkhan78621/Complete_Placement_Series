# # Question

# Given an array and multiple range queries, find the sum of elements between indices L and R (inclusive) efficiently.
# Instead of calculating the sum for every query, design an efficient solution.
# Example:

# Input:
# arr = [2, 4, 6, 8, 10]
# Query:
# L = 1
# R = 3

# Output:
# 18

# # Answer (Approach)
# • Since there are multiple queries, calculating the sum every time is inefficient.
# • Build a Prefix Sum array once.
# • Use the Prefix Sum array to answer each query in O(1) time.
# • Each query requires only one subtraction.

# # Algorithm
# 1. Create a Prefix Sum array.
# 2. Set:
#    • prefix[0] = arr[0]
# 3. For every index:
#    • prefix[i] = prefix[i - 1] + arr[i]
# 4. To find sum from L to R:
#    • If L == 0 → Answer = prefix[R]
#    • Else → Answer = prefix[R] - prefix[L - 1]

# # Python Code
# def build_prefix_sum(arr):

#     prefix = [0] * len(arr)
#     prefix[0] = arr[0]

#     for i in range(1, len(arr)):
#         prefix[i] = prefix[i - 1] + arr[i]

#     return prefix


# def range_sum(prefix, left, right):

#     if left == 0:
#         return prefix[right]

#     return prefix[right] - prefix[left - 1]


# arr = [2, 4, 6, 8, 10]

# prefix = build_prefix_sum(arr)

# print(range_sum(prefix, 1, 3))

# # Short Explanation

# • Prefix Sum stores the cumulative sum from index 0 to i.
# • Prefix array is built only once.
# • Every query is answered using a simple subtraction.
# • This avoids traversing the array for every query.
# • Best approach when multiple range sum queries are asked.

# ### Important Code Lines
# prefix = [0] * len(arr)
# • Creates the Prefix Sum array.
# prefix[0] = arr[0]
# • First prefix value is always the first array element.
# prefix[i] = prefix[i - 1] + arr[i]
# • Builds the Prefix Sum array.
# if left == 0:

# • Handles the special case when the range starts from index 0.
# return prefix[right] - prefix[left - 1]

# • Formula to find the sum between indices L and R.
# # Formula

# Prefix Sum:
# prefix[i] = Sum of elements from index 0 to i

# Range Sum:
# Sum(L, R) = prefix[R] - prefix[L - 1]

# Special Case:
# If L = 0
# Answer = prefix[R]

# # Important Points
# • Best for multiple range sum queries.
# • Prefix array is built only once.
# • Every query takes O(1) time.
# • Remember the special case when L = 0.
# • Prefix Sum is a preprocessing technique.

# # Edge Cases
# Input:
# arr = [5]
# L = 0
# R = 0

# Output:
# 5

# Input:
# arr = [2, 4, 6, 8, 10]
# L = 0
# R = 2

# Output:
# 12

# Input:
# arr = [2, 4, 6, 8, 10]
# L = 4
# R = 4

# Output:
# 10

# Input:
# arr = [2, -4, 6, -1]
# L = 1
# R = 3

# Output:
# 1

# # Time Complexity

# Preprocessing: O(n)

# Each Query: O(1)

# # Space Complexity

# O(n)

# # Similar Questions

# • LeetCode 303 – Range Sum Query (Immutable)
# • LeetCode 304 – Range Sum Query 2D (Immutable)
# • Prefix XOR Queries
# • Range Average Query
# • Count Even/Odd Numbers in a Range
# • Subarray Sum Equals K

# # Follow-up Questions

# • Range Average Query.
# • Prefix XOR Queries.
# • 2D Prefix Sum (Matrix).
# • Count Even/Odd Numbers in a Range.
# • Dynamic Range Sum using Fenwick Tree or Segment Tree.

# # Pattern Recognition

# Keywords:
# • Multiple Queries
# • Range Sum
# • L to R
# • Sum Between Indices
# • Query Processing

# ➡️ Think Prefix Sum.


def build_prefix_sum(arr):

    prefix = [0] * len(arr)

    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


def range_sum(prefix, left, right):

    if left == 0:
        return prefix[right]

    return prefix[right] - prefix[left - 1]


def main():

    arr = [2, 4, 6, 8, 10]

    prefix = build_prefix_sum(arr)

    left = 1
    right = 3

    print("Sum =", range_sum(prefix, left, right))


if __name__ == "__main__":
    main()
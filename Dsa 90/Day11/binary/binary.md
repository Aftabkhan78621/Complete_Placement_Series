
#     # Problem Statement

# A library stores Book IDs in sorted order.
# The librarian wants to find a requested book as quickly as possible.
# Given a sorted array of Book IDs and a Target Book ID, return its index.
# If the book does not exist, return -1.

# Example:
# Input:
# Book IDs = [10, 20, 30, 40, 50, 60, 70]
# Target = 50

# Output:
# 4

# --------------------------------------------------

# # Observation
# Question Keywords:
# • Sorted Array
# • Search Element
# • Find Index
# • Fast Search
# • O(log n)

# Observation:
# • Array already sorted hai.
# • Hume sirf target search karna hai.
# • Fast searching required hai.

# ➡️ Technique: Binary Search
# --------------------------------------------------

# # Why Binary Search?
# Why Binary Search?
# • Array sorted hai.
# • Har iteration me search space aadhi ho jati hai.
# • Time Complexity O(log n) hoti hai.

# Why NOT Linear Search?
# • Har element check karega.
# • Time Complexity O(n) hogi.
# • Sorted array ka advantage use nahi karega.

# Why NOT HashMap?
# • Extra memory O(n) lagegi.
# • Sirf ek search ke liye unnecessary hai.

# Golden Rule:
# Sorted Array
#         ↓
# Need Fast Search
#         ↓
# Binary Search

# --------------------------------------------------

# # Answer (Approach)
# • 3 pointers use karo:
#   - left
#   - right
#   - mid
# • Har iteration me middle element check karo.
# • Agar target mil jaye to index return karo.
# • Agar target chhota hai to right half discard karo.
# • Agar target bada hai to left half discard karo.
# • Jab left > right ho jaye, return -1.

# --------------------------------------------------
# # Algorithm
# Step 1:
# Initialize:
# left = 0
# right = len(array) - 1

# Step 2:
# Jab tak left <= right:

# • Find mid.

# Step 3:
# If array[mid] == target
# → Return mid.

# Step 4:
# If target < array[mid]
# → right = mid - 1

# Step 5:
# Else
# → left = mid + 1

# Step 6:
# Target na mile to return -1.

# --------------------------------------------------
# # Python Code

# ```python
# def binary_search(book_ids, target):

#     left = 0
#     right = len(book_ids) - 1

#     while left <= right:

#         mid = (left + right) // 2

#         if book_ids[mid] == target:
#             return mid

#         elif target < book_ids[mid]:
#             right = mid - 1

#         else:
#             left = mid + 1

#     return -1


# book_ids = [10, 20, 30, 40, 50, 60, 70]
# target = 50
# print(binary_search(book_ids, target))
# ```

# --------------------------------------------------

# # Code Explanation
# left = 0
# • Search starting index.
# right = len(book_ids) - 1
# • Search ending index.
# mid = (left + right) // 2
# • Middle index calculate karta hai.
# if book_ids[mid] == target
# • Target mil gaya.
# return mid

# • Target ka index return karta hai.
# elif target < book_ids[mid]
# • Target left side me hai.
# right = mid - 1

# • Right half remove kar deta hai.
# else
# • Target right side me hai.
# left = mid + 1
# • Left half remove kar deta hai.
# return -1

# • Target array me present nahi hai.

# --------------------------------------------------

# # Important Interview Theory
# Binary Search Kab Use Kare?

# ✅ Sorted Array
# ✅ Search Element
# ✅ Find Index
# ✅ O(log n) Required

# Binary Search Kab Use Na Kare?
# ❌ Unsorted Array
# ❌ Linked List
# ❌ Random Data

# Tab:
# ➡️ Linear Search use karo.

# How Binary Search Works?
# Every iteration:
# • Middle element check hota hai.
# • Half array discard ho jata hai.
# • Search space continuously reduce hoti hai.

# Example:
# 7 Elements
# ↓
# 3 Elements
# ↓
# 1 Element

# Isliye Time Complexity O(log n) hoti hai.

# --------------------------------------------------

# # Common Mistakes

# ❌ Unsorted array par Binary Search use karna.
# ❌ while left < right likh dena (basic search me <= hona chahiye).
# ❌ mid update na karna.
# ❌ left/right galat update karna.
# ❌ Infinite loop create kar dena.

# --------------------------------------------------

# # Edge Cases

# Input:
# [10]

# Target = 10

# Output:
# 0

# Input:
# [10]

# Target = 20

# Output:
# -1

# Input:
# []

# Output:
# -1

# Input:
# [10,20,30,40]

# Target = 5

# Output:
# -1

# --------------------------------------------------

# # Time Complexity

# Best Case:
# O(1)

# (Target middle me mil jaye.)

# Average Case:
# O(log n)

# Worst Case:
# O(log n)

# --------------------------------------------------

# # Space Complexity

# O(1)

# --------------------------------------------------

# # Similar Questions

# • LeetCode 704 – Binary Search
# • LeetCode 35 – Search Insert Position
# • First Occurrence of Target
# • Last Occurrence of Target
# • Lower Bound
# • Upper Bound
# • Count Occurrences
# • Peak Element
# • Search in Rotated Sorted Array

# --------------------------------------------------

# # Follow-up Questions

# • Find First Occurrence.
# • Find Last Occurrence.
# • Count Occurrences.
# • Lower Bound.
# • Upper Bound.
# • Search Insert Position.

# --------------------------------------------------

# # Pattern Recognition

# Question me agar ye words dikhe:

# • Sorted Array
# • Search Element
# • Find Index
# • Fast Search
# • O(log n)

# ➡️ Think Binary Search.

# Question me agar likha ho:

# • Unsorted Array

# ➡️ Think Linear Search.

# --------------------------------------------------

# # 30-Second Interview Revision

# Question
#         ↓
# Array Sorted?

#         ↓
#       YES
#         ↓
# Need Fast Search?

#         ↓
#       YES
#         ↓
# Binary Search
#         ↓
# Find Mid
#         ↓
# Target == Mid ?
#       ↓        ↓
#     Yes        No
#     ↓          ↓
#  Return     Left/Right Half Remove
#                  ↓
#           Repeat Until Found

# 💡 Interview Tip:

# Interviewer agar pooche **"Binary Search hi kyu?"**

# Answer:
# "Sir, array already sorted hai aur fast searching required hai. Binary Search har iteration me search space ko half kar deta hai, isliye Time Complexity O(log n) ho jati hai. Linear Search O(n) lega aur sorted array ka advantage use nahi karega."
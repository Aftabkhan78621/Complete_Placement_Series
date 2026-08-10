# # Problem Statement

# A photo management application stores Image IDs.

# Due to a synchronization issue, some image IDs are duplicated. Since the list is already sorted, all duplicate IDs appear together.

# Your task is to remove duplicate IDs in-place and print:

# • Number of unique Image IDs.
# • All unique Image IDs.

# You are not allowed to use set() or create another array of the same size.

# Example:

# Input:
# Image IDs = [1,1,2,2,3,4,4,5,5]

# Output:

# Unique Count = 5

# Unique IDs =
# 1 2 3 4 5

# --------------------------------------------------

# # Observation

# Question Keywords:
# • Sorted Array
# • Remove Duplicates
# • In-place
# • O(1) Space

# Observation:
# • Array already sorted hai.
# • Duplicates consecutive hain.
# • Extra array allowed nahi hai.

# ➡️ Technique: Two Pointer

# --------------------------------------------------

# # Why Two Pointer?

# Why Two Pointer?
# • Sorted array me duplicates saath-saath hote hain.
# • Same array ko modify karna hai.
# • Extra space use nahi karna.
# • O(n) time aur O(1) space milti hai.

# Why NOT HashMap?
# • O(n) extra space lagegi.
# • Constraint violate ho jayega.

# Why NOT Set?
# • Extra memory use hogi.
# • Original in-place modification nahi hogi.

# Why NOT Binary Search?
# • Binary Search searching ke liye hoti hai.
# • Duplicate remove nahi karti.

# Golden Rule:

# Sorted Array
#         ↓
# Remove Duplicates
#         ↓
# In-place
#         ↓
# Think Two Pointer

# --------------------------------------------------

# # Answer (Approach)

# • Do pointers use karo:
#   - read → Array scan karega.
#   - write → Next unique element ki position batayega.
# • Har naya unique element write position par copy karo.
# • Last me write + 1 unique elements ki count hogi.

# --------------------------------------------------

# # Algorithm

# Step 1:
# Agar array empty hai, return 0.

# Step 2:
# Initialize:
# write = 0

# Step 3:
# read pointer se array traverse karo.

# Step 4:
# Agar current element last unique element se different ho:
# • write++
# • Current element ko write position par copy karo.

# Step 5:
# Return:
# • Unique Count = write + 1
# • Unique IDs = image_ids[:write + 1]

# --------------------------------------------------

# # Python Code

# ```python
# def remove_duplicate_images(image_ids):

#     if not image_ids:
#         return 0, []

#     write = 0

#     for read in range(1, len(image_ids)):

#         if image_ids[read] != image_ids[write]:
#             write += 1
#             image_ids[write] = image_ids[read]

#     return write + 1, image_ids[:write + 1]


# image_ids = [1,1,2,2,3,4,4,5,5]

# count, unique = remove_duplicate_images(image_ids)

# print("Unique Count =", count)
# print("Unique IDs =", unique)
# ```

# --------------------------------------------------

# # Code Explanation

# if not image_ids

# • Empty array ko handle karta hai.

# write = 0

# • Pehla element hamesha unique hota hai.

# for read in range(1, len(image_ids))

# • Second element se scanning start hoti hai.

# if image_ids[read] != image_ids[write]

# • Check karta hai ki naya unique element mila ya nahi.

# write += 1

# • Next unique position par move karta hai.

# image_ids[write] = image_ids[read]

# • Unique element ko correct position par copy karta hai.

# return write + 1

# • Total unique elements return karta hai.

# image_ids[:write + 1]

# • Sirf unique part return karta hai.

# --------------------------------------------------

# # Important Interview Theory

# Two Pointer Kab Use Kare?

# ✅ Sorted Array
# ✅ Remove Duplicates
# ✅ In-place Modification
# ✅ O(1) Extra Space
# ✅ Compare Adjacent Elements

# Two Pointer Kab Use Na Kare?

# ❌ Unsorted Array
# ❌ Frequency Count Required
# ❌ Random Duplicate Positions

# Tab:
# ➡️ HashMap use karo.

# Important Observation:

# Interviewer story change karega.

# Orders
# ↓

# Image IDs
# ↓

# Employee IDs
# ↓

# Product IDs

# Pattern same rahega.

# Pattern pe focus karo, story pe nahi.

# --------------------------------------------------

# # Common Mistakes

# ❌ Extra array bana dena.
# ❌ set() use kar lena.
# ❌ write ko 1 se initialize kar dena.
# ❌ Slice galat return karna.
# ❌ Empty array handle na karna.

# --------------------------------------------------

# # Edge Cases

# Input:
# []

# Output:
# Unique Count = 0

# Input:
# [7]

# Output:
# Unique Count = 1

# Input:
# [1,1,1,1]

# Output:
# Unique Count = 1

# Input:
# [1,2,3,4]

# Output:
# Unique Count = 4

# --------------------------------------------------

# # Time Complexity

# Best Case:
# O(n)

# Average Case:
# O(n)

# Worst Case:
# O(n)

# --------------------------------------------------

# # Space Complexity

# O(1)

# (No extra array used.)

# --------------------------------------------------

# # Similar Questions

# • LeetCode 26 – Remove Duplicates from Sorted Array
# • LeetCode 80 – Remove Duplicates from Sorted Array II
# • LeetCode 27 – Remove Element
# • LeetCode 283 – Move Zeroes
# • LeetCode 88 – Merge Sorted Array
# • Two Sum II

# --------------------------------------------------

# # Follow-up Questions

# • Keep each duplicate at most twice.
# • Remove a given value.
# • Remove duplicates from an unsorted array.
# • Count duplicate elements.
# • Print only duplicate elements.

# --------------------------------------------------

# # Pattern Recognition

# Question me agar ye words dikhe:

# • Sorted Array
# • Remove Duplicates
# • In-place
# • Constant Space
# • Return New Length

# ➡️ Think Two Pointer.

# Question me agar dikhe:

# • Frequency
# • Count
# • Occurrence

# ➡️ Think HashMap.

# --------------------------------------------------

# # 30-Second Interview Revision

# Question
#         ↓
# Array Sorted?

#         ↓
#       YES
#         ↓
# Need Remove Duplicates?

#         ↓
#       YES
#         ↓
# Extra Space Allowed?

#         ↓
#       NO
#         ↓
# Two Pointer
#         ↓
# read → Scan
# write → Store Unique
#         ↓
# Return write + 1

# 💡 Interview Tip:

# Interviewer agar pooche **"Two Pointer hi kyu?"**

# Answer:
# "Sir, array sorted hai aur duplicates consecutive hain. Hume in-place modification karni hai aur O(1) extra space maintain karni hai. Two Pointer technique isi requirement ko O(n) time aur O(1) space me efficiently solve karti hai."
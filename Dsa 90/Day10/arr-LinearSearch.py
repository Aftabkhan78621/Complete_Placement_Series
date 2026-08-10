def Linear_search(prod,target):
    for index in range(len(prod)):
        if prod[index] == target:
            return (index,prod[index])
    return -1

def main():
    prod = [1,12,5,7,9]
    target = 7
    result = Linear_search(prod,target)
    print("Index is: ",result)

if __name__ == '__main__':
    main()


# Problem Statement

# A warehouse stores Product IDs in an array.
# The warehouse manager wants to quickly check whether a requested Product ID exists in the warehouse.
# Write a program to search for the given Target Product ID.
# If the product exists, return its index.
# Otherwise, return -1.

# Example:
# Input:
# Products = [12, 45, 78, 23, 90]
# Target = 23

# Output:
# 3

# --------------------------------------------------

# # Observation
# Question Keywords:
# • Search Element
# • Find Index
# • Unsorted Array

# Observation:
# • Array sorted nahi hai.
# • Hume sirf target find karna hai.
# • Isliye har element check karna padega.

# ➡️ Technique: Linear Search
# --------------------------------------------------

# # Why Linear Search?

# Why Linear Search?
# • Array unsorted hai.
# • Kisi bhi position par target ho sakta hai.
# • Har element check karna zaroori hai.

# Why NOT Binary Search?
# • Binary Search sirf Sorted Array par kaam karti hai.
# • Is array me elements sorted nahi hain.

# Why NOT HashMap?
# • Extra O(n) space lagega.
# • Sirf ek search ke liye unnecessary hai.

# --------------------------------------------------

# # Answer (Approach)
# • Array ke first element se traversal start karo.
# • Har element ko target se compare karo.
# • Match milte hi index return karo.
# • Agar pura array traverse ho jaye aur target na mile to -1 return karo.

# --------------------------------------------------

# # Algorithm

# Step 1:
# Array ke first index se traversal start karo.

# Step 2:
# Har element ko target se compare karo.

# Step 3:
# Agar match mil jaye, uska index return karo.

# Step 4:
# Agar pura array check ho jaye aur target na mile, return -1.

# --------------------------------------------------

# # Python Code
# ```python
# def linear_search(products, target):

#     for index in range(len(products)):
#         if products[index] == target:
#             return index

#     return -1


# products = [12, 45, 78, 23, 90]
# target = 23

# print(linear_search(products, target))
# ```

# --------------------------------------------------

# # Code Explanation
# for index in range(len(products))
# • Array ke har index par visit karta hai.
# products[index] == target
# • Current element aur target compare karta hai.
# return index
# • Target milte hi uska index return kar deta hai aur loop stop ho jata hai.
# return -1
# • Agar target nahi mila to -1 return hota hai.

# --------------------------------------------------

# # Important Interview Theory

# Linear Search Kab Use Kare?
# ✅ Array Unsorted ho.
# ✅ Chhota dataset ho.
# ✅ Sirf ek ya kuch hi searches karni ho.

# Linear Search Kab Use Na Kare?
# ❌ Array Sorted ho.
# ❌ Bahut zyada searches karni ho.
# ❌ Fast searching required ho.

# Tab:
# ➡️ Binary Search ya HashMap use karo.

# --------------------------------------------------

# # Common Mistakes

# ❌ Binary Search use kar dena on unsorted array.
# ❌ index() function use karna.
# ❌ -1 return karna bhool jana.
# ❌ Duplicate hone par first occurrence ka concept na samajhna.

# --------------------------------------------------

# # Edge Cases
# Input:
# [10], Target = 10
# Output:
# 0

# Input:
# [10], Target = 20
# Output:
# -1

# Input:
# []
# Output:
# -1

# Input:
# [5, 8, 9, 5], Target = 5
# Output:
# 0 (First Occurrence)

# --------------------------------------------------

# # Time Complexity
# Best Case:
# O(1)
# (Agar target first index par mil jaye.)
# Average Case:
# O(n)
# Worst Case:
# O(n)

# (Agar target last me ho ya present hi na ho.)

# --------------------------------------------------

# # Space Complexity
# O(1)
# (No extra memory used.)
# --------------------------------------------------

# # Similar Questions

# • LeetCode 704 – Binary Search
# • Search Insert Position
# • Find First Occurrence
# • Find Last Occurrence
# • Search in Rotated Sorted Array
# • Find Minimum Element

# --------------------------------------------------

# # Follow-up Questions
# • Find Last Occurrence of Target.
# • Count Occurrences of Target.
# • Search in Sorted Array (Binary Search).
# • Find First Element Greater Than Target.
# • Find Smallest/Largest Element.

# --------------------------------------------------

# # Pattern Recognition

# Question me agar ye words dikhe:
# • Search Element
# • Find Index
# • Unsorted Array
# • Search Target

# ➡️ Think Linear Search.

# Agar question me ye words dikhe:
# • Sorted Array
# • Search
# • O(log n)

# ➡️ Think Binary Search.

# --------------------------------------------------

# # 30-Second Interview Revision
# Question
#         ↓
# Array Sorted?

#         ↓
#       NO
#         ↓
# Linear Search
#         ↓
# Compare Every Element
#         ↓
# Match → Return Index
#         ↓
# No Match → Return -1

# 💡 Interview Tip:
# Interviewer agar pooche **"Linear Search hi kyu?"**

# Answer:
# "Sir, array sorted nahi hai. Isliye Binary Search apply nahi ho sakti. Har element ko check karna zaroori hai, isliye Linear Search optimal approach hai."
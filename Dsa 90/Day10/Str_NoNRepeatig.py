def first_non_repeating_ch(text):
    freq = {}
    # count frequency

    for ch in text:
        freq[ch] = freq.get(ch,0) + 1

    #  find first non repeating ch
    for ch in text:
        if freq[ch] == 1:
            return ch
    return -1





def main():
    text = input("Enter a text:  ")

    result = first_non_repeating_ch(text)

    print('answer is : ',result)

if __name__ == '__main__':
    main()


# Problem Statement

# An HR portal generates Employee IDs.
# During verification, the system needs to find the first character that appears only once.
# Your task is to return the first non-repeating character.
# If every character repeats, return -1.

# Example:
# Input:
# aabbcdde
# Output:
# c

# --------------------------------------------------

# # Observation

# Question Keywords:
# • First Non-Repeating Character
# • Frequency
# • Count
# • Occurrence

# Observation:
# • Hume character ka count bhi chahiye.
# • Aur original order bhi maintain karna hai.

# ➡️ Technique: HashMap (Dictionary)

# --------------------------------------------------

# # Why HashMap?

# Why HashMap?
# • Har character ki frequency O(1) average time me store aur access hoti hai.
# • Original string ka order preserve rehta hai.
# • Overall solution O(n) me ho jata hai.

# Why NOT Nested Loops?
# • Har character ke liye poori string scan karni padegi.
# • Time Complexity = O(n²).

# Why NOT Set?
# • Set frequency store nahi karta.
# • First non-repeating character identify nahi kar sakta.

# Why 2 Traversals?
# 1st Traversal:
# • Frequency count store karo.

# 2nd Traversal:
# • Original order me pehla character find karo jiski frequency 1 ho.

# --------------------------------------------------

# # Answer (Approach)

# • Dictionary me har character ki frequency count karo.
# • String ko dobara traverse karo.
# • Jis character ki frequency 1 mile, usse return karo.
# • Agar aisa koi character na mile to -1 return karo.

# --------------------------------------------------

# # Algorithm

# Step 1:
# Create an empty dictionary.
# Step 2:
# Count frequency of every character.
# Step 3:
# Traverse the original string again.
# Step 4:
# If frequency == 1, return that character.
# Step 5:
# If no such character exists, return -1.

# --------------------------------------------------

# # Python Code
# ```python
# def first_non_repeating_character(text):

#     frequency = {}

#     for character in text:
#         frequency[character] = frequency.get(character, 0) + 1

#     for character in text:
#         if frequency[character] == 1:
#             return character

#     return -1


# text = input("Enter String: ")
# print(first_non_repeating_character(text))
# ```

# --------------------------------------------------

# # Code Explanation

# frequency = {}
# • Character ki frequency store karta hai.
# frequency.get(character, 0) + 1
# • Character ka count increase karta hai.
# for character in text:
# • Pehla loop frequency build karta hai.
# for character in text:
# • Dusra loop original order me answer find karta hai.
# if frequency[character] == 1
# • Pehla non-repeating character check karta hai.
# return character
# • Character milte hi function stop ho jata hai.
# return -1

# • Agar sab repeat ho gaye to -1 return hota hai.

# --------------------------------------------------

# # Important Interview Theory

# HashMap Kab Use Kare?

# ✅ Frequency Count
# ✅ Count Occurrence
# ✅ Duplicate Detection
# ✅ First/Last Non-Repeating
# ✅ Character Counting

# HashMap Kab Use Na Kare?

# ❌ Jab array sorted ho aur Two Pointer se kaam ho.
# ❌ Jab sirf searching sorted array me karni ho (Binary Search better hai).

# Golden Rule:
# Frequency / Count / Occurrence dikhe
#         ↓
# Think HashMap

# --------------------------------------------------

# # Common Mistakes
# ❌ Sirf unique character return kar dena.
# ❌ Original order ignore kar dena.
# ❌ Set use kar lena.
# ❌ Ek hi traversal me answer dhoondhne ki koshish karna.
# ❌ Frequency count maintain na karna.

# --------------------------------------------------

# # Edge Cases

# Input:
# abcd
# Output:
# a
# Input:
# aabbcc
# Output:
# -1
# Input:
# z
# Output:
# z
# Input:
# aaabbbcccde
# Output:
# d
# Input:
# ""
# Output:
# -1

# --------------------------------------------------

# # Time Complexity
# 1st Traversal:
# O(n)
# 2nd Traversal:
# O(n)
# Overall:
# O(n)

# --------------------------------------------------

# # Space Complexity
# O(n)
# (Dictionary stores character frequencies.)

# --------------------------------------------------

# # Similar Questions

# • LeetCode 387 – First Unique Character in a String
# • Character Frequency Count
# • First Repeating Character
# • Last Non-Repeating Character
# • Majority Element
# • Top K Frequent Elements
# • Find the Mode

# --------------------------------------------------

# # Follow-up Questions

# • Find First Repeating Character.
# • Find Last Non-Repeating Character.
# • Count Frequency of Every Character.
# • Character with Maximum Frequency.
# • First Non-Repeating Word.

# --------------------------------------------------

# # Pattern Recognition

# Question me agar ye words dikhe:

# • Frequency
# • Count
# • Occurrence
# • Non-Repeating
# • First Unique Character
# • Duplicate Count

# ➡️ Think HashMap (Dictionary).

# --------------------------------------------------

# # 30-Second Interview Revision

# Question
#         ↓
# Need Frequency?
#         ↓
# YES
#         ↓
# Build HashMap
#         ↓
# Store Count
#         ↓
# Traverse Again
#         ↓
# Frequency == 1
#         ↓
# Return Character
#         ↓
# Else Return -1

# 💡 Interview Tip:

# Interviewer agar pooche **"HashMap hi kyu?"**

# Answer:
# "Sir, hume har character ki frequency bhi chahiye aur original order bhi maintain karna hai. HashMap frequency ko O(1) average time me store karta hai, isliye overall solution O(n) ho jata hai. Nested loops O(n²) lenge aur Set frequency maintain nahi karta."
# """
# ===========================
# QUESTION 41 : Reverse a String
# ===========================

# Theory:
# Reverse string interview ka sabse common string question hai.
# Two Pointer ya reverse traversal dono accepted hain. Yahan slicing use nahi ki gayi.

# def reverse_string(text):

#     reverse = ""

#     for i in range(len(text) - 1, -1, -1):
#         reverse += text[i]

#     return reverse


# print(reverse_string("python"))

# Time Complexity : O(n)
# Space Complexity: O(n)


# ===========================
# QUESTION 42 : Check Palindrome String
# ===========================

# Theory:
# Palindrome string Two Pointer ka basic application hai.
# Interview me slicing avoid karke logic likhna preferred hota hai.

# def is_palindrome(text):

#     left = 0
#     right = len(text) - 1

#     while left < right:

#         if text[left] != text[right]:
#             return False

#         left += 1
#         right -= 1

#     return True


# print(is_palindrome("madam"))

# Time Complexity : O(n)
# Space Complexity: O(1)


# ===========================
# QUESTION 43 : Count Characters
# ===========================

# Theory:
# String traversal ka basic interview question hai.
# Spaces ko bhi character maana gaya hai.

# def count_characters(text):

#     count = 0

#     for _ in text:
#         count += 1

#     return count


# print(count_characters("Hello"))

# Time Complexity : O(n)
# Space Complexity: O(1)


# ===========================
# QUESTION 44 : Count Words
# ===========================

# Theory:
# Interview me string parsing check karne ke liye common question hai.
# split() optimized approach hai.

# def count_words(text):

#     words = text.split()

#     return len(words)


# print(count_words("Hello Python World"))

# Time Complexity : O(n)
# Space Complexity: O(n)


# ===========================
# QUESTION 45 : Capitalize First Letter
# ===========================

# Theory:
# String formatting aur indexing ka basic application hai.

# def capitalize_first(text):

#     if not text:
#         return text

#     return text[0].upper() + text[1:]


# print(capitalize_first("python"))

# Time Complexity : O(n)
# Space Complexity: O(n)


# ===========================
# QUESTION 46 : Capitalize Each Word
# ===========================

# Theory:
# Interview me string manipulation aur traversal check karne ke liye pucha jata hai.

# def capitalize_each_word(text):

#     words = text.split()

#     result = []

#     for word in words:
#         result.append(word.capitalize())

#     return " ".join(result)


# print(capitalize_each_word("hello python world"))

# Time Complexity : O(n)
# Space Complexity: O(n)


# ===========================
# QUESTION 47 : Find Longest Word
# ===========================

# Theory:
# Traversal aur comparison logic ka common interview question hai.

# def longest_word(text):

#     words = text.split()

#     longest = ""

#     for word in words:

#         if len(word) > len(longest):
#             longest = word

#     return longest


# print(longest_word("I love programming in Python"))

# Time Complexity : O(n)
# Space Complexity: O(n)


# ===========================
# QUESTION 48 : Find Shortest Word
# ===========================

# Theory:
# Longest word ka reverse logic hai.
# Interview me comparison aur traversal check hota hai.

# def shortest_word(text):

#     words = text.split()

#     shortest = words[0]

#     for word in words:

#         if len(word) < len(shortest):
#             shortest = word

#     return shortest


# print(shortest_word("I love programming in Python"))

# Time Complexity : O(n)
# Space Complexity: O(n)


# ===========================
# QUESTION 49 : Remove Spaces
# ===========================

# Theory:
# String processing ka frequently asked interview question hai.
# replace() optimized solution hai.

# def remove_spaces(text):

#     return text.replace(" ", "")


# print(remove_spaces("Hello Python World"))

# Time Complexity : O(n)
# Space Complexity: O(n)


# ===========================
# QUESTION 50 : Remove Duplicate Characters
# ===========================

# Theory:
# HashSet/Dictionary concept check karne ke liye common interview question hai.
# Order maintain karna important hota hai.

# def remove_duplicate_characters(text):

#     seen = set()
#     answer = ""

#     for ch in text:

#         if ch not in seen:
#             seen.add(ch)
#             answer += ch

#     return answer


# print(remove_duplicate_characters("programming"))

# Time Complexity : O(n)
# Space Complexity: O(n)
# # ``
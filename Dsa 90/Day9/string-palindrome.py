# # Problem Statement

# An online document verification system accepts only those verification codes that are Palindrome.
# A Palindrome is a string that reads the same from left to right and right to left.
# Your task is to check whether the given string is a palindrome.

# Restriction:
# ❌ Don't use slicing ([::-1])

# Example 1:
# Input:
# madam

# Output:
# Palindrome

# Example 2:
# Input:
# python

# Output:
# Not Palindrome

# # Answer (Approach)
# • Use Two Pointer Technique.
# • One pointer starts from the beginning (left).
# • Another pointer starts from the end (right).
# • Compare both characters until the pointers meet.
# • If any pair is different, return "Not Palindrome".

# # Algorithm
# 1. Initialize:
#    • left = 0
#    • right = len(text) - 1
# 2. Compare characters from both ends.
# 3. If characters are different, return False.
# 4. Move:
#    • left += 1
#    • right -= 1
# 5. If the loop completes, return True.

# # Python Code
# ```python
# def is_palindrome(text):

#     left = 0
#     right = len(text) - 1

#     while left < right:

#         if text[left] != text[right]:
#             return False

#         left += 1
#         right -= 1

#     return True


# def main():

#     text = input("Enter String: ")

#     if is_palindrome(text):
#         print("Palindrome")
#     else:
#         print("Not Palindrome")


# if __name__ == "__main__":
#     main()
# ```

# # Short Explanation

# • Two Pointer technique compares characters from both ends.
# • If all character pairs match, the string is a palindrome.
# • If any pair doesn't match, immediately return False.
# • No extra string is created, so O(1) space is used.
# • This is the optimal interview solution.

# ### Important Code Lines

# left = 0

# • Left pointer starts from the first character.

# right = len(text) - 1

# • Right pointer starts from the last character.

# while left < right:

# • Continue comparing until both pointers meet.

# if text[left] != text[right]:

# • If characters differ, the string is not a palindrome.

# left += 1

# • Move left pointer one step forward.

# right -= 1

# • Move right pointer one step backward.

# return True

# • All character pairs matched.

# # Important Points

# • Don't use slicing ([::-1]).
# • Two Pointer is the optimal approach.
# • Stop immediately after finding the first mismatch.
# • Empty string and single-character strings are also palindromes.

# # Edge Cases

# Input: ""
# Output: Palindrome

# Input: "a"
# Output: Palindrome

# Input: "aa"
# Output: Palindrome

# Input: "ab"
# Output: Not Palindrome

# Input: "racecar"
# Output: Palindrome

# # Time Complexity

# O(n)

# # Space Complexity

# O(1)

# # Similar Questions

# • LeetCode 125 – Valid Palindrome
# • LeetCode 680 – Valid Palindrome II
# • Longest Palindromic Substring
# • Palindrome Number
# • Reverse String

# # Follow-up Questions

# • Ignore uppercase/lowercase characters.
# • Ignore spaces while checking.
# • Ignore special characters.
# • Find the longest palindromic substring.
# • Check if a string becomes a palindrome after removing one character.

# # Pattern Recognition

# Keywords:
# • Palindrome
# • Compare from both ends
# • Mirror
# • Reverse without extra space

# ➡️ Think Two Pointer Technique.


def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

def main():
    text = input("Enter a text: ")

    if is_palindrome(text):
        print('palindrome')
    else:
        print('Not palindrome')
    
if __name__ == '__main__':
    main()
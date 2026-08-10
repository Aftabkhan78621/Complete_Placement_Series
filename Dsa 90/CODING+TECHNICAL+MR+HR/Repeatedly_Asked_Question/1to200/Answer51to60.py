# ============================================================
# STRING PATTERN - Batch 1 (LeetCode + Service-Based Interview)
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# NOTE:
# Optimized Interview Solutions
# Built-in shortcuts like find(), replace(), count()
# are NOT used unless interview allows.
# ============================================================


# ------------------------------------------------------------
# 51. Check Anagram
# ------------------------------------------------------------
# Problem:
# Check if two strings contain same characters.
#
# Example:
# listen
# silent
#
# Output:
# True
#
# Pattern:
# Hashing
#
# Time : O(n)
# Space: O(n)
# ------------------------------------------------------------

def is_anagram(s1, s2):

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
# 52. Replace Substring (Manual)
# ------------------------------------------------------------
# Problem:
# Replace old substring with new substring.
#
# Example:
# Python is good
#
# Replace:
# good -> awesome
#
# Time : O(n*m)
# Space: O(n)
# ------------------------------------------------------------

def replace_substring(text, old, new):

    result = ""

    i = 0

    while i < len(text):

        if text[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += text[i]
            i += 1

    return result


# ------------------------------------------------------------
# 53. Find Substring
# (Without find(), index(), in)
# ------------------------------------------------------------
# Problem:
# Return starting index of substring.
#
# Example:
#
# Python Programming
#
# Program
#
# Output:
# 7
#
# Time : O(n*m)
# Space: O(1)
# ------------------------------------------------------------

def find_substring(text, pattern):

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):

        match = True

        for j in range(m):

            if text[i+j] != pattern[j]:
                match = False
                break

        if match:
            return i

    return -1


# ------------------------------------------------------------
# 54. Count Occurrence of Each Character
# ------------------------------------------------------------
# Problem:
#
# apple
#
# Output:
#
# a=1
# p=2
# l=1
# e=1
#
# Time : O(n)
# Space: O(n)
# ------------------------------------------------------------

def character_frequency(text):

    frequency = {}

    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1

    return frequency


# ------------------------------------------------------------
# 55. Convert String to Array
# (Without split())
# ------------------------------------------------------------
# Problem:
#
# "I Love Python"
#
# Output:
#
# ['I','Love','Python']
#
# Time : O(n)
# Space: O(n)
# ------------------------------------------------------------

def string_to_array(sentence):

    words = []

    current = ""

    for ch in sentence:

        if ch == " ":

            if current != "":
                words.append(current)

            current = ""

        else:
            current += ch

    if current != "":
        words.append(current)

    return words


# ============================================================
# Driver Code
# ============================================================

print("51. Anagram")
print(is_anagram("listen", "silent"))

print()

print("52. Replace Substring")
print(replace_substring("Python is good", "good", "awesome"))

print()

print("53. Find Substring")
print(find_substring("Python Programming", "Program"))

print()

print("54. Character Frequency")
print(character_frequency("apple"))

print()

print("55. String To Array")
print(string_to_array("I Love Python"))


# ============================================================
# Expected Output
# ============================================================

# 51.
# True

# 52.
# Python is awesome

# 53.
# 7

# 54.
# {'a':1,'p':2,'l':1,'e':1}

# 55.
# ['I','Love','Python']


# ============================================================
# Complexity
# ============================================================

# Check Anagram                O(n)     O(n)

# Replace Substring            O(n*m)   O(n)

# Find Substring               O(n*m)   O(1)

# Character Frequency          O(n)     O(n)

# String To Array              O(n)     O(n)

# ============================================================
# Frequently Asked
# ============================================================

# ✅ TCS
# ✅ Infosys
# ✅ Accenture
# ✅ Capgemini
# ✅ Cognizant
# ✅ IBM
# ✅ Deloitte
# ✅ Wipro
# ✅ HCL
# ✅ Cyntexa
#
# Also Common in LeetCode Easy
# ============================================================

# ============================================================
# STRING PATTERN - Batch 2
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ------------------------------------------------------------
# 56. Convert Array to String
# (Without join())
# ------------------------------------------------------------
# Example:
# ["I","Love","Python"]
#
# Output:
# I Love Python
#
# Time : O(n)
# Space: O(n)
# ------------------------------------------------------------

def array_to_string(arr):

    result = ""

    for i in range(len(arr)):

        result += arr[i]

        if i != len(arr)-1:
            result += " "

    return result


# ------------------------------------------------------------
# 57. Remove Vowels
# ------------------------------------------------------------
# Example:
# education
#
# Output:
# dctn
#
# Time : O(n)
# Space: O(n)
# ------------------------------------------------------------

def remove_vowels(text):

    vowels = "aeiouAEIOU"

    result = ""

    for ch in text:

        if ch not in vowels:
            result += ch

    return result


# ------------------------------------------------------------
# 58. Find Index of Character
# (Without index())
# ------------------------------------------------------------
# Example:
# Python
#
# Find:
# h
#
# Output:
# 3
#
# Time : O(n)
# Space: O(1)
# ------------------------------------------------------------

def character_index(text, target):

    for i in range(len(text)):

        if text[i] == target:
            return i

    return -1


# ------------------------------------------------------------
# 59. Check String Contains Only Digits
# (Without isdigit())
# ------------------------------------------------------------
# Example:
# 12345
#
# Output:
# True
#
# Time : O(n)
# Space: O(1)
# ------------------------------------------------------------

def only_digits(text):

    for ch in text:

        if ch < '0' or ch > '9':
            return False

    return True


# ============================================================
# Driver Code
# ============================================================

print(array_to_string(["I","Love","Python"]))

print(remove_vowels("education"))

print(character_index("Python",'h'))

print(only_digits("123456"))

print(only_digits("12A56"))


# ============================================================
# Complexity
#
# Array to String      O(n)
# Remove Vowels        O(n)
# Character Index      O(n)
# Only Digits          O(n)
# ============================================================


# ============================================================
# STRING PATTERN - Batch 3
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
# ============================================================


# ------------------------------------------------------------
# 60. Check Only Alphabets
# (Without isalpha())
# ------------------------------------------------------------
# Example:
# Python
#
# Output:
# True
#
# Time : O(n)
# Space: O(1)
# ------------------------------------------------------------

def only_alphabets(text):

    for ch in text:

        if not ('A' <= ch <= 'Z' or 'a' <= ch <= 'z'):
            return False

    return True


# ------------------------------------------------------------
# 61. Reverse Words in Sentence
# ------------------------------------------------------------
# Example:
# I Love Python
#
# Output:
# Python Love I
#
# Time : O(n)
# Space: O(n)
# ------------------------------------------------------------

def reverse_words(sentence):

    words = sentence.split()

    left = 0
    right = len(words)-1

    while left < right:

        words[left], words[right] = words[right], words[left]

        left += 1
        right -= 1

    result = ""

    for i in range(len(words)):

        result += words[i]

        if i != len(words)-1:
            result += " "

    return result


# ------------------------------------------------------------
# 62. Starts With
# (Without startswith())
# ------------------------------------------------------------
# Example:
# Python Programming
#
# Python
#
# Output:
# True
#
# Time : O(m)
# Space: O(1)
# ------------------------------------------------------------

def starts_with(text, word):

    if len(word) > len(text):
        return False

    for i in range(len(word)):

        if text[i] != word[i]:
            return False

    return True


# ------------------------------------------------------------
# 63. Ends With
# (Without endswith())
# ------------------------------------------------------------
# Example:
# Python Programming
#
# ming
#
# Output:
# True
#
# Time : O(m)
# Space: O(1)
# ------------------------------------------------------------

def ends_with(text, word):

    if len(word) > len(text):
        return False

    start = len(text) - len(word)

    for i in range(len(word)):

        if text[start+i] != word[i]:
            return False

    return True


# ============================================================
# Driver Code
# ============================================================

print(only_alphabets("Python"))

print(only_alphabets("Python123"))

print(reverse_words("I Love Python"))

print(starts_with("Python Programming","Python"))

print(ends_with("Python Programming","ming"))


# ============================================================
# Complexity
#
# Only Alphabets      O(n)
# Reverse Words       O(n)
# Starts With         O(m)
# Ends With           O(m)
# ============================================================


# ============================================================
# STRING PATTERN - Batch 4
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Optimized Interview Solutions
# ============================================================


# ------------------------------------------------------------
# 64. Find Duplicate Words
# ------------------------------------------------------------
# Example:
# "python java python c java"
#
# Output:
# ['python', 'java']
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def duplicate_words(sentence):

    words = sentence.split()

    frequency = {}
    duplicates = []

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    for word in frequency:

        if frequency[word] > 1:
            duplicates.append(word)

    return duplicates


# ------------------------------------------------------------
# 65. First Non-Repeating Character
# ------------------------------------------------------------
# Example:
# "aabbcdde"
#
# Output:
# c
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def first_non_repeating(text):

    frequency = {}

    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in text:

        if frequency[ch] == 1:
            return ch

    return None


# ------------------------------------------------------------
# 66. Most Frequent Character
# ------------------------------------------------------------
# Example:
# "programming"
#
# Output:
# g
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def most_frequent(text):

    frequency = {}

    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1

    maximum = 0
    answer = ""

    for ch in frequency:

        if frequency[ch] > maximum:
            maximum = frequency[ch]
            answer = ch

    return answer


# ------------------------------------------------------------
# 67. Compare Two Strings Ignoring Case
# (Without lower())
# ------------------------------------------------------------
# Example:
# Python
# python
#
# Output:
# True
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def compare_ignore_case(s1, s2):

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):

        ch1 = s1[i]
        ch2 = s2[i]

        if 'A' <= ch1 <= 'Z':
            ch1 = chr(ord(ch1) + 32)

        if 'A' <= ch2 <= 'Z':
            ch2 = chr(ord(ch2) + 32)

        if ch1 != ch2:
            return False

    return True


# ------------------------------------------------------------
# 68. Remove Special Characters
# ------------------------------------------------------------
# Example:
# Py@th#on123!
#
# Output:
# Python123
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def remove_special(text):

    result = ""

    for ch in text:

        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
            result += ch

    return result


# ------------------------------------------------------------
# 69. Truncate String
# ------------------------------------------------------------
# Example:
# PythonProgramming
#
# Length = 6
#
# Output:
# Python
#
# Time  : O(k)
# Space : O(k)
# ------------------------------------------------------------

def truncate_string(text, length):

    result = ""

    for i in range(min(length, len(text))):
        result += text[i]

    return result


# ------------------------------------------------------------
# 70. Count Uppercase Letters
# ------------------------------------------------------------
# Example:
# PyTHonAI
#
# Output:
# 5
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def count_uppercase(text):

    count = 0

    for ch in text:

        if 'A' <= ch <= 'Z':
            count += 1

    return count


# ============================================================
# Driver Code
# ============================================================

print("64.", duplicate_words("python java python c java"))

print("65.", first_non_repeating("aabbcdde"))

print("66.", most_frequent("programming"))

print("67.", compare_ignore_case("Python", "python"))

print("68.", remove_special("Py@th#on123!"))

print("69.", truncate_string("PythonProgramming", 6))

print("70.", count_uppercase("PyTHonAI"))


# ============================================================
# Expected Output
# ============================================================

# 64. ['python', 'java']

# 65. c

# 66. g

# 67. True

# 68. Python123

# 69. Python

# 70. 5


# ============================================================
# Complexity
# ============================================================

# Duplicate Words               O(n)   O(n)

# First Non-Repeating Char      O(n)   O(n)

# Most Frequent Character       O(n)   O(n)

# Compare Ignore Case           O(n)   O(1)

# Remove Special Characters     O(n)   O(n)

# Truncate String               O(k)   O(k)

# Count Uppercase               O(n)   O(1)


# ============================================================
# Frequently Asked
# ============================================================

# ✅ TCS
# ✅ Infosys
# ✅ Accenture
# ✅ Capgemini
# ✅ Cognizant
# ✅ IBM
# ✅ Deloitte
# ✅ Wipro
# ✅ HCL
# ✅ Cyntexa
#
# LeetCode Easy Pattern
# ============================================================



# ============================================================
# STRING PATTERN - Batch 5A
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Optimized Interview Solutions (Python)
# ============================================================


# ------------------------------------------------------------
# 71. Count Lowercase Letters
# ------------------------------------------------------------
# Problem:
# Count total lowercase letters.
#
# Example:
# "PyTHonAI"
#
# Output:
# 3
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def count_lowercase(text):

    count = 0

    for ch in text:

        if 'a' <= ch <= 'z':
            count += 1

    return count


# ------------------------------------------------------------
# 72. Toggle Case of String
# ------------------------------------------------------------
# Problem:
# Convert Uppercase -> Lowercase
# Convert Lowercase -> Uppercase
#
# Example:
# "PyThOn"
#
# Output:
# "pYtHoN"
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def toggle_case(text):

    result = ""

    for ch in text:

        if 'A' <= ch <= 'Z':

            result += chr(ord(ch) + 32)

        elif 'a' <= ch <= 'z':

            result += chr(ord(ch) - 32)

        else:

            result += ch

    return result


# ------------------------------------------------------------
# 73. Sort Characters Alphabetically
# ------------------------------------------------------------
# Problem:
# Sort all characters.
#
# Example:
# "python"
#
# Output:
# "hnopty"
#
# Time  : O(n²)
# Space : O(n)
#
# (Selection Sort - Interview Friendly)
# ------------------------------------------------------------

def sort_characters(text):

    arr = list(text)

    n = len(arr)

    for i in range(n):

        minimum = i

        for j in range(i + 1, n):

            if arr[j] < arr[minimum]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]

    result = ""

    for ch in arr:
        result += ch

    return result


# ------------------------------------------------------------
# 74. Check Valid Email Format
# ------------------------------------------------------------
# Problem:
# Basic email validation.
#
# Rules:
# ✔ One '@'
# ✔ At least one '.'
# ✔ '@' before '.'
#
# Example:
# abc@gmail.com
#
# Output:
# True
#
# Time  : O(n)
# Space : O(1)
# ------------------------------------------------------------

def valid_email(email):

    at = -1
    dot = -1

    for i in range(len(email)):

        if email[i] == '@':
            at = i

        if email[i] == '.':
            dot = i

    if at == -1:
        return False

    if dot == -1:
        return False

    if at > dot:
        return False

    if at == 0:
        return False

    if dot == len(email)-1:
        return False

    return True


# ------------------------------------------------------------
# 75. Mask Email ID
# ------------------------------------------------------------
# Problem:
# Hide email username.
#
# Example:
# johnsmith@gmail.com
#
# Output:
# j*******h@gmail.com
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def mask_email(email):

    at = email.find("@")

    username = email[:at]

    domain = email[at:]

    if len(username) <= 2:
        return username[0] + "*" + domain

    masked = username[0]

    masked += "*" * (len(username)-2)

    masked += username[-1]

    return masked + domain


# ============================================================
# Driver Code
# ============================================================

print("71.", count_lowercase("PyTHonAI"))

print("72.", toggle_case("PyThOn"))

print("73.", sort_characters("python"))

print("74.", valid_email("abc@gmail.com"))

print("74.", valid_email("abcgmailcom"))

print("75.", mask_email("johnsmith@gmail.com"))


# ============================================================
# Expected Output
# ============================================================

# 71.
# 3

# 72.
# pYtHoN

# 73.
# hnopty

# 74.
# True

# False

# 75.
# j*******h@gmail.com


# ============================================================
# Complexity
# ============================================================

# Count Lowercase         O(n)     O(1)

# Toggle Case             O(n)     O(n)

# Sort Characters         O(n²)    O(n)

# Valid Email             O(n)     O(1)

# Mask Email              O(n)     O(n)


# ============================================================
# Frequently Asked
# ============================================================

# ✅ TCS
# ✅ Infosys
# ✅ Accenture
# ✅ Capgemini
# ✅ Cognizant
# ✅ IBM
# ✅ Deloitte
# ✅ Wipro
# ✅ HCL
# ✅ Cyntexa
# ============================================================


# ============================================================
# STRING PATTERN - Batch 5B
# Companies:
# TCS | Infosys | Accenture | Capgemini | Cognizant
# IBM | Deloitte | Wipro | HCL | Cyntexa
#
# Optimized Interview Solutions (Python)
# ============================================================


# ------------------------------------------------------------
# 76. Mask Phone Number
# ------------------------------------------------------------
# Problem:
# Hide all digits except last 4 digits.
#
# Example:
# 9876543210
#
# Output:
# ******3210
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def mask_phone(number):

    result = ""

    for i in range(len(number)):

        if i < len(number) - 4:
            result += "*"
        else:
            result += number[i]

    return result


# ------------------------------------------------------------
# 77. Reverse Sentence Without Reversing Words
# ------------------------------------------------------------
# Problem:
# Reverse complete sentence.
#
# Example:
# I Love Python
#
# Output:
# nohtyP evoL I
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def reverse_sentence(sentence):

    result = []

    for i in range(len(sentence)-1, -1, -1):
        result.append(sentence[i])

    return "".join(result)


# ------------------------------------------------------------
# 78. Longest Palindrome Substring (Basic)
# ------------------------------------------------------------
# Problem:
# Find longest palindrome substring.
#
# Example:
# babad
#
# Output:
# bab
#
# Time  : O(n²)
# Space : O(1)
# ------------------------------------------------------------

def longest_palindrome(text):

    longest = ""

    for i in range(len(text)):

        # Odd Length Palindrome
        left = i
        right = i

        while left >= 0 and right < len(text) and text[left] == text[right]:

            if right - left + 1 > len(longest):
                longest = text[left:right+1]

            left -= 1
            right += 1

        # Even Length Palindrome
        left = i
        right = i + 1

        while left >= 0 and right < len(text) and text[left] == text[right]:

            if right - left + 1 > len(longest):
                longest = text[left:right+1]

            left -= 1
            right += 1

    return longest


# ------------------------------------------------------------
# 79. Check String Rotation
# ------------------------------------------------------------
# Problem:
# Check whether s2 is rotation of s1.
#
# Example:
# ABCD
# CDAB
#
# Output:
# True
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def string_rotation(s1, s2):

    if len(s1) != len(s2):
        return False

    return s2 in (s1 + s1)


# ------------------------------------------------------------
# 80. Remove Extra Spaces
# ------------------------------------------------------------
# Problem:
# Remove multiple spaces.
#
# Example:
# I    Love     Python
#
# Output:
# I Love Python
#
# Time  : O(n)
# Space : O(n)
# ------------------------------------------------------------

def remove_extra_spaces(sentence):

    result = ""

    previous_space = False

    for ch in sentence:

        if ch == " ":

            if not previous_space:
                result += ch

            previous_space = True

        else:

            result += ch
            previous_space = False

    return result.strip()


# ============================================================
# Driver Code
# ============================================================

print("76.", mask_phone("9876543210"))

print("77.", reverse_sentence("I Love Python"))

print("78.", longest_palindrome("babad"))

print("79.", string_rotation("ABCD", "CDAB"))

print("80.", remove_extra_spaces("I    Love      Python"))


# ============================================================
# Expected Output
# ============================================================

# 76.
# ******3210

# 77.
# nohtyP evoL I

# 78.
# bab
# (aba is also correct)

# 79.
# True

# 80.
# I Love Python


# ============================================================
# Complexity
# ============================================================

# Mask Phone                 O(n)      O(n)

# Reverse Sentence           O(n)      O(n)

# Longest Palindrome         O(n²)     O(1)

# String Rotation            O(n)      O(n)

# Remove Extra Spaces        O(n)      O(n)


# ============================================================
# Frequently Asked
# ============================================================

# ✅ TCS
# ✅ Infosys
# ✅ Accenture
# ✅ Capgemini
# ✅ Cognizant
# ✅ IBM
# ✅ Deloitte
# ✅ Wipro
# ✅ HCL
# ✅ Cyntexa
# ============================================================
# """
# ===========================
# QUESTION 31 : Find LCM of Two Numbers
# ===========================

# Theory:
# LCM (Least Common Multiple) interview me GCD ke saath bahut common question hai.
# Optimized approach Euclid's Algorithm se GCD nikal kar LCM = (a*b)//GCD use karti hai.

# def gcd(a, b):

#     while b != 0:
#         a, b = b, a % b

#     return a


# def lcm(a, b):

#     return (a * b) // gcd(a, b)


# print(lcm(12, 18))

# Time Complexity : O(log(min(a,b)))
# Space Complexity: O(1)


# ===========================
# QUESTION 32 : Find GCD (HCF)
# ===========================

# Theory:
# GCD finding Euclid's Algorithm ka direct application hai.
# Ye interview me optimization aur mathematical thinking check karta hai.

# def gcd(a, b):

#     while b != 0:
#         a, b = b, a % b

#     return a


# print(gcd(12, 18))

# Time Complexity : O(log(min(a,b)))
# Space Complexity: O(1)


# ===========================
# QUESTION 33 : Check Armstrong Number
# ===========================

# Theory:
# Digits manipulation aur mathematical operations check karne ke liye Armstrong number pucha jata hai.

# def is_armstrong(number):

#     original = number
#     digits = len(str(number))
#     total = 0

#     while number > 0:

#         digit = number % 10
#         total += digit ** digits
#         number //= 10

#     return total == original


# print(is_armstrong(153))

# Time Complexity : O(log n)
# Space Complexity: O(1)


# ===========================
# QUESTION 34 : Count Vowels
# ===========================

# Theory:
# String traversal aur membership operator ('in') ki understanding check karne ke liye common question hai.

# def count_vowels(text):

#     vowels = "aeiouAEIOU"
#     count = 0

#     for ch in text:

#         if ch in vowels:
#             count += 1

#     return count


# print(count_vowels("Hello World"))

# Time Complexity : O(n)
# Space Complexity: O(1)


# ===========================
# QUESTION 35 : Count Consonants
# ===========================

# Theory:
# String processing aur alphabet checking ka interview question hai.
# isalpha() ka use best approach hai.

# def count_consonants(text):

#     vowels = "aeiouAEIOU"
#     count = 0

#     for ch in text:

#         if ch.isalpha() and ch not in vowels:
#             count += 1

#     return count


# print(count_consonants("Hello World"))

# Time Complexity : O(n)
# Space Complexity: O(1)


# ===========================
# QUESTION 36 : Check Leap Year
# ===========================

# Theory:
# Conditional logic check karne ke liye leap year interview ka standard question hai.

# def is_leap_year(year):

#     if year % 400 == 0:
#         return True

#     if year % 100 == 0:
#         return False

#     return year % 4 == 0


# print(is_leap_year(2024))

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 37 : Find ASCII Value
# ===========================

# Theory:
# Character encoding ki basic understanding check karne ke liye ord() function use hota hai.

# def ascii_value(character):

#     return ord(character)


# print(ascii_value("A"))

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 38 : Celsius to Fahrenheit
# ===========================

# Theory:
# Formula implementation aur arithmetic operations check karne ke liye ye basic interview question hai.

# def celsius_to_fahrenheit(celsius):

#     return (celsius * 9 / 5) + 32


# print(celsius_to_fahrenheit(25))

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 39 : Fahrenheit to Celsius
# ===========================

# Theory:
# Temperature conversion ka reverse formula implement karna hota hai.

# def fahrenheit_to_celsius(fahrenheit):

#     return (fahrenheit - 32) * 5 / 9


# print(fahrenheit_to_celsius(77))

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 40 : Generate Random Number (1–10)
# ===========================

# Theory:
# Random number generation games, testing aur simulations me use hoti hai.
# Python me random.randint() optimized approach hai.

# import random

# def generate_random():

#     return random.randint(1, 10)


# print(generate_random())

# Time Complexity : O(1)
# Space Complexity: O(1)
# ```
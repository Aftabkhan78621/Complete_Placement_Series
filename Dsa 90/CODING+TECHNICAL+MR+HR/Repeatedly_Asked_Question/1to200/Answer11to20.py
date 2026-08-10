# """
# ===========================
# QUESTION 11 : Check Positive, Negative or Zero
# ===========================

# Theory:
# Interview me conditional statements aur comparison operators test karne ke liye pucha jata hai.
# Ye basic decision-making problem hai.

# def check_number(number):

#     if number > 0:
#         return "Positive"

#     elif number < 0:
#         return "Negative"

#     return "Zero"


# print(check_number(-15))

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 12 : Factorial of a Number
# ===========================

# Theory:
# Loop aur multiplication logic check karne ke liye common interview question hai.
# Recursion bhi puch sakte hain, lekin iterative approach zyada optimized hai.

# def factorial(number):

#     result = 1

#     for i in range(2, number + 1):
#         result *= i

#     return result


# print(factorial(5))

# Time Complexity : O(n)
# Space Complexity: O(1)


# ===========================
# QUESTION 13 : Fibonacci Series
# ===========================

# Theory:
# Loop, variable update aur sequence generation check karne ke liye pucha jata hai.
# Iterative solution recursion se better hai.

# def fibonacci(n):

#     first = 0
#     second = 1
#     sum = 0

#     for _ in range(n):

#         print(first, end=" ")
#         sum += first
#         first, second = second, first + second
#     return {(first,second),(sum)}

# fibonacci(10)
# print('\n')

# def fibo(n):
#     f = 0
#     s = 1
#     total = 0
#     result = []
#     for _ in range(n):
#         result.append(f)
#         total += f
#         f,s = s, f+s
#     return result,total
# result,total = fibo(5)
# print(result)
# print("sum is: ",total)

# Time Complexity : O(n)
# Space Complexity: O(1)


# ===========================
# QUESTION 14 : Reverse a Number
# ===========================

# Theory:
# Modulo (%) aur integer division (//) ka use check karne ke liye common interview question hai.

# def reverse_number(number):

#     reverse = 0

#     while number > 0:

#         digit = number % 10
#         reverse = reverse * 10 + digit
#         number //= 10

#     return reverse


# print(reverse_number(12345))

# Time Complexity : O(log n)
# Space Complexity: O(1)


# ===========================
# QUESTION 15 : Check Palindrome Number
# ===========================

# Theory:
# Reverse number concept ka application hai.
# Interviewer logical thinking aur arithmetic operations check karta hai.

# def palindrome_number(number):

#     original = number
#     reverse = 0

#     while number > 0:

#         digit = number % 10
#         reverse = reverse * 10 + digit
#         number //= 10

#     return original == reverse


# print(palindrome_number(121))

# Time Complexity : O(log n)
# Space Complexity: O(1)


# ===========================
# QUESTION 16 : Check Prime Number
# ===========================

# Theory:
# Optimization check karne ke liye important question hai.
# Square root tak check karna interview standard approach hai.

# def is_prime(number):

#     if number < 2:
#         return False

#     i = 2

#     while i * i <= number:

#         if number % i == 0:
#             return False

#         i += 1

#     return True


# print(is_prime(29))

# Time Complexity : O(√n)
# Space Complexity: O(1)


# ===========================
# QUESTION 17 : Print Prime Numbers Between 1–100
# ===========================

# Theory:
# Prime checking ko multiple numbers par apply karna hota hai.
# Interview me nested logic check hota hai.

# def print_primes(limit):

#     for number in range(2, limit + 1):

#         prime = True

#         i = 2

#         while i * i <= number:

#             if number % i == 0:
#                 prime = False
#                 break

#             i += 1

#         if prime:
#             print(number, end=" ")


# print_primes(100)

# Time Complexity : O(n√n)
# Space Complexity: O(1)


# ===========================
# QUESTION 18 : Print Table of a Number
# ===========================

# Theory:
# Loop aur multiplication ka basic application hai.

# def multiplication_table(number):

#     for i in range(1, 11):
#         print(f"{number} x {i} = {number * i}")


# multiplication_table(5)

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 19 : Sum of Digits
# ===========================

# Theory:
# Modulo aur integer division ka ek aur important application.
# Interview me frequently pucha jata hai.

# def sum_of_digits(number):

#     total = 0

#     while number > 0:

#         total += number % 10
#         number //= 10

#     return total


# print(sum_of_digits(9876))

# Time Complexity : O(log n)
# Space Complexity: O(1)


# ===========================
# QUESTION 20 : Power Without Math.pow()
# ===========================

# Theory:
# Loop aur repeated multiplication ka concept check kiya jata hai.
# Math.pow() use nahi karna hota.

# def power(base, exponent):

#     result = 1

#     for _ in range(exponent):
#         result *= base

#     return result


# print(power(2, 5))

# Time Complexity : O(n)
# Space Complexity: O(1)
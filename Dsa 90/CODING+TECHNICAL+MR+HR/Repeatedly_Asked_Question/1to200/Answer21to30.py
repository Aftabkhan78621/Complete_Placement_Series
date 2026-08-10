# """
# ===========================
# QUESTION 21 : Print Numbers 1–100
# ===========================

# Theory:
# Interview me loop fundamentals check karne ke liye ye basic question pucha jata hai.
# Candidate ko loop syntax aur iteration ki understanding honi chahiye.

# def print_numbers():

#     for number in range(1, 101):
#         print(number, end=" ")


# print_numbers()

# Time Complexity : O(n)
# Space Complexity: O(1)


# ===========================
# QUESTION 22 : Print Even Numbers
# ===========================

# Theory:
# Modulo operator aur loop ka basic application hai.
# Optimized approach me step size 2 use karte hain.

# def print_even_numbers():

#     for number in range(2, 101, 2):
#         print(number, end=" ")


# print_even_numbers()

# Time Complexity : O(n)
# Space Complexity: O(1)


# ===========================
# QUESTION 23 : Print Odd Numbers
# ===========================

# Theory:
# Even numbers ki tarah hi ye bhi loop traversal check karta hai.
# Step size 2 best approach hai.

# def print_odd_numbers():

#     for number in range(1, 101, 2):
#         print(number, end=" ")


# print_odd_numbers()

# Time Complexity : O(n)
# Space Complexity: O(1)


# ===========================
# QUESTION 24 : Count Digits
# ===========================

# Theory:
# Modulo aur integer division ka interview favorite application hai.
# Number processing questions ka base concept hai.

# def count_digits(number):

#     if number == 0:
#         return 1

#     count = 0

#     while number > 0:

#         count += 1
#         number //= 10

#     return count


# print(count_digits(123456))

# Time Complexity : O(log n)
# Space Complexity: O(1)


# ===========================
# QUESTION 25 : Sum of First N Natural Numbers
# ===========================

# Theory:
# Interviewer mathematical optimization check kar sakta hai.
# Formula approach loop se better hai.

# def sum_of_n_numbers(n):

#     return n * (n + 1) // 2


# print(sum_of_n_numbers(10))

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 26 : Print Star Pattern
# ===========================

# Theory:
# Nested loops aur pattern logic check karne ke liye ye bahut common interview question hai.

# def star_pattern(rows):

#     for i in range(1, rows + 1):
#         print("*" * i)


# star_pattern(5)

# Time Complexity : O(n²)
# Space Complexity: O(1)


# ===========================
# QUESTION 27 : Reverse Star Pattern
# ===========================

# Theory:
# Pattern questions me decreasing loop aur nested logic check ki jati hai.

# def reverse_star_pattern(rows):

#     for i in range(rows, 0, -1):
#         print("*" * i)


# reverse_star_pattern(5)

# Time Complexity : O(n²)
# Space Complexity: O(1)


# ===========================
# QUESTION 28 : Break vs Continue
# ===========================

# Theory:
# Control statements ki understanding check karne ke liye interviewer ye question puch sakta hai.

# def break_continue_demo():

#     print("Break Example")

#     for i in range(1, 11):

#         if i == 6:
#             break

#         print(i, end=" ")

#     print()

#     print("Continue Example")

#     for i in range(1, 11):

#         if i == 6:
#             continue

#         print(i, end=" ")


# break_continue_demo()

# Time Complexity : O(n)
# Space Complexity: O(1)


# ===========================
# QUESTION 29 : Nested Loop Example
# ===========================

# Theory:
# Nested loops ka use matrix, pattern aur combinations me hota hai.
# Interview me basic understanding check hoti hai.

# def nested_loop(rows, columns):

#     for i in range(rows):

#         for j in range(columns):
#             print(f"({i},{j})", end=" ")

#         print()


# nested_loop(3, 3)

# Time Complexity : O(rows × columns)
# Space Complexity: O(1)


# ===========================
# QUESTION 30 : Multiplication Table (1–10)
# ===========================

# Theory:
# Nested loops ka practical application hai.
# Loop control aur multiplication logic test hota hai.

# def multiplication_tables():

#     for table in range(1, 11):

#         print(f"\nTable of {table}")

#         for number in range(1, 11):
#             print(f"{table} x {number} = {table * number}")


# multiplication_tables()

# Time Complexity : O(1)
# Space Complexity: O(1)
# ```
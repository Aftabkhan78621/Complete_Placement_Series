# """
# ===========================
# QUESTION 1 : Print Hello World
# ===========================

# Theory:
# Ye sabse basic interview question hai jo language syntax aur output statement check karta hai.
# Mostly warm-up question hota hai.

# def print_hello():
#     print("Hello World")


# print_hello()

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 2 : Declare Variables
# ===========================

# Theory:
# Interviewer check karta hai ki variable declaration aur naming conventions aati hain ya nahi.

# def declare_variables():

#     age = 21
#     name = "Aftab"
#     salary = 25000.50
#     is_student = True

#     print(age)
#     print(name)
#     print(salary)
#     print(is_student)


# declare_variables()

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 3 : Difference between let, var, const (Python)
# ===========================

# Theory:
# Python me var, let aur const nahi hote.
# Python dynamically typed language hai.

# def variable_demo():

#     number = 10
#     number = 20

#     PI = 3.14159      # Constant by convention only

#     print(number)
#     print(PI)


# variable_demo()

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 4 : Check Data Type
# ===========================

# Theory:
# Interview me datatype understanding check karne ke liye puchte hain.

# def check_type(value):

#     return type(value)


# print(check_type(10))
# print(check_type("Python"))
# print(check_type(10.5))

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 5 : String to Number
# ===========================

# Theory:
# Input handling me bahut common conversion question hai.

# def string_to_number(value):

#     return int(value)


# print(string_to_number("123"))

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 6 : Number to String
# ===========================

# Theory:
# Output formatting aur concatenation me use hota hai.

# def number_to_string(number):

#     return str(number)


# print(number_to_string(123))

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 7 : Swap Without Third Variable
# ===========================

# Theory:
# Interviewer tuple unpacking ya arithmetic thinking check karta hai.

# def swap_numbers(a, b):

#     a, b = b, a

#     return a, b


# print(swap_numbers(10, 20))

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 8 : Even or Odd
# ===========================

# Theory:
# Modulo operator ka basic application.

# def even_or_odd(number):

#     if number % 2 == 0:
#         return "Even"

#     return "Odd"


# print(even_or_odd(15))

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 9 : Largest of Two Numbers
# ===========================

# Theory:
# Conditional statements aur comparison operators check kiye jate hain.

# def largest_of_two(a, b):

#     if a > b:
#         return a

#     return b


# print(largest_of_two(15, 25))

# Time Complexity : O(1)
# Space Complexity: O(1)


# ===========================
# QUESTION 10 : Largest of Three Numbers
# ===========================

# Theory:
# Multiple conditions aur logical comparison ka basic interview question.

# def largest_of_three(a, b, c):

#     largest = a

#     if b > largest:
#         largest = b

#     if c > largest:
#         largest = c

#     return largest


# print(largest_of_three(15, 90, 35))

# Time Complexity : O(1)
# Space Complexity: O(1)
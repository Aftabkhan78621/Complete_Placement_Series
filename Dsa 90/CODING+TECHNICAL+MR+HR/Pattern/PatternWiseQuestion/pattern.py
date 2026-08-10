# ============================================================
# PATTERN 1 : RIGHT TRIANGLE STAR PATTERN
# ============================================================

# Output (n = 5)
#
# *
# * *
# * * *
# * * * *
# * * * * *

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

"""
EXPLANATION

The first thing you should observe is how many rows are present. Here there are
5 rows. Now look carefully at each row. In the first row there is 1 star,
in the second row there are 2 stars, in the third row there are 3 stars and
so on. This means the number of stars is always equal to the current row
number. Therefore the outer loop controls the rows while the inner loop prints
the stars. The inner loop simply runs 'i' times because row i needs i stars.
After every row we call print() so that the cursor moves to the next line.
Whenever you see a similar increasing pattern in an interview, always think:
"What is increasing every row?" Here the answer is stars, so the inner loop
depends on the row number.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 2 : INVERTED RIGHT TRIANGLE
# ============================================================

# Output
#
# * * * * *
# * * * *
# * * *
# * *
# *

n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

"""
EXPLANATION

This pattern is exactly opposite to Pattern 1. Instead of increasing stars,
the stars decrease after every row. The first row contains n stars, the second
contains n-1 stars and the last row contains only one star. Therefore the outer
loop starts from n and decreases until 1. Since the current row value already
represents the number of stars needed, the inner loop runs exactly i times.
Whenever you see an inverted pattern, simply think that the counting direction
has changed. Instead of moving from 1 to n, you move from n to 1.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 3 : LEFT ALIGNED TRIANGLE
# ============================================================

# Output
#
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

n = 5

for i in range(1, n + 1):

    # Print Spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Print Stars
    for j in range(i):
        print("*", end=" ")

    print()

"""
EXPLANATION

This pattern introduces spaces before stars. First observe that stars are still
increasing exactly like Pattern 1. The only difference is that every row starts
with some blank spaces. The number of leading spaces decreases by one after
every row. Therefore there are two inner loops. The first inner loop prints
spaces and the second prints stars. The formula is very easy:
Spaces = n - row number
Stars = row number
Whenever you see any shifted pattern, first calculate spaces and then calculate
symbols. This is one of the most common interview tricks.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 4 : INVERTED LEFT TRIANGLE
# ============================================================

# Output
#
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

n = 5

for i in range(n, 0, -1):

    # Spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Stars
    for j in range(i):
        print("*", end=" ")

    print()

"""
EXPLANATION

This pattern combines the ideas of Pattern 2 and Pattern 3. Stars decrease but
spaces increase. The first row has zero spaces and maximum stars. Every next
row adds one more leading space and removes one star. Therefore:
Spaces = n - current row
Stars = current row
Whenever you solve a pattern like this, separate the problem into two parts.
First calculate spaces, then calculate stars. Solving one component at a time
makes the logic very easy.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 5 : PYRAMID STAR PATTERN
# ============================================================

# Output
#
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

n = 5

for i in range(1, n + 1):

    # Spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Stars
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()

"""
EXPLANATION

The pyramid pattern is one of the most frequently asked placement questions.
Observe carefully that spaces decrease while stars increase. However, unlike
the triangle, the stars increase by two in every row because the pyramid must
remain symmetrical. The star sequence is:
1, 3, 5, 7, 9 ...
This is the sequence of odd numbers. The formula for odd numbers is:
Stars = 2 × row - 1
The spaces are still:
Spaces = n - row
Therefore the algorithm becomes very simple. First print the required spaces,
then print the required odd number of stars. Whenever you encounter any pyramid,
always remember the formula 2*i-1. Most interviewers expect candidates to
identify this formula quickly rather than memorize the entire pattern.

Time Complexity : O(n²)
Space Complexity : O(1)
"""

# ============================================================
# UNIVERSAL INTERVIEW APPROACH FOR PATTERN QUESTIONS
# ============================================================

"""
Before writing code for any pattern, always follow these five steps.

Step 1: Count the number of rows.

Step 2: Observe what changes in every row. It may be stars, numbers,
alphabets or spaces.

Step 3: Find the mathematical formula. Examples:
Stars = i
Stars = n - i + 1
Spaces = n - i
Stars = 2*i - 1

Step 4: Write the outer loop for rows.

Step 5: Write one inner loop for every component.
If a pattern contains spaces and stars, you need two inner loops.
If it contains spaces, numbers and stars, you need three inner loops.

This thinking process works for almost every pattern question asked in campus
placements such as Cyntexa, TCS, Infosys, Capgemini, Cognizant, Accenture,
Deloitte and many other companies.
"""


# ============================================================
# PATTERN 6 : INVERTED PYRAMID
# ============================================================

# Output (n = 5)
#
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

n = 5

for i in range(n, 0, -1):

    # Print Spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Print Stars
    for j in range(2 * i - 1):
        print("*", end=" ")

    print()

"""
EXPLANATION

This pattern is exactly opposite to the normal pyramid. The first row contains
the maximum number of stars and each next row removes two stars while adding
one leading space. The star sequence becomes 9, 7, 5, 3, 1 when n = 5.
Since a pyramid always follows odd numbers, the formula remains
Stars = 2*i - 1. The only difference is that the outer loop starts from n and
moves towards 1. Spaces increase gradually while stars decrease gradually.
Whenever you see an inverted pyramid, simply reverse the outer loop of the
normal pyramid.

Formula:
Spaces = n - i
Stars  = 2*i - 1

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 7 : DIAMOND PATTERN
# ============================================================

# Output
#
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
def upper_pyramid(n):
    for i in range(1, n + 1):

        # Print Spaces
        for j in range(n - i):
            print(" ", end=" ")

        # Print Stars
        for j in range(2 * i - 1):
            print("*", end=" ")

        print()


def lower_inverted_pyramid(n):
    for i in range(n - 1, 0, -1):

        # Print Spaces
        for j in range(n - i):
            print(" ", end=" ")

        # Print Stars
        for j in range(2 * i - 1):
            print("*", end=" ")

        print()


def diamond_pattern(n):
    upper_pyramid(n)
    lower_inverted_pyramid(n)


# Driver Code
n = 5
diamond_pattern(n)

"""
EXPLANATION

A diamond is nothing but two patterns joined together. The upper half is a
normal pyramid while the lower half is an inverted pyramid. Instead of trying
to invent a completely new solution, simply reuse the previous two patterns.
This is an important interview skill because many difficult patterns are
actually combinations of easier patterns. Build the upper half first and then
attach the lower half without printing the middle row twice.

Think:
Upper Half  -> Pyramid
Lower Half  -> Inverted Pyramid

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 8 : HOLLOW DIAMOND
# ============================================================

# Output
#
#         *
#       *   *
#     *       *
#   *           *
# *               *
#   *           *
#     *       *
#       *   *
#         *

n = 5

# Upper Part
for i in range(1, n + 1):

    # Left Spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Hollow Logic
    for j in range(2 * i - 1):

        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")

    print()

# Lower Part
for i in range(n - 1, 0, -1):

    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):

        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")

    print()

"""
EXPLANATION

A hollow pattern means only the boundary should contain stars while everything
inside remains empty. Therefore, while printing each row, print a star only
when you are at the first position or the last position. Every middle position
prints a space. The diamond is again formed by joining an upper hollow pyramid
and a lower hollow inverted pyramid. Most hollow patterns are solved using the
same boundary condition.

Boundary Condition:
First Position  -> *
Last Position   -> *
Middle          -> Space

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 9 : FULL PASCAL TRIANGLE PATTERN
# ============================================================

# Output
#
#         *
#       * *
#     * * * *
#   * * * * * * * *
# * * * * * * * * * * * * * * * *

n = 5

# Left Triangle
for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()

# Right Triangle
for i in range(n - 1, 0, -1):

    for j in range(n - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()

"""
EXPLANATION

The Full Pascal Star Pattern is formed by combining a right triangle and an
inverted right triangle. Unlike the mathematical Pascal Triangle, this pattern
contains only stars. The upper half continuously increases the number of stars,
while the lower half decreases them. The logic is exactly the same as joining
two opposite triangles. Whenever a pattern looks symmetric, try breaking it
into two familiar patterns instead of solving everything together.

Think:
Triangle + Inverted Triangle = Full Pascal Pattern

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 10 : BUTTERFLY PATTERN
# ============================================================

# Output
#
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *

n = 5

# Upper Part
for i in range(1, n + 1):

    # Left Wing
    for j in range(i):
        print("*", end=" ")

    # Middle Spaces
    for j in range(2 * (n - i)):
        print(" ", end=" ")

    # Right Wing
    for j in range(i):
        print("*", end=" ")

    print()

# Lower Part
for i in range(n - 1, 0, -1):

    for j in range(i):
        print("*", end=" ")

    for j in range(2 * (n - i)):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()

"""
EXPLANATION

The butterfly pattern consists of two identical wings separated by spaces.
The left wing is a right triangle, while the right wing is another right
triangle printed after some spaces. As the rows increase, the wings become
larger and the middle gap becomes smaller. After reaching the center, the
process reverses. Therefore, this pattern is simply an upper half and a lower
half. The important observation is that the number of stars equals the row
number while the middle spaces equal 2 × (n − row).

Formula:
Left Stars   = i
Middle Space = 2*(n-i)
Right Stars  = i

Time Complexity : O(n²)
Space Complexity : O(1)
"""

# ============================================================
# MASTER APPROACH (Patterns 6-10)
# ============================================================

"""
The biggest mistake students make is memorizing patterns. Interviewers are not
testing memory; they are testing observation. Every pattern can be solved by
answering four questions:

1. How many rows are there?
2. How many spaces are needed?
3. How many symbols (stars/numbers/letters) are needed?
4. Is the pattern made by combining smaller patterns?

For example:
• Inverted Pyramid = Reverse Pyramid
• Diamond = Pyramid + Inverted Pyramid
• Hollow Diamond = Hollow Pyramid + Hollow Inverted Pyramid
• Pascal Star Pattern = Triangle + Reverse Triangle
• Butterfly = Two Triangles + Middle Spaces

If you learn to identify these building blocks, you can solve almost every
pattern asked in campus placements without memorizing the code.
"""



# ============================================================
# PATTERN 11 : HOLLOW SQUARE PATTERN
# ============================================================

# Output (n = 5)
#
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

n = 5

for i in range(n):

    # Print Columns
    for j in range(n):

        # Boundary Condition
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


"""
EXPLANATION

A Hollow Square Pattern means only the outer boundary contains stars while the
inside of the square remains empty. Unlike the Solid Square where every position
prints a star, here we first check whether the current position lies on the
boundary. The boundary consists of the first row, last row, first column and
last column. If the current position belongs to any one of these boundaries,
we print a star. Otherwise we print a blank space.

Think of the square as a matrix having rows and columns. Every position is
represented by (i, j). Before printing anything, simply ask yourself:
"Is this position on the boundary?"
If the answer is Yes, print "*".
Otherwise print a space.

This is the basic logic behind almost every hollow pattern asked in interviews.
Only the boundary is printed while the inside remains empty.


Boundary Conditions

First Row    : i == 0
Last Row     : i == n - 1
First Column : j == 0
Last Column  : j == n - 1

If any one of these conditions is true,
print a star.


Algorithm

Step 1:
Run the outer loop for all rows.

Step 2:
Run the inner loop for all columns.

Step 3:
Check whether the current position lies on the boundary.

Step 4:
If yes, print "*".

Step 5:
Otherwise print a blank space.

Step 6:
Move to the next line after completing each row.


Dry Run (n = 5)

i = 0

*****
(All positions are in the first row.)

------------------------

i = 1

*   *
(Only first and last columns print stars.)

------------------------

i = 2

*   *

------------------------

i = 3

*   *

------------------------

i = 4

*****
(All positions are in the last row.)


Formula

Rows    = n
Columns = n

Boundary

i == 0
OR
i == n - 1
OR
j == 0
OR
j == n - 1


Time Complexity : O(n²)

Reason:
There are n rows and n columns.

Space Complexity : O(1)

Reason:
No extra array or list is used.


Interview Tip

Whenever you hear the word "Hollow", immediately think:

"Print only the boundary."

Then identify

✔ First Row
✔ Last Row
✔ First Column
✔ Last Column

Every hollow pattern (Square, Rectangle, Diamond, Pyramid, Butterfly, etc.)
uses this same boundary concept. Once you master this logic, solving hollow
patterns becomes much easier.
"""


# ============================================================
# PATTERN 12 : SOLID SQUARE PATTERN
# ============================================================

# Output (n = 5)
#
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

n = 5

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

"""
DESCRIPTION

A Solid Square is the simplest pattern. Every row contains the same number
of stars and every column also contains the same number of stars. Since
nothing changes from row to row, both loops simply run n times.

Formula
Rows    = n
Columns = n

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 13 : HOLLOW RECTANGLE PATTERN
# ============================================================

# Output (Rows = 4, Columns = 7)
#
# * * * * * * *
# *           *
# *           *
# * * * * * * *

rows = 4
cols = 7

for i in range(rows):
    for j in range(cols):

        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

"""
DESCRIPTION

A Hollow Rectangle is similar to a Hollow Square. The only difference is
that the number of rows and columns are different. Print stars only on
the boundary and spaces inside.

Formula
Rows    = rows
Columns = cols

Boundary:
i == 0
i == rows - 1
j == 0
j == cols - 1

Time Complexity : O(rows × cols)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 14 : NUMBER TRIANGLE
# ============================================================

# Output (n = 5)
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

"""
DESCRIPTION

In this pattern, every row starts from 1 and ends at the current row
number. The number of elements increases by one in each row.

Formula
Rows = n
Numbers = Row Number

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 15 : FLOYD'S TRIANGLE
# ============================================================

# Output (n = 5)
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = 5
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

"""
DESCRIPTION

Floyd's Triangle prints continuous numbers instead of restarting from 1.
A variable 'num' stores the current value and increases after every print.

Formula
Rows = n
Numbers = Continuous

Time Complexity : O(n²)
Space Complexity : O(1)
"""


# ============================================================
# PATTERN 16 : PASCAL'S TRIANGLE
# ============================================================

# Output (n = 5)
#
#         1
#       1 1
#     1 2 1
#   1 3 3 1
# 1 4 6 4 1

n = 5

for i in range(n):

    num = 1

    for j in range(n - i - 1):
        print(" ", end=" ")

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()

"""
DESCRIPTION

Pascal's Triangle contains binomial coefficients.
Every row starts and ends with 1.
The middle values are calculated using the formula.

Formula
num = num * (i - j) // (j + 1)

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")


# ============================================================
# PATTERN 17 : 0-1 TRIANGLE PATTERN
# ============================================================

# Output (n = 5)
#
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

n = 5

for i in range(1, n + 1):

    for j in range(1, i + 1):

        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")

    print()

"""
DESCRIPTION

This pattern prints alternate 0 and 1.
The value depends on whether (row + column)
is even or odd.

Formula

(i + j) % 2 == 0 → 1
Else              → 0

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")


# ============================================================
# PATTERN 18 : CHARACTER TRIANGLE
# ============================================================

# Output (n = 5)
#
# A
# A B
# A B C
# A B C D
# A B C D E

n = 5

for i in range(1, n + 1):

    ch = 65

    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1

    print()

"""
DESCRIPTION

This pattern prints alphabets instead of stars.
Every row starts from A and continues up to
the current row.

Formula

ASCII of A = 65
chr(65) = A

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")


# ============================================================
# PATTERN 19 : REVERSE CHARACTER TRIANGLE
# ============================================================

# Output (n = 5)
#
# A B C D E
# A B C D
# A B C
# A B
# A

n = 5

for i in range(n, 0, -1):

    ch = 65

    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1

    print()

"""
DESCRIPTION

This is the reverse of Character Triangle.
The first row prints maximum alphabets and
each next row prints one less alphabet.

Formula

Characters = Current Row

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")


# ============================================================
# PATTERN 20 : CONTINUOUS NUMBER TRIANGLE
# ============================================================

# Output (n = 5)
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = 5
num = 1

for i in range(1, n + 1):

    for j in range(i):
        print(num, end=" ")
        num += 1

    print()

"""
DESCRIPTION

Continuous Number Triangle prints numbers
continuously without restarting from 1.
A variable 'num' stores the current value
and increases after every print.

Formula

Print num
num += 1

Time Complexity : O(n²)
Space Complexity : O(1)
"""


# ============================================================
# PATTERN 20 : CONTINUOUS NUMBER TRIANGLE
# ============================================================

# Output (n = 5)
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = 5
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

"""
DESCRIPTION

Numbers are printed continuously.
The value never restarts from 1.

Formula
Print num
num += 1

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 21 : PALINDROME NUMBER PYRAMID
# ============================================================

# Output (n = 5)
#
#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5

n = 5

for i in range(1, n + 1):

    # Spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Descending Numbers
    for j in range(i, 0, -1):
        print(j, end=" ")

    # Ascending Numbers
    for j in range(2, i + 1):
        print(j, end=" ")

    print()

"""
DESCRIPTION

Print spaces first.
Then print numbers in descending order.
Finally print numbers in ascending order.

Formula

Spaces      = n - i
Descending  = i → 1
Ascending   = 2 → i

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 22 : PALINDROME ALPHABET PYRAMID
# ============================================================

# Output (n = 5)
#
#         A
#       B A B
#     C B A B C
#   D C B A B C D
# E D C B A B C D E

n = 5

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end=" ")

    # Descending Alphabets
    for j in range(i, 0, -1):
        print(chr(64 + j), end=" ")

    # Ascending Alphabets
    for j in range(2, i + 1):
        print(chr(64 + j), end=" ")

    print()

"""
DESCRIPTION

Same logic as Palindrome Number Pyramid.
Only numbers are replaced with alphabets.

Formula

chr(65) = A

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 23 : HOLLOW PYRAMID
# ============================================================

# Output (n = 5)
#
#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *

n = 5

for i in range(1, n + 1):

    # Spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Hollow Stars
    for j in range(2 * i - 1):

        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="")
        else:
            print(" ", end="")

    print()

"""
DESCRIPTION

Print stars only on the boundary.
The last row is completely filled.

Formula

Boundary:
j == 0
j == 2*i-2
or Last Row

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 24 : HOLLOW INVERTED PYRAMID
# ============================================================

# Output (n = 5)
#
# * * * * * * * * *
#   *           *
#     *       *
#       *   *
#         *

n = 5

for i in range(n, 0, -1):

    # Spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Hollow Stars
    for j in range(2 * i - 1):

        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="")
        else:
            print(" ", end="")

    print()

"""
DESCRIPTION

Reverse of Hollow Pyramid.
First row is completely filled.
Remaining rows print only boundary stars.

Formula

Boundary:
j == 0
j == 2*i-2
or First Row

Time Complexity : O(n²)
Space Complexity : O(1)
"""

print("\n")

# ============================================================
# PATTERN 25 : HOLLOW RIGHT TRIANGLE
# ============================================================

# Output (n = 5)
#
# *
# * *
# *   *
# *     *
# * * * * *

n = 5

for i in range(1, n + 1):

    for j in range(1, i + 1):

        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

"""
DESCRIPTION

Print stars on the first column,
diagonal and last row.
All remaining positions are spaces.

Formula

Boundary

j == 1
j == i
i == n

Time Complexity : O(n²)
Space Complexity : O(1)
"""
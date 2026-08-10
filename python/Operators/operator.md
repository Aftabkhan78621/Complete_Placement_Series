==========================================================
                 PYTHON NOTES - LESSON 9
                    PYTHON OPERATORS
==========================================================

Definition
----------
• Operators are special symbols used to perform operations on variables and values.
• Python provides different types of operators for arithmetic, comparison, assignment, logical, identity, membership, bitwise operations, and operator precedence.

Python Operator Types
---------------------
1. Arithmetic Operators
2. Assignment Operators
3. Ternary Operator
4. Comparison Operators
5. Logical Operators
6. Identity Operators
7. Membership Operators
8. Bitwise Operators
9. Operator Precedence

==========================================================
1. ARITHMETIC OPERATORS
==========================================================

Definition
----------
Used to perform mathematical calculations.

| Operator | Name | Example |
|----------|------|---------|
| + | Addition | x + y |
| - | Subtraction | x - y |
| * | Multiplication | x * y |
| / | Division | x / y |
| % | Modulus (Remainder) | x % y |
| ** | Exponent (Power) | x ** y |
| // | Floor Division | x // y |

Example
-------
```python
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333
print(a % b)    # 1
print(a ** b)   # 1000
print(a // b)   # 3
```

Interview Points
----------------
• "/" always returns float.
• "//" removes decimal part.
• "%" returns remainder.
• "**" calculates powers.

==========================================================
2. ASSIGNMENT OPERATORS
==========================================================

Definition
----------
Used to assign or update values of variables.

| Operator | Same As |
|----------|---------|
| = | x = 5 |
| += | x = x + 3 |
| -= | x = x - 3 |
| *= | x = x * 3 |
| /= | x = x / 3 |
| %= | x = x % 3 |
| //= | x = x // 3 |
| **= | x = x ** 3 |
| &= | x = x & 3 |
| \|= | x = x \| 3 |
| ^= | x = x ^ 3 |
| >>= | x = x >> 3 |
| <<= | x = x << 3 |
| := | Walrus Operator |

Example
-------
```python
x = 10
x += 5
print(x)      # 15

x *= 2
print(x)      # 30
```

Walrus Operator (:=)
--------------------
• Introduced in Python 3.8.
• Assigns and returns a value in a single expression.

Example
-------
```python
numbers = [1,2,3,4,5]

if (count := len(numbers)) > 3:
    print(count)
```

Interview Point
---------------
• Used to avoid repeated calculations.
• Common in loops and conditions.

==========================================================
3. TERNARY OPERATOR
==========================================================

Definition
----------
A shorthand for if-else.

Syntax
------
```python
value_if_true if condition else value_if_false
```

Example
-------
```python
age = 20

status = "Adult" if age >= 18 else "Minor"
print(status)
```

Nested Ternary
--------------
```python
num = 6

day = "Fri" if num == 5 else \
      "Sat" if num == 6 else \
      "Sun" if num == 7 else \
      "Weekday"

print(day)
```

Interview Point
---------------
• Best for simple conditions.
• Avoid very deep nested ternary expressions.

==========================================================
4. COMPARISON OPERATORS
==========================================================

Definition
----------
Used to compare two values.
Returns True or False.

| Operator | Meaning |
|----------|---------|
| == | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

Example
-------
```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a >= b)
```

Interview Point
---------------
• Always returns Boolean values.

==========================================================
5. LOGICAL OPERATORS
==========================================================

Definition
----------
Used to combine conditional expressions.

| Operator | Description |
|----------|-------------|
| and | True if both conditions are True |
| or | True if any one condition is True |
| not | Reverses Boolean result |

Examples
--------

```python
x = 5

print(x > 0 and x < 10)
```

```python
print(x < 5 or x > 10)
```

```python
print(not(x > 3 and x < 10))
```

Truth Table
-----------

AND

True and True → True

True and False → False

False and True → False

False and False → False

OR

True or False → True

False or True → True

False or False → False

NOT

not True → False

not False → True

==========================================================
6. IDENTITY OPERATORS
==========================================================

Definition
----------
Checks whether two variables refer to the same object in memory.

| Operator | Meaning |
|----------|---------|
| is | Same object |
| is not | Different object |

Example
-------
```python
x = [1,2,3]
y = [1,2,3]
z = x

print(x == y)     # True
print(x is y)     # False
print(x is z)     # True
```

Interview Difference
--------------------

==  → Compares values.

is  → Compares memory locations.

==========================================================
7. MEMBERSHIP OPERATORS
==========================================================

Definition
----------
Checks whether a value exists inside a sequence.

| Operator | Meaning |
|----------|---------|
| in | Present |
| not in | Not Present |

Example
-------
```python
fruits = ["apple","banana","cherry"]

print("banana" in fruits)
print("mango" not in fruits)
```

Membership in Strings
---------------------

```python
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)
```

Interview Point
---------------
• Works with strings, lists, tuples, sets, dictionaries and other iterables.

==========================================================
8. BITWISE OPERATORS
==========================================================

Definition
----------
Operate directly on binary bits.

| Operator | Name |
|----------|------|
| & | AND |
| \| | OR |
| ^ | XOR |
| ~ | NOT |
| << | Left Shift |
| >> | Right Shift |

Examples
--------

Bitwise AND

```python
print(6 & 3)
# 2
```

Bitwise OR

```python
print(6 | 3)
# 7
```

Bitwise XOR

```python
print(6 ^ 3)
# 5
```

Bitwise NOT

```python
print(~6)
# -7
```

Left Shift

```python
print(6 << 1)
# 12
```

Right Shift

```python
print(6 >> 1)
# 3
```

Interview Point
---------------
• Frequently used in low-level programming and optimization.

==========================================================
9. OPERATOR PRECEDENCE
==========================================================

Definition
----------
Determines the order in which operators are evaluated.

Highest to Lowest
-----------------

1. ()
2. **
3. +x, -x, ~x
4. *, /, //, %
5. +, -
6. <<, >>
7. &
8. ^
9. |
10. ==, !=, >, >=, <, <=, is, is not, in, not in
11. not
12. and
13. or

Examples
--------

```python
print((6 + 3) - (6 + 3))
```

```python
print(100 + 5 * 3)
# 115
```

==========================================================
COMMON INTERVIEW QUESTIONS
==========================================================

1. Difference between "/" and "//"?
2. Difference between "==" and "is"?
3. What is the Walrus operator?
4. Explain Bitwise operators.
5. Difference between Assignment and Arithmetic operators.
6. What is Operator Precedence?
7. Difference between "in" and "is"?
8. Explain Logical operators with truth table.
9. What does "%" operator return?
10. What is Nested Ternary Operator?

==========================================================
COMMON MISTAKES
==========================================================

• Confusing == with =.
• Confusing == and is.
• Forgetting operator precedence.
• Using / instead of //.
• Overusing nested ternary operators.
• Forgetting that "in" is case-sensitive for strings.

==========================================================
MEMORY TRICKS
==========================================================

• == → Value
• is → Identity (Memory)
• in → Inside
• % → Remainder
• // → Integer Division
• ** → Power
• and → Both
• or → Any
• not → Reverse

==========================================================
KEY POINTS FOR INTERVIEW
==========================================================

• Python has 9 major categories of operators.
• Comparison operators always return Boolean values.
• "is" checks object identity, not value equality.
• Walrus operator (:=) was introduced in Python 3.8.
• Bitwise operators work on binary representation.
• Parentheses have the highest precedence.
• "and" has higher precedence than "or".
• Membership operators work on sequences.
==========================================================
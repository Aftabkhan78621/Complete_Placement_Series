# Python Notes

`Topic: Python Numbers`

```text
Python has three built-in numeric data types:

• int – Stores whole numbers without decimal values.
• float – Stores numbers with decimal values.
• complex – Stores complex numbers with a real and an imaginary part.

Numeric variables are created automatically when a value is assigned to them. You can use the type() function to check the data type of any variable.
```

Example:

```python
x = 1          # int
y = 2.8        # float
z = 1j         # complex

print(type(x))
print(type(y))
print(type(z))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'complex'>
```

---

`Topic: Random Number`

```text
Python does not have a built-in random() function to generate random numbers directly. Instead, it provides a built-in module named random. By importing this module, you can generate random numbers using different functions such as randrange().
```

Example:

```python
import random

print(random.randrange(1, 10))
```

Output:

```text
Any random number between 1 and 9
```

---

`Topic: Casting Challenge`

```text
This coding challenge demonstrates how to convert an integer into different data types using type casting. First, create an integer variable. Then convert it into a float and a string, store the converted values in separate variables, and print them.
```

Example:

```python
# Create an integer
x = 1

# Convert to float
a = float(x)

# Convert to string
b = str(x)

# Print values
print(a)
print(b)
```

Output:

```text
1.0
1
```

---

`Topic: Multiline Strings`

```text
Python allows multiline strings by using either three double quotes (""") or three single quotes ('''). Everything written between the triple quotes becomes part of the string, including line breaks.
```

Example (Triple Double Quotes):

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)
```

Output:

```text
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
```

Example (Triple Single Quotes):

```python
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)
```

Output:

```text
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
```

---

`Topic: Slice From the Start`

```text
When the starting index is omitted, Python automatically starts slicing from index 0 (the first character). The ending index is not included in the result.
```

Example:

```python
b = "Hello, World!"

print(b[:5])
```

Output:

```text
Hello
```

Note:

```text
The first character of a string has index 0.
```

---

`Topic: Negative Indexing`

```text
Negative indexing starts counting characters from the end of the string. It is useful when you want to access or slice characters relative to the end instead of the beginning.
```

Example:

```python
b = "Hello, World!"

print(b[-5:-2])
```

Output:

```text
orl
```
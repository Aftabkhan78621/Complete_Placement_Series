# Python Notes

## 1. Assign Multiple Values

Python allows you to assign multiple values to multiple variables in a single statement. The number of variables must match the number of values; otherwise, Python will generate an error.

Example:

```python
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)
```

Output:

```text
Orange
Banana
Cherry
```

---

## 2. One Value to Multiple Variables

Python also allows you to assign the same value to multiple variables in a single line.

Example:

```python
x = y = z = "Orange"

print(x)
print(y)
print(z)
```

Output:

```text
Orange
Orange
Orange
```

---

## 3. Output Variables

The `print()` function is used to display variables.

Example:

```python
x = "Python is awesome"

print(x)
```

Output:

```text
Python is awesome
```

---

You can combine text and a variable using the `+` operator.

Example:

```python
x = "awesome"

print("Python is " + x)
```

Output:

```text
Python is awesome
```

---

You can also combine two string variables using the `+` operator.

Example:

```python
x = "Python is "
y = "awesome"

print(x + y)
```

Output:

```text
Python is awesome
```

---

You can add two numeric variables using the `+` operator.

Example:

```python
x = 5
y = 10

print(x + y)
```

Output:

```text
15
```

---

Trying to add a string and a number using the `+` operator causes an error.

Example:

```python
x = 5
y = "John"

print(x + y)
```

Output:

```text
TypeError
```

---

The best way to print multiple variables together is by separating them with commas. This also supports different data types.

Example:

```python
x = 5
y = "John"

print(x, y)
```

Output:

```text
5 John
```

---

## 4. Global Variables

A variable created outside a function is called a **global variable**. Global variables can be accessed both inside and outside functions.

Example:

```python
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
```

Output:

```text
Python is awesome
```

---

If a variable with the same name is created inside a function, it becomes a **local variable**. The global variable remains unchanged.

Example:

```python
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
```

Output:

```text
Python is fantastic
Python is awesome
```

---

## 5. The `global` Keyword

Normally, a variable created inside a function is local. To create a global variable inside a function, use the `global` keyword.

Example:

```python
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
```

Output:

```text
Python is fantastic
```
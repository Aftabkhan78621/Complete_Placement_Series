# Python Notes

## 1. Python Syntax

Python syntax is the set of rules that define how Python programs are written. One of the biggest advantages of Python is its simple and readable syntax, which makes it easy for beginners to learn. Unlike many other programming languages, Python uses **indentation (spaces)** instead of curly braces `{}` to define blocks of code. Every statement is usually written on a new line, making the code clean and easy to understand.

Python code can be executed in two ways:
1. Directly from the Python Interpreter (Command Line).
2. By creating a Python file (`.py`) and running it from the terminal.

Example:

```python
print("Hello, World!")
```

Output:

```text
Hello, World!
```

You can also execute a Python file from the command line:

```cmd
python myfile.py
```

---

## 2. Python Indentation

Indentation means adding spaces before a line of code. In Python, indentation is mandatory because it tells the interpreter which statements belong to a particular block of code. The recommended indentation is **4 spaces**.

Correct Example:

```python
if 5 > 2:
    print("Five is greater than two.")
```

Output:

```text
Five is greater than two.
```

If indentation is missing, Python raises an **IndentationError**.

---

# Interview Questions

### Q1. Why is indentation important in Python?

Python uses indentation to define code blocks instead of curly braces.

### Q2. Can we use tabs instead of spaces?

Yes, but using **4 spaces** is the recommended practice according to **PEP 8**.

---

# Quick Revision

✔ Python uses indentation instead of `{}`.

✔ Use **4 spaces** for indentation.

✔ Save Python files with the **.py** extension.

✔ Run a Python file using:

```cmd
python filename.py
```
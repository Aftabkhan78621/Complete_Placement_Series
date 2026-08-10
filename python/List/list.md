# ==========================================================
#           PYTHON NOTES - LISTS[]
#        Remove | Loop | List Comprehension | Sort
# ==========================================================

Difficulty          : ⭐⭐☆☆☆
Importance          : ⭐⭐⭐⭐⭐
Interview Frequency : Very High

# ==========================================================
# 1. REMOVE LIST ITEMS
# ==========================================================

A Python list can be modified after creation. Items can be removed by:
- Value
- Index
- Deleting the entire list
- Clearing all items

----------------------------------------------------------
1. remove()
----------------------------------------------------------

Definition
- Removes the specified VALUE from the list.
- Removes only the FIRST occurrence if duplicates exist.

Syntax
```python
list.remove(value)
```

Example
```python
thislist = ["apple", "banana", "cherry"]

thislist.remove("banana")

print(thislist)
```

Output
```python
['apple', 'cherry']
```

Important
- Removes by VALUE.
- Removes first matching value only.
- Raises ValueError if value not found.

----------------------------------------------------------
Duplicate Example
----------------------------------------------------------

```python
numbers = [10,20,20,30]

numbers.remove(20)

print(numbers)
```

Output
```python
[10,20,30]
```

Only first 20 is removed.

# ==========================================================
# pop()
# ==========================================================

Definition
- Removes item using INDEX.
- Returns removed element.

Syntax
```python
list.pop(index)
```

Example

```python
thislist = ["apple","banana","cherry"]

thislist.pop(1)

print(thislist)
```

Output

```python
['apple','cherry']
```

Important
- Removes by INDEX.
- Returns removed value.

----------------------------------------------------------
pop() without index
----------------------------------------------------------

If index is omitted,
last item is removed.

Example

```python
thislist = ["apple","banana","cherry"]

thislist.pop()

print(thislist)
```

Output

```python
['apple','banana']
```

Important
- Default index = -1
- Removes last element.

# ==========================================================
# del Keyword
# ==========================================================

Definition
- Deletes items using index.
- Can also delete the entire list.

----------------------------------------------------------
Delete specific index
----------------------------------------------------------

```python
thislist = ["apple","banana","cherry"]

del thislist[0]

print(thislist)
```

Output

```python
['banana','cherry']
```

----------------------------------------------------------
Delete complete list
----------------------------------------------------------

```python
thislist = ["apple","banana","cherry"]

del thislist
```

After this,

```python
print(thislist)
```

Output

```python
NameError
```

Reason
- Variable no longer exists.

# ==========================================================
# clear()
# ==========================================================

Definition
- Removes every element.
- List object still exists.

Syntax

```python
list.clear()
```

Example

```python
thislist=["apple","banana","cherry"]

thislist.clear()

print(thislist)
```

Output

```python
[]
```

Important

Before

```python
["apple","banana","cherry"]
```

After clear()

```python
[]
```

List still exists.

# ==========================================================
Difference
# ==========================================================

remove()
- Remove by value

pop()
- Remove by index
- Returns removed item

del
- Delete index
- Delete slice
- Delete entire list

clear()
- Empty list
- Object remains

# ==========================================================
# 2. LOOP LISTS
# ==========================================================

Looping means visiting every item of the list one by one.

There are four common ways.

1.
for loop

2.
for + range()

3.
while loop

4.
List Comprehension

# ==========================================================
Using for Loop
# ==========================================================

Definition

- Simplest way to iterate list items.

Syntax

```python
for variable in list:
    statement
```

Example

```python
thislist=["apple","banana","cherry"]

for x in thislist:
    print(x)
```

Output

```python
apple
banana
cherry
```

Important

- No index needed.
- Most commonly used.

# ==========================================================
Loop through Index Numbers
# ==========================================================

Definition

Access elements using index.

Uses

- range()
- len()

Syntax

```python
for i in range(len(list)):
```

Example

```python
thislist=["apple","banana","cherry"]

for i in range(len(thislist)):
    print(thislist[i])
```

Output

```python
apple
banana
cherry
```

Explanation

len(thislist)

returns

```python
3
```

range(3)

creates

```python
0
1
2
```

Indexes used

```python
thislist[0]
thislist[1]
thislist[2]
```

Use when index is required.

# ==========================================================
Using while Loop
# ==========================================================

Definition

Loop until condition becomes False.

Example

```python
thislist=["apple","banana","cherry"]

i=0

while i<len(thislist):
    print(thislist[i])
    i=i+1
```

Output

```python
apple
banana
cherry
```

Important

Always increase i

Otherwise

Infinite Loop

# ==========================================================
Loop using List Comprehension
# ==========================================================

Shortest syntax

```python
[print(x) for x in thislist]
```

Output

```python
apple
banana
cherry
```

Used mainly for short code.

# ==========================================================
# 3. LIST COMPREHENSION
# ==========================================================

Definition

List Comprehension provides a shorter syntax for creating a NEW list using an existing iterable.

Instead of writing

```python
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)
```

We simply write

```python
newlist=[x for x in fruits if "a" in x]
```

Result is same.

# ==========================================================
Syntax
# ==========================================================

```python
newlist=[expression for item in iterable if condition]
```

Breakdown

Expression
- Final value inserted.

Item
- Current element.

Iterable
- List
- Tuple
- Set
- Range
- String
- Dictionary

Condition
- Optional filter.
- Keeps only True values.

Return Value

Always creates

NEW LIST

Original list remains unchanged.

# ==========================================================
Condition
# ==========================================================

Condition behaves like a filter.

Example

```python
fruits=["apple","banana","cherry","kiwi","mango"]

newlist=[x for x in fruits if "a" in x]

print(newlist)
```

Output

```python
['apple','banana','mango']
```

Only items containing

"a"

are included.

----------------------------------------------------------
Another Example
----------------------------------------------------------

```python
newlist=[x for x in fruits if x!="apple"]
```

Output

```python
['banana','cherry','kiwi','mango']
```

Condition

```python
x!="apple"
```

returns True

for every item except apple.

# ==========================================================
Without if
# ==========================================================

Condition is optional.

Example

```python
newlist=[x for x in fruits]
```

Output

Copy of original list.

# ==========================================================
Iterable
# ==========================================================

Iterable means any object that can be looped.

Examples

- List
- Tuple
- Set
- Dictionary
- String
- range()

Example

```python
numbers=[x for x in range(10)]
```

Output

```python
[0,1,2,3,4,5,6,7,8,9]
```

----------------------------------------------------------
With Condition
----------------------------------------------------------

```python
numbers=[x for x in range(10) if x<5]
```

Output

```python
[0,1,2,3,4]
```

# ==========================================================
Expression
# ==========================================================

Expression decides

What will be stored.

----------------------------------------------------------
Upper Case
----------------------------------------------------------

```python
newlist=[x.upper() for x in fruits]
```

Output

```python
['APPLE','BANANA','CHERRY','KIWI','MANGO']
```

Expression used

```python
x.upper()
```

----------------------------------------------------------
Constant Expression
----------------------------------------------------------

```python
newlist=["hello" for x in fruits]
```

Output

```python
['hello','hello','hello','hello','hello']
```

Every element becomes

hello

----------------------------------------------------------
if...else Expression
----------------------------------------------------------

Syntax

```python
expression_if_true if condition else expression_if_false
```

Example

```python
newlist=[x if x!="banana" else "orange" for x in fruits]
```

Output

```python
['apple','orange','cherry','kiwi','mango']
```

Explanation

If

x!="banana"

Return x

Else

Return orange

# ==========================================================
# 4. SORT LISTS
# ==========================================================

Definition

sort()

Sorts list in ascending order by default.

Works on

- Strings
- Numbers

# ==========================================================
Alphabetical Sort
# ==========================================================

```python
thislist=["orange","mango","kiwi","pineapple","banana"]

thislist.sort()

print(thislist)
```

Output

```python
['banana','kiwi','mango','orange','pineapple']
```

# ==========================================================
Numeric Sort
# ==========================================================

```python
thislist=[100,50,65,82,23]

thislist.sort()

print(thislist)
```

Output

```python
[23,50,65,82,100]
```

# ==========================================================
Descending Sort
# ==========================================================

Use

```python
reverse=True
```

Strings

```python
thislist.sort(reverse=True)
```

Output

```python
['pineapple','orange','mango','kiwi','banana']
```

Numbers

```python
thislist=[100,50,65,82,23]

thislist.sort(reverse=True)
```

Output

```python
[100,82,65,50,23]
```

# ==========================================================
Custom Sort Function
# ==========================================================

Use

```python
key=function
```

Example

```python
def myfunc(n):
    return abs(n-50)

thislist=[100,50,65,82,23]

thislist.sort(key=myfunc)

print(thislist)
```

Explanation

Distance from

50

100 → 50

50 → 0

65 → 15

82 → 32

23 → 27

Sorted Output

```python
[50,65,23,82,100]
```

Reason

Smaller returned value

comes first.

# ==========================================================
Case Sensitive Sort
# ==========================================================

Default sort is

CASE SENSITIVE

Example

```python
thislist=["banana","Orange","Kiwi","cherry"]

thislist.sort()

print(thislist)
```

Output

```python
['Kiwi','Orange','banana','cherry']
```

Reason

Capital letters

come before

small letters.

# ==========================================================
Case Insensitive Sort
# ==========================================================

Use

```python
key=str.lower
```

Example

```python
thislist=["banana","Orange","Kiwi","cherry"]

thislist.sort(key=str.lower)

print(thislist)
```

Output

```python
['banana','cherry','Kiwi','Orange']
```

Reason

All values are compared in lowercase.

# ==========================================================
Interview Summary
# ==========================================================

remove()
→ Remove by value

pop()
→ Remove by index
→ Returns removed item

del
→ Delete item
→ Delete entire list

clear()
→ Empty list only

for loop
→ Simple iteration

range(len())
→ Iterate using indexes

while
→ Manual iteration

List Comprehension
→ Create new list quickly

sort()
→ Ascending

reverse=True
→ Descending

key=
→ Custom sorting

str.lower
→ Case-insensitive sorting

# ==========================================================
Frequently Asked Interview Questions
# ==========================================================

1. Difference between remove() and pop()?
2. Difference between clear() and del?
3. Difference between sort() and sorted()?
4. What does pop() return?
5. What happens if remove() cannot find value?
6. Why use range(len())?
7. When should while loop be preferred?
8. What is List Comprehension?
9. Explain List Comprehension syntax.
10. Difference between expression and condition?
11. What is iterable?
12. Why use reverse=True?
13. What is key parameter in sort()?
14. Why use str.lower in sorting?
15. Is List Comprehension faster than for loop?
16. Does List Comprehension modify original list?
17. What is returned by clear()?
18. What happens after del list?
19. How to remove last item from a list?
20. How to sort based on custom logic?
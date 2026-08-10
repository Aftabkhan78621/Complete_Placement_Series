==========================================================
               PYTHON DICTIONARIES
==========================================================

Difficulty            : ⭐⭐☆☆☆
Importance            : ⭐⭐⭐⭐⭐
Interview Frequency   : Very High

----------------------------------------------------------
1. Python Dictionaries
----------------------------------------------------------

Definition
----------
• Dictionary is a built-in data type used to store data in Key : Value pairs.
• Each key maps to one value.
• Dictionaries are mutable (changeable).

Syntax
------
```python
dict_name = {
    "key1": value1,
    "key2": value2
}
```

Example
-------
```python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
```

Features
--------
• Stores data in Key : Value format.
• Uses curly braces {}.
• Keys must be unique.
• Values can be duplicated.
• Changeable (Mutable).
• Ordered (Python 3.7+).

Important Points
----------------
• Access data using keys, not indexes.
• Dictionary can store multiple data types.
• Keys are generally immutable types (str, int, tuple).
• One key can have only one value.

----------------------------------------------------------
Ordered or Unordered
----------------------------------------------------------

Python Version        Dictionary Order
--------------------------------------------
Python 3.7+           Ordered
Python 3.6 & Earlier  Unordered

Meaning
-------
• Ordered → Items maintain insertion order.
• Unordered → No guaranteed order.

----------------------------------------------------------
Changeable
----------------------------------------------------------

• Items can be:
  - Modified
  - Added
  - Deleted

----------------------------------------------------------
Duplicates
----------------------------------------------------------

• Duplicate keys are NOT allowed.

Example
-------

```python
car = {
    "brand":"Ford",
    "brand":"BMW"
}
```

Result
------

```python
{'brand':'BMW'}
```

• Latest value overwrites previous value.

----------------------------------------------------------
Length
----------------------------------------------------------

```python
len(dictionary)
```

Returns total number of key-value pairs.

----------------------------------------------------------
dict() Constructor
----------------------------------------------------------

Definition
----------
Creates a dictionary using dict() function.

Syntax
------

```python
dict(key=value, key=value)
```

Example
-------

```python
person = dict(
    name="John",
    age=36,
    country="Norway"
)
```

----------------------------------------------------------
Python Collections Comparison
----------------------------------------------------------

Collection      Ordered   Changeable   Duplicate Values
------------------------------------------------------------
List            Yes       Yes          Yes
Tuple           Yes       No           Yes
Set             No        No*          No
Dictionary      Yes*      Yes          Keys ❌ Values ✅

(* Ordered from Python 3.7+)

----------------------------------------------------------
Interview Questions
----------------------------------------------------------

1. What is a Dictionary?
2. Why are dictionary keys unique?
3. Difference between List and Dictionary?
4. Is Dictionary ordered?
5. Can Dictionary store duplicate values?
6. Why can't duplicate keys exist?
7. What is dict() constructor?

----------------------------------------------------------
Memory Trick
----------------------------------------------------------

Dictionary

KEY  ➜ VALUE

Roll No ➜ Student
ID ➜ Employee
Username ➜ Password
Country ➜ Capital

==========================================================
              ACCESS DICTIONARY ITEMS
==========================================================

Difficulty            : ⭐⭐☆☆☆
Importance            : ⭐⭐⭐⭐⭐
Interview Frequency   : Very High

----------------------------------------------------------
1. Access Items
----------------------------------------------------------

Definition
----------
Retrieve dictionary values using their keys.

Syntax
------

```python
dictionary[key]
```

Example
-------

```python
car["model"]
```

----------------------------------------------------------
2. get()
----------------------------------------------------------

Definition
----------
Returns value of a key.

Syntax
------

```python
dictionary.get(key)
```

Example
-------

```python
car.get("model")
```

Difference
----------

[]              get()
------------------------------
Error           Returns None
Key Required    Safe Access

----------------------------------------------------------
3. keys()
----------------------------------------------------------

Definition
----------
Returns all dictionary keys.

Syntax
------

```python
dictionary.keys()
```

Returns
-------

dict_keys object (View)

Important Points
----------------
• It is a dynamic view.
• If dictionary changes, keys view updates automatically.

----------------------------------------------------------
4. values()
----------------------------------------------------------

Definition
----------
Returns all values.

Syntax
------

```python
dictionary.values()
```

Returns
-------

dict_values object (View)

Important Points
----------------
• Dynamic view.
• Reflects latest dictionary changes.

----------------------------------------------------------
5. items()
----------------------------------------------------------

Definition
----------
Returns key-value pairs.

Syntax
------

```python
dictionary.items()
```

Returns
-------

dict_items object

Example
-------

```python
('brand','Ford')
('year',1964)
```

----------------------------------------------------------
6. Check Key Exists
----------------------------------------------------------

Syntax
------

```python
if "model" in car:
```

Returns
-------

True / False

----------------------------------------------------------
Comparison
----------------------------------------------------------

Method          Returns
-------------------------------
keys()          All Keys
values()        All Values
items()         Key-Value Pairs
get()           Value
[]              Value

----------------------------------------------------------
Interview Questions
----------------------------------------------------------

1. Difference between [] and get()?
2. What does keys() return?
3. What does values() return?
4. What does items() return?
5. How do you check if a key exists?

----------------------------------------------------------
Memory Trick
----------------------------------------------------------

Keys → Name
Values → Data
Items → Both

==========================================================
              CHANGE DICTIONARY ITEMS
==========================================================

Difficulty            : ⭐⭐☆☆☆
Importance            : ⭐⭐⭐⭐☆
Interview Frequency   : High

----------------------------------------------------------
1. Change Value
----------------------------------------------------------

Syntax
------

```python
dictionary[key] = new_value
```

Example
-------

```python
car["year"] = 2018
```

----------------------------------------------------------
2. update()
----------------------------------------------------------

Definition
----------
Updates existing key.
If key doesn't exist, it is added.

Syntax
------

```python
dictionary.update({"key":value})
```

Example
-------

```python
car.update({"year":2020})
```

Important Points
----------------
• Accepts dictionary or iterable of key-value pairs.
• Existing key → Updated.
• New key → Added.

----------------------------------------------------------
Comparison
----------------------------------------------------------

Method              Existing Key      New Key
-----------------------------------------------
[]                  Update            Add
update()            Update            Add

----------------------------------------------------------
Interview Questions
----------------------------------------------------------

1. Difference between [] and update()?
2. Can update() add new keys?
3. Which method is used to modify values?

==========================================================
               ADD DICTIONARY ITEMS
==========================================================

Difficulty            : ⭐⭐☆☆☆
Importance            : ⭐⭐⭐⭐☆
Interview Frequency   : High

----------------------------------------------------------
1. Add Item
----------------------------------------------------------

Syntax
------

```python
dictionary[new_key] = value
```

Example
-------

```python
car["color"] = "Red"
```

----------------------------------------------------------
2. update()
----------------------------------------------------------

Definition
----------
Adds item if key doesn't exist.

Syntax
------

```python
dictionary.update({"color":"Red"})
```

----------------------------------------------------------
Comparison
----------------------------------------------------------

Method          Purpose
------------------------------
[]              Add/Update
update()        Add/Update

----------------------------------------------------------
Interview Questions
----------------------------------------------------------

1. How do you add a new key?
2. Can update() insert new keys?

==========================================================
             REMOVE DICTIONARY ITEMS
==========================================================

Difficulty            : ⭐⭐⭐☆☆
Importance            : ⭐⭐⭐⭐⭐
Interview Frequency   : Very High

----------------------------------------------------------
Methods
----------------------------------------------------------

Method          Purpose
------------------------------------
pop()           Remove by key
popitem()       Remove last item
del             Delete key/object
clear()         Empty dictionary

----------------------------------------------------------
1. pop()
----------------------------------------------------------

Syntax
------

```python
dictionary.pop(key)
```

Removes specified key.

----------------------------------------------------------
2. popitem()
----------------------------------------------------------

Syntax
------

```python
dictionary.popitem()
```

Python 3.7+
-----------
• Removes last inserted item.

Python <3.7
-----------
• Removes random item.

----------------------------------------------------------
3. del
----------------------------------------------------------

Delete Key

```python
del dictionary[key]
```

Delete Entire Dictionary

```python
del dictionary
```

----------------------------------------------------------
4. clear()
----------------------------------------------------------

Syntax
------

```python
dictionary.clear()
```

Removes all items but dictionary object remains.

----------------------------------------------------------
Comparison
----------------------------------------------------------

Method          Removes
---------------------------------------
pop()           Specific key
popitem()       Last item
del key         One key
del dict        Entire dictionary
clear()         All items only

----------------------------------------------------------
Interview Questions
----------------------------------------------------------

1. Difference between pop() and popitem()?
2. Difference between del and clear()?
3. Which method deletes the entire dictionary?
4. Which method removes the last inserted item?

----------------------------------------------------------
Memory Trick
----------------------------------------------------------

pop()      → Particular Key
popitem()  → Last Item
clear()    → Empty Dictionary
del        → Delete Object

==========================================================
              LOOP DICTIONARIES
==========================================================

Difficulty            : ⭐⭐⭐☆☆
Importance            : ⭐⭐⭐⭐⭐
Interview Frequency   : Very High

----------------------------------------------------------
Loop Through Dictionary
----------------------------------------------------------

Definition
----------
Iterate through dictionary using for loop.

----------------------------------------------------------
1. Loop Keys
----------------------------------------------------------

Syntax
------

```python
for key in dictionary:
    print(key)
```

OR

```python
for key in dictionary.keys():
```

----------------------------------------------------------
2. Loop Values
----------------------------------------------------------

Syntax
------

```python
for key in dictionary:
    print(dictionary[key])
```

OR

```python
for value in dictionary.values():
```

----------------------------------------------------------
3. Loop Keys & Values
----------------------------------------------------------

Syntax
------

```python
for key, value in dictionary.items():
    print(key, value)
```

----------------------------------------------------------
Comparison
----------------------------------------------------------

Method              Returns
-----------------------------------
for x in dict       Keys
keys()              Keys
values()            Values
items()             Keys + Values

----------------------------------------------------------
Interview Questions
----------------------------------------------------------

1. How do you iterate over dictionary keys?
2. How do you iterate over values?
3. Which method returns both key and value?
4. Difference between keys(), values(), and items()?

----------------------------------------------------------
Memory Trick
----------------------------------------------------------

keys()   → Keys

values() → Values

items()  → Both

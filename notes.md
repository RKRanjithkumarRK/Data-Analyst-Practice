# 🧠 Day 1 Notes – Python Fundamentals

## 🎯 Goal of the Day
Understand Python’s core behavior — how **lists**, **loops**, and **dictionaries** work behind the scenes.  
These are the foundation for manipulating data in Pandas, performing analysis, and writing efficient code.

---

## 🧩 Concepts Covered
### 1. Python Basics
- Python runs using an **interpreter**; indentation defines code blocks.
- Common data types: `int`, `float`, `str`, `bool`.
- Type casting functions: `int()`, `float()`, `str()`.

### 2. Lists
- Created using square brackets: `my_list = [1, 2, 3]`
- Support indexing, slicing, and nesting.
- Mutable (can be changed).
- Common methods: `append()`, `insert()`, `remove()`, `pop()`, `sort()`.
- List comprehension: `[x**2 for x in range(5)]` for concise looping.

### 3. Loops
- `for` loops for sequential iteration.
- `while` loops for condition-based iteration.
- `break`, `continue`, `pass` control loop behavior.
- Nested loops for 2D patterns or matrix-like operations.

### 4. Dictionaries
- Store key-value pairs: `{'name': 'Alice', 'age': 30}`
- Access using `dict[key]` or `dict.get(key)`.
- Methods: `.items()`, `.keys()`, `.values()`, `.pop()`.
- Dictionary comprehension: `{x: x**2 for x in range(5)}`.

### 5. Mutable vs Immutable
- **Mutable:** Lists, Dictionaries → Can be changed in-place.
- **Immutable:** Tuples, Strings → Cannot be changed once created.
- Important for understanding variable assignments and function parameters.

---

## 💻 Programs Practiced
1. Find the largest and smallest number in a list (without built-ins).
2. Count how many times “Football” appears in a list (manual counter).
3. Print number patterns using nested loops.
4. Calculate the sum of numbers from 1 to N.
5. Display a multiplication table for 2.
6. Demonstrate dictionary creation, modification, and iteration.

---

## 🧠 Key Takeaways
- Always initialize variables before loops (e.g., `count = 0`).
- Avoid built-ins initially to strengthen logic understanding.
- Comprehensions are powerful and concise, but clarity matters first.
- Consistency in naming and indentation improves readability.
- Modular code (functions) makes future reuse in data analysis easier.

---

## ⏭ Next Step (Day 2)
Learn **Functions** and **Object-Oriented Programming (OOP)** concepts:
- Function definitions, parameters, and return values.
- Classes, objects, constructors, inheritance.

---

## 🗂️ Files for Day 1
- `problems.py` → Clean modular scripts for Python fundamentals.
- `solutions.ipynb` → Executed notebook with visible outputs.
- `notes.md` → Concept summary (this file).

---

## 🧩 Reflection
Day 1 built a strong logical foundation. Understanding loops, data structures, and flow control prepares for data manipulation in Pandas and beyond.  
Next: start building reusable code structures through functions and OOP to organize analysis workflows efficiently.


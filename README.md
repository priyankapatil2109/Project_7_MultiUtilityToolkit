# Multi-Utility Toolkit 🛠️

A Python-based Multi-Utility Toolkit that integrates multiple standard modules, custom modules, and packages to perform a variety of tasks.

---


---

## 📁 Project Structure

```
MultiUtilityToolkit/
├── main.py
└── toolkit/
    ├── __init__.py
    ├── datetime_module.py
    ├── math_module.py
    ├── random_module.py
    ├── uuid_module.py
    └── file_module.py
```

---

## 📌 About the Project

This project demonstrates Python's modular structure by organizing utility functions into separate modules grouped inside a package called `toolkit`. The main menu lets users choose from 6 different utility features, each handled by its own module.

---

## ✅ Features

### 1. 📅 Datetime and Time Operations
- Display current date and time
- Calculate difference between two dates
- Format date into custom format
- Stopwatch
- Countdown Timer

### 2. ➕ Mathematical Operations
- Calculate Factorial
- Solve Compound Interest
- Trigonometric Calculations (Sin, Cos, Tan)
- Area of Geometric Shapes (Circle, Rectangle)

### 3. 🎲 Random Data Generation
- Generate Random Number
- Generate Random List
- Create Random Password
- Generate Random OTP

### 4. 🔑 Generate Unique Identifiers (UUID)
- Generate UUID4
- Generate UUID1

### 5. 📂 File Operations (Custom Module)
- Create a new file
- Write to a file
- Read from a file
- Append to a file

### 6. 🔍 Explore Module Attributes (dir())
- Dynamically explore attributes of any built-in Python module

---


## 💻 Example Output

```
==========================
Welcome to Multi-Utility Toolkit
==========================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
==========================
Enter your choice:
```

---

## 🧰 Modules Used

| Module | Type | Purpose |
|--------|------|---------|
| `datetime` | Built-in | Date and time operations |
| `time` | Built-in | Stopwatch and countdown |
| `math` | Built-in | Mathematical calculations |
| `random` | Built-in | Random data generation |
| `uuid` | Built-in | Unique identifier generation |
| `importlib` | Built-in | Dynamic module exploration |
| `file_module` | Custom | File read/write operations |
| `math_module` | Custom | Area and unit calculations |

---

## 📝 Concepts Used

- Python Modules and Packages
- `__init__.py` for package initialization
- `__name__` and `__main__` paradigm
- Built-in modules: `datetime`, `math`, `random`, `uuid`
- Custom modules with reusable functions
- Menu-driven user interface
- `dir()` for dynamic module exploration

---


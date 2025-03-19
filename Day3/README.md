## Types of Modules

1. Built-in Modules: Pre-installed with Python (e.g., `math`, `os`, `sys`).
2. User-defined Modules: Created by the user, like `math_operations` above.
3. Third-party Modules: Installed using `pip` (e.g., `numpy`, `pandas`).

# Circular Import-
A circular import happens when two or more modules depend on each other during import.This infinite loop leads to an ImportError or AttributeError.
Import inside function to avoid circular import

# Dynamic Import
Dynamic module loading means importing a module at runtime instead of at the beginning of the script. This is useful when you don’t know in advance which module or function will be used.

# Custom Module
A custom module is a Python file that contains functions, classes, or variables, which can be imported and used in other scripts.

# Measuring Import Time
The time module helps measure how long different import methods take.
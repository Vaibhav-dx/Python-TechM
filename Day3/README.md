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

Investigate sys.path
  - sys.path.append()-Temporary, valid for current session.
  - Modify PYTHONPATH	Permanent solution for custom imports(Add the path to PYTHONPATH in your system’s environment variables.)
  - Check sys.path	Debug import issues

# Mocking Modules for Testing
  - Mocking is a technique used in testing to replace real dependencies with fake ones. This helps isolate the function being tested and control its behavior.

# Import Side Effects
  - Import side effects occur when a module automatically executes code as soon as it is imported, rather than just defining functions, classes, or variables. This can be useful for setting up configurations, logging, or initializing resources but can also cause unexpected behavior.
  # Logging & Configuration
    - import logging
    - print("Setting up logging...")
    - logging.basicConfig(level=logging.DEBUG)
  # Database Connections or Setup
    - import sqlite3
    - print("Connecting to database...")
    - conn = sqlite3.connect("my_database.db")
  # To prevent a module from executing code during import
    - def greet():
    - return "Hello from my_module!"
    - if __name__ == "__main__":
    - print("This runs only when executed directly!")

# Investigate Python’s Import Caching
  - When you import a module in Python, it is cached in sys.modules to avoid redundant imports and improve   performance. This means that subsequent imports of the same module do not reload it—Python just reuses the cached version.
# How to reload module
   - import importlib
   - import mymodule
   - importlib.reload(mymodule)  
# Inspect all loaded modules
   - import sys
   - print(sys.modules.keys()) 
# In Python, a context manager is an object with defined methods that you can use in combination with the `with` statement.
# A context manager allows properly managing resources so that you can specify exactly what happens before a block of code runs
# and after a block of code completes its execution.
# Specifically, a context manager needs to implement two methods:

# - `__enter__()`: This method is executed at the beginning of the `with` block.
# Its return value is bound to the target of the `with` statement, if it has one.
#
# - `__exit__(exc_type, exc_val, exc_tb)`: This method is executed after the completion of the block of code within the `with` statement,
# and it's used to perform clean-up actions.
#
# A classic use of context managers is file handling. You may want to open a file, write to the file, and then close it.
# Using a context manager ensures the file is closed once you're done with it, even if errors occur while the file is open.
# Context Managers are most commonly used with file operations, threading Locks, and creating temporary resources
# that need specific startup/cleanup procedures but are not restrict to this and can be created
# to manage almost any kind of resource that needs proper management.

with open('context_manager_file.txt', 'w') as file:
     file.write('Hello, world!')

class ContextManager:

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        print(exc_type, exc_value, exc_tb, sep="\n")
        return "exit called"

    def __enter__(self):
         print("Entering the context...")
         return "Hello, World!"


with ContextManager() as cm:
     print(cm)
